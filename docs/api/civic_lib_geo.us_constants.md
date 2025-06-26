# Module `civic_lib_geo.us_constants`

## Functions

### `get_state_dir_name(state_abbr: str) -> str`

Return the standardized directory name for a state (full lowercase name with underscores).

### `get_state_record_by_abbr(abbr: str) -> dict | None`

Return state record by 2-letter abbreviation (e.g., 'MN').

### `get_state_record_by_any(value: str) -> dict | None`

Return state record by abbr, name, or FIPS code (case-insensitive).

### `get_state_record_by_fips(fips: str) -> dict | None`

Return state record by FIPS code (e.g., '27').

### `get_state_record_by_name(name: str) -> dict | None`

Return state record by full name (e.g., 'Minnesota').

### `list_state_choices() -> list[tuple[str, str]]`

Return list of (abbr, name) tuples for all states (for dropdowns/UI).

### `list_state_choices_by_fips() -> list[tuple[str, str]]`

Return list of (FIPS, name) tuples for all states (for dropdowns/UI).
