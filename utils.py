# utils.py
import os
from pathlib import Path


def find_project_root(markers=("pyproject.toml", "README.md", ".git"), root_name="data-science"):
    """Find the project root by searching for marker files or root directory name."""
    current = Path.cwd().resolve()
    for directory in [current, *current.parents]:
        if any((directory / marker).exists() for marker in markers) or directory.name == root_name:
            return directory
    return current


def setup_project_root():
    """Change to the project root and return the path."""
    root = find_project_root()
    os.chdir(root)
    return root