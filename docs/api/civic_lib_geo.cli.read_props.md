# Module `civic_lib_geo.cli.read_props`

## Classes

### `Path(self, *args, **kwargs)`

PurePath subclass that can make system calls.

Path represents a filesystem path but unlike PurePath, also offers
methods to do system calls on path objects. Depending on your system,
instantiating a Path will return either a PosixPath or a WindowsPath
object. You can also instantiate a PosixPath or WindowsPath directly,
but cannot instantiate a WindowsPath on a POSIX system or vice versa.

## Functions

### `apply_to_geojson_folder(folder: pathlib.Path, action_fn: collections.abc.Callable, *, suffix: str = '_processed.geojson', tolerance: float | None = None, max_features: int | None = None)`

Apply an action to every .geojson file in a folder.

Args:
    folder (Path): Path to folder containing .geojson files.
    action_fn (Callable): Function to apply to each file.
    suffix (str): Suffix to add to output filenames.
    tolerance (float | None): Optional tolerance value for simplification.
    max_features (int | None): Optional limit for chunking.

### `main(path: pathlib.Path, all_files: bool = False) -> int`

Display feature properties for a single file or all .geojson files in a folder.

Args:
    path (Path): File or folder path.
    all_files (bool): If True and path is a folder, process all .geojson files inside.

Returns:
    int: 0 if success, 1 on error.

### `read_geojson_props(path: pathlib.Path) -> list[dict[str, typing.Any]]`

Load only the properties from a GeoJSON file.

Args:
    path (Path): Path to the GeoJSON file.

Returns:
    list[dict[str, Any]]: A list of property dictionaries from each feature.

### `read_props_one(path: pathlib.Path, output: pathlib.Path | None = None, max_rows: int = 5)`

Print properties from the first few features in a GeoJSON file.

Args:
    path (Path): Path to the GeoJSON file.
    output (Path | None): Ignored in this function (kept for compatibility).
    max_rows (int): Number of feature properties to preview.
