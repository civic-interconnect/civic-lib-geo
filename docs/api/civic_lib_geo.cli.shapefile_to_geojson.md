# Module `civic_lib_geo.cli.shapefile_to_geojson`

## Classes

### `Path(self, *args, **kwargs)`

PurePath subclass that can make system calls.

Path represents a filesystem path but unlike PurePath, also offers
methods to do system calls on path objects. Depending on your system,
instantiating a Path will return either a PosixPath or a WindowsPath
object. You can also instantiate a PosixPath or WindowsPath directly,
but cannot instantiate a WindowsPath on a POSIX system or vice versa.

## Functions

### `main(shp_path: pathlib.Path, geojson_path: pathlib.Path) -> int`

Convert a shapefile to GeoJSON.

Args:
    shp_path (Path): Input .shp file path.
    geojson_path (Path): Output .geojson file path.

Returns:
    int: 0 if success, 1 on error.
