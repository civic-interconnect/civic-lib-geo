# Module `civic_lib_geo.cli.cli`

## Classes

### `Path(self, *args, **kwargs)`

PurePath subclass that can make system calls.

Path represents a filesystem path but unlike PurePath, also offers
methods to do system calls on path objects. Depending on your system,
instantiating a Path will return either a PosixPath or a WindowsPath
object. You can also instantiate a PosixPath or WindowsPath directly,
but cannot instantiate a WindowsPath on a POSIX system or vice versa.

## Functions

### `check_size_command(path: pathlib.Path)`

Report the size of a GeoJSON file and whether it exceeds the GitHub Pages 25MB limit.

### `chunk_command(folder: pathlib.Path = <typer.models.ArgumentInfo object at 0x00000227578DD550>, max_features: int = 500, single_file: pathlib.Path = <typer.models.OptionInfo object at 0x0000022756F65640>)`

Chunk a GeoJSON file or all files in a folder into smaller files with limited features.

### `main() -> int`

No description available.

### `props_command(path: pathlib.Path)`

Display the property keys from the first feature of a GeoJSON file.

### `shapefile_to_geojson_command(shp_path: pathlib.Path, geojson_path: pathlib.Path)`

Convert a shapefile to GeoJSON.

### `simplify_command(folder: pathlib.Path = <typer.models.ArgumentInfo object at 0x00000227578DD550>, tolerance: float = 0.01, single_file: pathlib.Path = <typer.models.OptionInfo object at 0x0000022756F65640>)`

Simplify one GeoJSON file or all files in a folder using the given tolerance.

### `topojson_to_geojson_command(topo_path: pathlib.Path, geojson_path: pathlib.Path)`

Convert a TopoJSON file to GeoJSON using GeoPandas (if supported).
