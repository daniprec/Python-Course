Param()

$repoRoot = (Get-Location).Path
Write-Host "Setting git core.hooksPath to .githooks (repo root: $repoRoot)"
git config core.hooksPath .githooks

if (Test-Path -Path ".githooks/pre-commit") {
    Write-Host "Making sure .githooks/pre-commit is executable (for msys/git)"
    git update-index --add --chmod=+x .githooks/pre-commit 2>$null
}

Write-Host "Installing Python dependency nbformat (user)"
python -m pip install --user nbformat

Write-Host "Done. Pre-commit hook will run tools/sync_execute_flags.py on commit."
Write-Host "If you use a different python binary in CI, ensure that environment has nbformat installed."
