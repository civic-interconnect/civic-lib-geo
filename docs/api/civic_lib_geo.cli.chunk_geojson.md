# Module `civic_lib_geo.cli.chunk_geojson`

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

### `chunk_geojson_features(geojson: dict, max_features: int = 500, output_dir: str | pathlib.Path = 'chunks', base_name: str = 'chunk') -> list[pathlib.Path]`

Split a GeoJSON FeatureCollection into multiple smaller files.

Args:
    geojson: Loaded GeoJSON dictionary (must contain a 'features' list).
    max_features: Maximum number of features per chunk.
    output_dir: Directory to write chunked files to.
    base_name: Base filename prefix for each chunk.

Returns:
    List of Paths to chunked files.

Raises:
    ValueError: If 'features' is missing or not a list.

### `chunk_one(path: pathlib.Path, max_features: int, output_dir: pathlib.Path)`

Chunk a single GeoJSON file and write the output files.

Args:
    path (Path): Path to input GeoJSON file.
    max_features (int): Max features per chunk.
    output_dir (Path): Output folder to store chunks.

### `main(path: pathlib.Path, max_features: int = 500, output_dir: pathlib.Path = WindowsPath('chunks'), all_files: bool = False) -> int`

Chunk a single file or all .geojson files in a folder.

Args:
    path (Path): Input file or folder path.
    max_features (int): Max features per chunk.
    output_dir (Path): Directory to store chunks.
    all_files (bool): If True and path is a folder, chunk all files in it.

Returns:
    int: Exit code, 0 if success, 1 if failure.
