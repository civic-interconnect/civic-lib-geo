from pathlib import Path

import geopandas as gpd

from civic_lib_geo.geojson_utils import (
    load_geojson,
    read_geojson_props,
    simplify_geojson,
)

TEST_DATA = Path(__file__).parent / "data" / "test.geojson"


def test_load_geojson():
    gdf = load_geojson(TEST_DATA)
    assert isinstance(gdf, gpd.GeoDataFrame)
    assert not gdf.empty


def test_read_geojson_props():
    props = read_geojson_props(TEST_DATA)
    assert isinstance(props, list)
    assert isinstance(props[0], dict)


def test_simplify_geojson():
    gdf = load_geojson(TEST_DATA)
    simplified = simplify_geojson(gdf, tolerance=0.01)
    assert isinstance(simplified, gpd.GeoDataFrame)
    assert len(simplified) == len(gdf)
