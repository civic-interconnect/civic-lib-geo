# Module `civic_lib_geo.fips_utils`

## Classes

### `Path(self, *args, **kwargs)`

PurePath subclass that can make system calls.

Path represents a filesystem path but unlike PurePath, also offers
methods to do system calls on path objects. Depending on your system,
instantiating a Path will return either a PosixPath or a WindowsPath
object. You can also instantiate a PosixPath or WindowsPath directly,
but cannot instantiate a WindowsPath on a POSIX system or vice versa.

## Functions

### `get_fips_by_state_code(state_code: str, source: pathlib.Path | None = None) -> str`

Returns the FIPS code for a given 2-letter state code.

Args:
    state_code (str): A 2-letter state abbreviation (e.g., 'MN').
    source (Path | None): Optional override path to a custom CSV file.

Returns:
    str: Corresponding FIPS code (e.g., '27').

Raises:
    ValueError: If the state code is not found.

### `get_state_fips_df(source: pathlib.Path | None = None) -> pandas.core.frame.DataFrame`

Load and return a DataFrame of US state FIPS codes.

Args:
    source (Path | None): Path to a CSV file. If None, uses the default embedded CSV.

Returns:
    pd.DataFrame: A DataFrame with columns ['state_code', 'state_name', 'fips_code'].

### `get_state_name_by_code(state_code: str, source: pathlib.Path | None = None) -> str`

Returns the full state name for a given 2-letter state code.

Args:
    state_code (str): A 2-letter state abbreviation.
    source (Path | None): Optional override path to a custom CSV file.

Returns:
    str: Full state name (e.g., 'Minnesota').

Raises:
    ValueError: If the state code is not found.

### `read_csv_from_path(source: pathlib.Path) -> pandas.core.frame.DataFrame`

Reads a CSV file from the given path and returns a DataFrame.

Args:
    source (Path): Path to the CSV file.

Returns:
    pd.DataFrame: DataFrame containing the CSV data.
