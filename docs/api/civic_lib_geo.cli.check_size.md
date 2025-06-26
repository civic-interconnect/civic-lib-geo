# Module `civic_lib_geo.cli.check_size`

## Classes

### `Path(self, *args, **kwargs)`

PurePath subclass that can make system calls.

Path represents a filesystem path but unlike PurePath, also offers
methods to do system calls on path objects. Depending on your system,
instantiating a Path will return either a PosixPath or a WindowsPath
object. You can also instantiate a PosixPath or WindowsPath directly,
but cannot instantiate a WindowsPath on a POSIX system or vice versa.

## Functions

### `get_file_size_mb(path: str | pathlib.Path) -> float`

Return the file size in megabytes (MB).

Args:
    path: Path to the file.

Returns:
    File size in megabytes.

Raises:
    FileNotFoundError: If the file does not exist.

### `main(path: pathlib.Path) -> int`

Print the size of a GeoJSON file and whether it exceeds GitHub Pages limits.

Args:
    path (Path): Path to the GeoJSON file to inspect.

Returns:
    int: 0 if OK, 1 if an error occurs.

### `needs_chunking(path: str | pathlib.Path, max_mb: float = 25.0) -> bool`

Determine whether the GeoJSON file exceeds the size threshold.

Args:
    path: Path to the file.
    max_mb: Maximum file size before chunking is recommended.

Returns:
    True if file exceeds max_mb, else False.
