# Module `report_utils`

## Classes

### `Path(self, *args, **kwargs)`

PurePath subclass that can make system calls.

Path represents a filesystem path but unlike PurePath, also offers
methods to do system calls on path objects. Depending on your system,
instantiating a Path will return either a PosixPath or a WindowsPath
object. You can also instantiate a PosixPath or WindowsPath directly,
but cannot instantiate a WindowsPath on a POSIX system or vice versa.

## Functions

### `get_agent_name_from_path(path: pathlib.Path) -> str`

Extract and format the agent name from a report file path.

The agent name is derived from the parent folder of the report file,
with underscores replaced by spaces and title-cased.

If the path does not have a parent directory, returns 'Unknown Agent'.

Args:
    path (Path): The path to a report file.

Returns:
    str: Formatted agent name or fallback string.

### `is_report_file(path: pathlib.Path) -> bool`

Determine whether the given file path is a valid report file.

A valid report file must:
- Have a ".json" extension
- Begin with a date prefix (e.g., "2024-01-01")

Args:
    path (Path): The path to check.

Returns:
    bool: True if the path matches report file format, False otherwise.
