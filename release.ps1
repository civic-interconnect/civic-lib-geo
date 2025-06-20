param (
    [Parameter(Mandatory=$true)]
    [string]$Version  # Example: "v0.1.0"
)

$Stripped = $Version.TrimStart("v")

Write-Host "Bumping version to $Version..."

# Update version in all files
python bump_version.py (Get-Content VERSION -Raw).Trim() $Stripped

# Optional: update pre-commit hooks
pre-commit autoupdate --repo https://github.com/pre-commit/pre-commit-hooks

# Clean build
if (Test-Path build) { Remove-Item -Recurse -Force build }

# Reinstall package in editable mode
pip uninstall civic-lib-geo -y
pip install -e .

# Lint and test
ruff check . --fix || exit $LASTEXITCODE
pytest || exit $LASTEXITCODE

# Git commit and tag
git add .
git commit -m "Release: v$Version"
git push origin main

git tag v$Version
git push origin v$Version

Write-Host "`nRelease v$Version completed successfully."
