# Module `civic_lib_geo.shapefile_utils`

## Classes

### `Path(self, *args, **kwargs)`

PurePath subclass that can make system calls.

Path represents a filesystem path but unlike PurePath, also offers
methods to do system calls on path objects. Depending on your system,
instantiating a Path will return either a PosixPath or a WindowsPath
object. You can also instantiate a PosixPath or WindowsPath directly,
but cannot instantiate a WindowsPath on a POSIX system or vice versa.

## Functions

### `convert_shapefile_to_geojson(shp_path: pathlib.Path, geojson_path: pathlib.Path) -> pathlib.Path`

Convert a shapefile to a GeoJSON file.

Args:
    shp_path (Path): Path to the source shapefile (.shp).
    geojson_path (Path): Path to the output GeoJSON file.

Returns:
    Path: The path to the saved GeoJSON file.

### `load_shapefile(path: pathlib.Path) -> geopandas.geodataframe.GeoDataFrame`

Load a shapefile into a GeoDataFrame.

Args:
    path (Path): Path to the shapefile (.shp).

Returns:
    gpd.GeoDataFrame: A GeoDataFrame with geometries and attributes.
