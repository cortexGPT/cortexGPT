"""
This module provides the EnvironmentManager class, which is responsible
for managing the installation of dependencies for the Cortex project.
"""

import subprocess
import os


class EnvironmentManager:
    """
    Manages the installation of dependencies using the system's pip.

    Attributes:
        requirements_file (str): The path to the requirements.txt file.
    """

    def __init__(self, requirements_file="requirements.txt"):
        """
        Initializes the EnvironmentManager with the specified requirements file.

        Args:
            requirements_file (str): The path to the requirements.txt file.
        """
        self.requirements_file = requirements_file

    def install_dependencies(self):
        """
        Installs dependencies from the requirements.txt file using pip.

        Raises:
            FileNotFoundError: If the requirements.txt file is not found.
        """
        if os.path.exists(self.requirements_file):
            subprocess.run(["pip", "install", "-r", self.requirements_file], check=True)
            return True
        raise FileNotFoundError(f"{self.requirements_file} not found.")
