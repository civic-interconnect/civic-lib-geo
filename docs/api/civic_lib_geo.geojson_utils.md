# Module `civic_lib_geo.geojson_utils`

## Classes

### `Any(self, /, *args, **kwargs)`

Special type indicating an unconstrained type.

- Any is compatible with every type.
- Any assumed to have all methods.
- All values assumed to be instances of Any.

Note that all the above statements are true from the point of view of
static type checkers. At runtime, Any should not be used with instance
checks.

### `Callable(self, /, *args, **kwargs)`

No description available.

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

### `get_file_size_mb(path: str | pathlib.Path) -> float`

Return the file size in megabytes (MB).

Args:
    path: Path to the file.

Returns:
    File size in megabytes.

Raises:
    FileNotFoundError: If the file does not exist.

### `is_valid_geojson_feature_collection(obj: dict) -> bool`

Quick check if an object looks like a valid GeoJSON FeatureCollection.

Args:
    obj: Dictionary to check.

Returns:
    True if valid structure, else False.

### `list_geojson_files(folder: pathlib.Path) -> list[pathlib.Path]`

Return a list of .geojson files in the specified folder.

Args:
    folder (Path): Directory to search.

Returns:
    list[Path]: List of .geojson file paths.

### `load_geojson(path: pathlib.Path) -> geopandas.geodataframe.GeoDataFrame`

Load a GeoJSON file into a GeoDataFrame.

Args:
    path (Path): Path to the GeoJSON file.

Returns:
    gpd.GeoDataFrame: A GeoDataFrame with geometries and attributes.

### `needs_chunking(path: str | pathlib.Path, max_mb: float = 25.0) -> bool`

Determine whether the GeoJSON file exceeds the size threshold.

Args:
    path: Path to the file.
    max_mb: Maximum file size before chunking is recommended.

Returns:
    True if file exceeds max_mb, else False.

### `read_geojson_props(path: pathlib.Path) -> list[dict[str, typing.Any]]`

Load only the properties from a GeoJSON file.

Args:
    path (Path): Path to the GeoJSON file.

Returns:
    list[dict[str, Any]]: A list of property dictionaries from each feature.

### `save_geojson(gdf: 'gpd.GeoDataFrame', path: pathlib.Path, indent: int = 2) -> pathlib.Path`

Save a GeoDataFrame to GeoJSON format.

Args:
    gdf (gpd.GeoDataFrame): The GeoDataFrame to save.
    path (Path): Output file path.
    indent (int): Indentation level for formatting (unused by GeoPandas but included for consistency).

Returns:
    Path: The path to the saved file.

### `simplify_geojson(gdf: geopandas.geodataframe.GeoDataFrame, tolerance: float) -> geopandas.geodataframe.GeoDataFrame`

Return a simplified copy of the GeoDataFrame using the given tolerance.

Args:
    gdf (gpd.GeoDataFrame): The input GeoDataFrame.
    tolerance (float): Tolerance for simplification (smaller values retain more detail).

Returns:
    gpd.GeoDataFrame: A new GeoDataFrame with simplified geometry.
