--
-- Name: regions; Type: TABLE; Schema: tasks; Owner: -
--
DROP TABLE IF EXISTS public.regions;


CREATE TABLE regions (
    slug text NOT NULL,
    name text NOT NULL,
    parent_slug text
);





--
-- Data for Name: regions; Type: TABLE DATA; Schema: tasks; Owner: -
--
INSERT INTO public.regions(slug, name, parent_slug) VALUES
('china_main',	'China Main', NULL),
('northern_europe',	'Northern Europe', NULL),
('stockholm_area',	'Stockholm Area',	'scandinavia'),
('uk_sub',	'UK Sub',	'north_europe_sub'),
('finland_main',	'Finland Main',	'baltic'),
('baltic_main',	'Baltic Main',	'baltic'),
('poland_main',	'Poland Main',	'baltic,'),
('kattegat',	'Kattegat',	'scandinavia'),
('norway_north_west',	'Norway North West',	'scandinavia'),
('norway_south_east',	'Norway South East',	'scandinavia'),
('norway_south_west',	'Norway South West',	'scandinavia'),
('uk_main',	'UK Main',	'north_europe_main'),
('russia_north_west',	'Russia North West',	'northern_europe'),
('north_europe_main',	'North Europe Main',	'northern_europe'),
('north_europe_sub',	'North Europe Sub',	'northern_europe'),
('china_east_main',	'China East Main',	'china_main'),
('china_south_main',	'China South Main',	'china_main'),
('baltic',	'Baltic',	'northern_europe'),
('scandinavia',	'Scandinavia',	'northern_europe'),
('china_north_main',	'China North Main',	'china_main');
