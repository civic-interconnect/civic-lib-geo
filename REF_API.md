# Civic Interconnect API Documentation

# API for `civic_lib_geo.constants`

# API for `civic_lib_geo.fips_utils`

## `Path(*args, **kwargs)`
PurePath subclass that can make system calls.

Path represents a filesystem path but unlike PurePath, also offers
methods to do system calls on path objects. Depending on your system,
instantiating a Path will return either a PosixPath or a WindowsPath
object. You can also instantiate a PosixPath or WindowsPath directly,
but cannot instantiate a WindowsPath on a POSIX system or vice versa.

## `get_fips_by_state_code(state_code: str, source: pathlib.Path | None = None) -> str`
Returns the FIPS code for a given 2-letter state code.

Args:
    state_code (str): A 2-letter state abbreviation (e.g., 'MN').
    source (Path | None): Optional override path to a custom CSV file.

Returns:
    str: Corresponding FIPS code (e.g., '27').

Raises:
    ValueError: If the state code is not found.

## `get_state_fips_df(source: pathlib.Path | None = None) -> pandas.core.frame.DataFrame`
Load and return a DataFrame of US state FIPS codes.

Args:
    source (Path | None): Path to a CSV file. If None, uses the default embedded CSV.

Returns:
    pd.DataFrame: A DataFrame with columns ['state_code', 'state_name', 'fips_code'].

## `get_state_name_by_code(state_code: str, source: pathlib.Path | None = None) -> str`
Returns the full state name for a given 2-letter state code.

Args:
    state_code (str): A 2-letter state abbreviation.
    source (Path | None): Optional override path to a custom CSV file.

Returns:
    str: Full state name (e.g., 'Minnesota').

Raises:
    ValueError: If the state code is not found.

## `read_csv_from_path(source: pathlib.Path) -> pandas.core.frame.DataFrame`
Reads a CSV file from the given path and returns a DataFrame.

Args:
    source (Path): Path to the CSV file.

Returns:
    pd.DataFrame: DataFrame containing the CSV data.

# API for `civic_lib_geo.geojson_utils`

## `Any(*args, **kwargs)`
Special type indicating an unconstrained type.

- Any is compatible with every type.
- Any assumed to have all methods.
- All values assumed to be instances of Any.

Note that all the above statements are true from the point of view of
static type checkers. At runtime, Any should not be used with instance
checks.

## `Path(*args, **kwargs)`
PurePath subclass that can make system calls.

Path represents a filesystem path but unlike PurePath, also offers
methods to do system calls on path objects. Depending on your system,
instantiating a Path will return either a PosixPath or a WindowsPath
object. You can also instantiate a PosixPath or WindowsPath directly,
but cannot instantiate a WindowsPath on a POSIX system or vice versa.

## `load_geojson(path: pathlib.Path) -> geopandas.geodataframe.GeoDataFrame`
Load a GeoJSON file into a GeoDataFrame.

Args:
    path (Path): Path to the GeoJSON file.

Returns:
    gpd.GeoDataFrame: A GeoDataFrame with geometries and attributes.

## `read_geojson_props(path: pathlib.Path) -> list[dict[str, typing.Any]]`
Load only the properties from a GeoJSON file.

Args:
    path (Path): Path to the GeoJSON file.

Returns:
    list[dict[str, Any]]: A list of property dictionaries from each feature.

## `save_geojson(gdf: geopandas.geodataframe.GeoDataFrame, path: pathlib.Path, indent: int = 2) -> pathlib.Path`
Save a GeoDataFrame to GeoJSON format.

Args:
    gdf (gpd.GeoDataFrame): The GeoDataFrame to save.
    path (Path): Output file path.
    indent (int): Indentation level for formatting (unused by GeoPandas but included for consistency).

Returns:
    Path: The path to the saved file.

## `simplify_geojson(gdf: geopandas.geodataframe.GeoDataFrame, tolerance: float) -> geopandas.geodataframe.GeoDataFrame`
Return a simplified copy of the GeoDataFrame using the given tolerance.

Args:
    gdf (gpd.GeoDataFrame): The input GeoDataFrame.
    tolerance (float): Tolerance for simplification (smaller values retain more detail).

Returns:
    gpd.GeoDataFrame: A new GeoDataFrame with simplified geometry.

# API for `civic_lib_geo.shapefile_utils`

## `Path(*args, **kwargs)`
PurePath subclass that can make system calls.

Path represents a filesystem path but unlike PurePath, also offers
methods to do system calls on path objects. Depending on your system,
instantiating a Path will return either a PosixPath or a WindowsPath
object. You can also instantiate a PosixPath or WindowsPath directly,
but cannot instantiate a WindowsPath on a POSIX system or vice versa.

## `convert_shapefile_to_geojson(shp_path: pathlib.Path, geojson_path: pathlib.Path) -> pathlib.Path`
Convert a shapefile to a GeoJSON file.

Args:
    shp_path (Path): Path to the source shapefile (.shp).
    geojson_path (Path): Path to the output GeoJSON file.

Returns:
    Path: The path to the saved GeoJSON file.

## `load_shapefile(path: pathlib.Path) -> geopandas.geodataframe.GeoDataFrame`
Load a shapefile into a GeoDataFrame.

Args:
    path (Path): Path to the shapefile (.shp).

Returns:
    gpd.GeoDataFrame: A GeoDataFrame with geometries and attributes.
