# Standard Library
from typing import Any, List

# Third Party Stuff
from django.db import connection

from .utils import dict_fetchall


def child_elements(
    table_name: str, parent_key: str, child_key: str, filter_parent_key: str
) -> List[Any]:
    """Returns all the children of a parent
    Args:
        table_name: Table name
        parent_key: Parent field name
        child_key: Children field name
        filter_parent_key: Filter value on the parent_key
    Returns:
        List of dict [{child_key: ''},..]
    """
    data = []
    query = f"""
        WITH RECURSIVE children AS (
            SELECT
                *
                FROM {table_name}
                WHERE {parent_key} = %s
            UNION
                SELECT
                    p.*
                FROM {table_name} p
                INNER JOIN children c
                ON c.{child_key} = p.{parent_key}
        ) SELECT
            {child_key}
        FROM
            children;
    """
    with connection.cursor() as cursor:
        cursor.execute(query, [filter_parent_key])
        data = dict_fetchall(cursor)
    return data


def average_prices_per_day(
    date_to: str, date_from: str, origin: str, destination: str
) -> List[Any]:
    """Returns the average price between an origin and destination
        over a period of time
        Note: If three or more price entries are there then
        only the average price is calculated
    Args:
        date_to: Maximum Date (inclusive)
        date_from: Minimum Date (inclusive)
        origin: origin (port code or region)
        destination: destination (dest code or region)
    Returns:
        List of dict [{day: '2016-11-11', average_price: 1111},..]
    """
    data = []
    dest_child_ports_data = child_elements(
        "regions", "parent_slug", "slug", destination
    )
    origin_child_ports_data = child_elements("regions", "parent_slug", "slug", origin)
    dest_child_ports = ", ".join(
        ["'{}'".format(v["slug"]) for v in dest_child_ports_data if v.get("slug", None)]
    )
    origin_child_ports = ", ".join(
        [
            "'{}'".format(v["slug"])
            for v in origin_child_ports_data
            if v.get("slug", None)
        ]
    )
    query_for_origin_condition = (
        f"or origin_port.parent_slug in ({origin_child_ports})"
        if len(origin_child_ports)
        else ""
    )
    query_for_dest_condition = (
        f"or dest_port.parent_slug in ({dest_child_ports})"
        if len(dest_child_ports)
        else ""
    )
    query = f"""
        SELECT
            price.day,
            CASE
                WHEN count(*) > 2 THEN avg(price.price)::numeric::integer ELSE NULL
            END as average_price FROM prices price
        LEFT JOIN ports origin_port
            ON price.orig_code = origin_port.code
        LEFT JOIN ports dest_port
            ON price.dest_code = dest_port.code
        WHERE
            (price.orig_code = %s or origin_port.parent_slug = %s {query_for_origin_condition})
            AND
            (price.dest_code = %s or dest_port.parent_slug = %s {query_for_dest_condition})
            AND
            price.day >= %s::date
            AND
            price.day <= %s::date
        GROUP BY
        price.day
    """
    with connection.cursor() as cursor:
        cursor.execute(
            query, [origin, origin, destination, destination, date_from, date_to]
        )
        data = dict_fetchall(cursor)
    return data
