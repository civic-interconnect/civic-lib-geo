# Module `civic_lib_geo.cli.simplify_geojson`

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

### `load_geojson(path: pathlib.Path) -> geopandas.geodataframe.GeoDataFrame`

Load a GeoJSON file into a GeoDataFrame.

Args:
    path (Path): Path to the GeoJSON file.

Returns:
    gpd.GeoDataFrame: A GeoDataFrame with geometries and attributes.

### `main(path: pathlib.Path, tolerance: float = 0.01, output: pathlib.Path | None = None, all_files: bool = False)`

Simplify a single file or all .geojson files in a folder.

Args:
    path (Path): Input file or folder.
    tolerance (float): Simplification tolerance.
    output (Path | None): Output file path for single file use.
    all_files (bool): If True and path is a folder, simplify all .geojson files.

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

### `simplify_one(path: pathlib.Path, tolerance: float, output: pathlib.Path)`

Simplify a single GeoJSON file and write the output.

Args:
    path (Path): Path to the original GeoJSON file.
    tolerance (float): Tolerance for simplification.
    output (Path): Output path for the simplified file.
