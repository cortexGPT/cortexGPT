import os

from src.environment_manager import EnvironmentManager


def test_dependency_installation():
    env_manager = EnvironmentManager(requirements_file="requirements.txt")
    assert env_manager.install_dependencies() == True


def test_directory_structure():
    expected_structure = ["src", "tests", "docs", "requirements.txt"]
    actual_structure = os.listdir(".")
    assert all(item in actual_structure for item in expected_structure)


def test_gitignore_exclusion():
    with open(".gitignore") as f:
        ignored_files = f.read().splitlines()
    assert "venv/" in ignored_files
