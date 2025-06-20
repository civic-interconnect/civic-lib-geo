"""
src/civic_lib_geo/geojson_utils.py - GeoJSON utility functions for Civic Interconnect.
"""

import json
from pathlib import Path
from typing import Any

import geopandas as gpd

__all__ = [
    "load_geojson",
    "read_geojson_props",
    "save_geojson",
    "simplify_geojson",
]


def load_geojson(path: Path) -> gpd.GeoDataFrame:
    """
    Load a GeoJSON file into a GeoDataFrame.

    Args:
        path (Path): Path to the GeoJSON file.

    Returns:
        gpd.GeoDataFrame: A GeoDataFrame with geometries and attributes.
    """
    return gpd.read_file(path)


def read_geojson_props(path: Path) -> list[dict[str, Any]]:
    """
    Load only the properties from a GeoJSON file.

    Args:
        path (Path): Path to the GeoJSON file.

    Returns:
        list[dict[str, Any]]: A list of property dictionaries from each feature.
    """
    with open(path, encoding="utf-8") as f:
        data = json.load(f)
    return [feature["properties"] for feature in data["features"]]


def save_geojson(gdf: gpd.GeoDataFrame, path: Path, indent: int = 2) -> Path:
    """
    Save a GeoDataFrame to GeoJSON format.

    Args:
        gdf (gpd.GeoDataFrame): The GeoDataFrame to save.
        path (Path): Output file path.
        indent (int): Indentation level for formatting (unused by GeoPandas but included for consistency).

    Returns:
        Path: The path to the saved file.
    """
    gdf.to_file(path, driver="GeoJSON")
    return path


def simplify_geojson(gdf: gpd.GeoDataFrame, tolerance: float) -> gpd.GeoDataFrame:
    """
    Return a simplified copy of the GeoDataFrame using the given tolerance.

    Args:
        gdf (gpd.GeoDataFrame): The input GeoDataFrame.
        tolerance (float): Tolerance for simplification (smaller values retain more detail).

    Returns:
        gpd.GeoDataFrame: A new GeoDataFrame with simplified geometry.
    """
    return gdf.copy().assign(geometry=gdf.geometry.simplify(tolerance, preserve_topology=True))
