# Standard Library

# Third Party Stuff
import pytest
from django.urls import reverse

# from tests import factories as f

pytestmark = pytest.mark.django_db


@pytest.mark.parametrize(
    "date_to,date_from,origin,destination,missing_field",
    [
        ("2016-01-10", "2016-01-01", "north_europe_main", None, "destination"),
        ("2016-01-10", "2016-01-01", None, "CNSG", "origin"),
        ("2016-01-10", None, "north_europe_main", "CNSG", "date_from"),
        (None, "2016-01-01", "north_europe_main", "CNSG", "date_to"),
    ],
)
def test_ports_rates_api_missing_params(
    date_to, date_from, origin, destination, missing_field, client
):
    url = reverse("ports-rates")
    params = {
        "date_to": date_to,
        "date_from": date_from,
        "origin": origin,
        "destination": destination,
    }
    params = "&".join(
        ["{}={}".format(k, v) for k, v in params.items() if v is not None]
    )
    url = f"{url}?{params}"
    response = client.get(url)
    errors = response.json().get("errors", [])
    error_type = response.json().get("error_type", None)
    assert response.status_code == 400
    assert len(errors) == 1
    assert errors[0]["field"] == missing_field
    assert errors[0]["message"] == "This field is required."
    assert error_type == "ValidationError"


@pytest.mark.parametrize(
    "date_to,date_from,origin,destination,result",
    [
        (
            "2016-01-12",
            "2016-01-11",
            "CNYTN",
            "NOORK",
            [
                {"day": "2016-01-11", "average_price": 2063},
                {"day": "2016-01-12", "average_price": None},
            ],
        ),
        (
            "2016-01-03",
            "2016-01-02",
            "CNGGZ",
            "scandinavia",
            [
                {"day": "2016-01-02", "average_price": 1714},
                {"day": "2016-01-03", "average_price": 1714},
            ],
        ),
    ],
)
def test_ports_rates_api_success(
    date_to, date_from, origin, destination, result, client
):
    url = reverse("ports-rates")
    params = {
        "date_to": date_to,
        "date_from": date_from,
        "origin": origin,
        "destination": destination,
    }
    params = "&".join(
        ["{}={}".format(k, v) for k, v in params.items() if v is not None]
    )
    url = f"{url}?{params}"
    response = client.get(url)
    data = response.json()
    assert response.status_code == 200
    assert len(data) == len(result)
    assert data == result


def test_ports_list_api(client):
    url = reverse("ports-list")
    response = client.get(url)
    assert response.status_code == 501


def test_ports_create_api(client):
    url = reverse("ports-list")
    response = client.post(url)
    assert response.status_code == 501


def test_ports_retrieve_api(client):
    url = reverse("ports-list")
    url = f"{url}/random-port-id"
    response = client.get(url)
    assert response.status_code == 501


def test_ports_put_api(client):
    url = reverse("ports-list")
    url = f"{url}/random-port-id"
    response = client.put(url)
    assert response.status_code == 501


def test_ports_patch_api(client):
    url = reverse("ports-list")
    url = f"{url}/random-port-id"
    response = client.patch(url)
    assert response.status_code == 501


def test_ports_delete_api(client):
    url = reverse("ports-list")
    url = f"{url}/random-port-id"
    response = client.patch(url)
    assert response.status_code == 501
