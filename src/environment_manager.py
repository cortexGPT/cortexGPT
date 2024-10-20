import subprocess
import os


class EnvironmentManager:
    def __init__(self, requirements_file="requirements.txt"):
        self.requirements_file = requirements_file

    def install_dependencies(self):
        """Install dependencies from the requirements.txt file using the system's pip."""
        if os.path.exists(self.requirements_file):
            subprocess.run(["pip", "install", "-r", self.requirements_file], check=True)
            return True
        else:
            raise FileNotFoundError(f"{self.requirements_file} not found.")
