# Module `civic_lib_geo.topojson_utils`

## Classes

### `Path(self, *args, **kwargs)`

PurePath subclass that can make system calls.

Path represents a filesystem path but unlike PurePath, also offers
methods to do system calls on path objects. Depending on your system,
instantiating a Path will return either a PosixPath or a WindowsPath
object. You can also instantiate a PosixPath or WindowsPath directly,
but cannot instantiate a WindowsPath on a POSIX system or vice versa.

## Functions

### `convert_topojson_to_geojson(topojson_path: pathlib.Path, geojson_path: pathlib.Path) -> pathlib.Path`

Convert a TopoJSON file to a GeoJSON file using geopandas or CLI tools.
