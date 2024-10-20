"""
Test suite for the EnvironmentManager class and project structure validation.

This module includes unit tests for:
- Installing dependencies from requirements.txt.
- Verifying the project's directory structure.
- Ensuring the .gitignore file excludes specific files and directories.
"""

import os
from src.environment_manager import EnvironmentManager


def test_dependency_installation():
    """
    Test that dependencies are installed correctly using the EnvironmentManager.
    """
    env_manager = EnvironmentManager(requirements_file="requirements.txt")
    assert env_manager.install_dependencies()


def test_directory_structure():
    """
    Test that the project directory structure matches the expected layout.
    """
    expected_structure = ["src", "tests", "docs", "requirements.txt"]
    actual_structure = os.listdir(".")
    assert all(item in actual_structure for item in expected_structure)


def test_gitignore_exclusion():
    """
    Test that the .gitignore file contains the expected excluded directories and files.
    """
    with open(".gitignore", encoding="utf-8") as f:
        ignored_files = f.read().splitlines()
    assert "venv/" in ignored_files
