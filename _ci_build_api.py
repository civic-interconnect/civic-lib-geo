"""
_ci_build_api.py - Generate simple API documentation for public functions and classes.

- Scans the main package directory for public functions/classes.
- Documents their signatures and docstrings.
- Warns if any public object is missing a docstring.
- Writes the output to meta/api.md.

Intended for use in Civic Interconnect libraries.
"""

import contextlib
import importlib
import inspect
from pathlib import Path


def find_modules(package_dir: Path, package_name: str):
    """Yield all importable Python modules in a package."""
    for py_file in package_dir.rglob("*.py"):
        if "__init__" in py_file.name or py_file.name.startswith("_"):
            continue
        rel_path = py_file.relative_to(package_dir.parent).with_suffix("")
        module_name = ".".join(rel_path.parts)
        if module_name.startswith(package_name):
            yield module_name


def generate_api_doc(module_name: str):
    """Generate API documentation for a given module."""
    lines = [f"# API for `{module_name}`\n"]
    try:
        mod = importlib.import_module(module_name)
    except Exception as e:
        return [f"ERROR: Failed to import `{module_name}`: {e}\n"]

    for name, obj in inspect.getmembers(mod):
        if name.startswith("_"):
            continue
        if inspect.isfunction(obj) or inspect.isclass(obj):
            sig = ""
            with contextlib.suppress(Exception):
                sig = str(inspect.signature(obj))
            lines.append(f"## `{name}{sig}`")
            doc = inspect.getdoc(obj)
            if doc:
                lines.append(doc)
            else:
                lines.append("WARNING: Missing docstring._")
            lines.append("")  # Blank line
    return lines


def main():
    print("Starting to Generate API documentation...")

    repo_root_dir = Path(__file__).resolve().parent
    print(f"Repository root directory: {repo_root_dir}")
    if not repo_root_dir.exists():
        raise RuntimeError(f"Repository root directory not found: {repo_root_dir}")

    repo_src_dir = repo_root_dir / "src"
    print(f"Source directory: {repo_src_dir}")
    if not repo_src_dir.exists():
        raise RuntimeError(f"Source directory not found: {repo_src_dir}")

    # Detect the package folder in src (assumes exactly one top-level folder starting with civic_)
    repo_package_dir = next(
        (p for p in repo_src_dir.iterdir() if p.is_dir() and p.name.startswith("civic_")), None
    )

    if repo_package_dir is None:
        raise RuntimeError("Could not find top-level package folder starting with 'civic_'.")

    pkg_name = repo_package_dir.name
    output_path = repo_root_dir / "REF_API.md"

    package_dir = repo_src_dir / pkg_name
    if not package_dir.exists():
        print(f"ERROR: Package directory not found: {pkg_name}")
        return

    all_lines = ["# Civic Interconnect API Documentation\n"]
    for mod in sorted(find_modules(package_dir, pkg_name)):
        print(f"Processing module: {mod}")
        all_lines += generate_api_doc(mod)

    output_path.parent.mkdir(exist_ok=True)
    output_path.write_text("\n".join(all_lines), encoding="utf-8")
    print(f"API documentation written to {output_path}")


if __name__ == "__main__":
    main()
