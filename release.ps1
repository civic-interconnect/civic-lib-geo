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
pip uninstall civic-lib -y
pip install -e .

# Lint and test
ruff check . --fix
pytest

# Git commit and tag
git add .
git commit -m "Release: civic-lib $Version"
git push origin main

git tag $Version
git push origin $Version

Write-Host "`nRelease $Version completed successfully."
