Here is an integrated **CHANGELOG** for **Cortex** that incorporates the changes from **v0.0.0.2** into the existing log:

## **CHANGELOG**

### **v0.0.0.2 - Flask Application Bootstrapping**
#### **Date**: 2024-10-25

---

### **New Features**
1. **Basic Flask Application Structure**:
   - Set up a minimal Flask application serving as the backend.
   - Created the basic folder structure, including `/src/app/` and `/templates/`.
   - Commit: `feat: setup basic Flask application structure`.

2. **Initial Routes Defined**:
   - Two routes were implemented:
     - `/` route serves the `index.html` template.
     - `/health` route returns a JSON response (`{"status": "running"}`).
   - Commit: `feat: define initial routes for home and health check`.

3. **HTML Template Integration**:
   - Integrated a basic HTML template (`index.html`) that renders a landing page with the message "Hello, Cortex!".
   - Template located in `/src/app/templates/index.html`.
   - Commit: `feat: integrate basic HTML template`.

4. **Local Deployment Tested**:
   - Tested local deployment, confirming that the Flask app responds correctly at `http://localhost:5000/`.
   - The `/` route loads the template, and the `/health` route provides the JSON response.
   - Commit: `test: verify local deployment of Flask application`.

5. **Unit Tests Added**:
   - Added unit tests for validating the `/` and `/health` routes.
   - Tests are located in `/tests/test_routes.py`.
   - Commit: `test: add unit tests for home and health routes`.

---

### **Fixes**
1. **Resolved Duplicate `home()` Function**:
   - Removed the redundant `home()` function in `app.py` that caused issues during testing.
   - Commit: `fix: remove duplicate home function in app.py`.

2. **Cross-Platform Compatibility Improvements**:
   - Added a `.gitattributes` file to ensure consistent line endings (CRLF vs. LF) across operating systems.
   - Commit: `chore: add .gitattributes for cross-platform consistency`.

---

### **Known Issues**
1. **Pre-Commit Hook Enforcement**:
   - Pre-commit hooks for `pylint` and `black` may not be running consistently across all environments, causing inconsistent linting and formatting.
   - **Status**: **Partially Resolved** (Issue 2).
   - **Proposed Solution**: Update documentation with setup instructions for pre-commit hooks across platforms.

2. **Documentation Gaps**:
   - Some areas of the documentation (contribution guidelines, troubleshooting) are incomplete or unclear for new contributors.
   - **Status**: **Partially Resolved** (Issue 5).
   - **Proposed Solution**: Expand documentation to include more information on testing, setup, and troubleshooting.

3. **Platform-Specific Path Handling**:
   - Differences in file paths between Windows and Linux/macOS are causing challenges in running scripts.
   - **Status**: **Open** (Issue 12).
   - **Proposed Solution**: Continue documenting platform-specific path handling instructions and update any related configurations.

---

### **v0.0.0.1 - Initial Project Setup and Environment Configuration**

#### **Date**: 2024-10-20

---

### **New Features**
1. **Project Setup**:
   - Installed Python 3.8+ and required libraries (`Flask`, `pytest`).
   - Created a `requirements.txt` file to manage project dependencies.
   - Initialized a virtual environment (later removed) for development consistency across platforms.
   - Ensured system-wide `pip` usage after removing virtual environment logic to simplify development.

2. **Directory Structure**:
   - Created a modular project directory structure with separate folders for source code (`/src`), tests (`/tests`), and documentation (`/docs`).
   - The structure is designed to support future scaling with clear separation of concerns.

3. **Git Repository**:
   - Initialized a Git repository with version control for all project files.
   - Configured `.gitignore` to exclude virtual environment folders, logs, and other unnecessary files from version control.

4. **Pre-Commit Hooks**:
   - Installed `pylint` for linting and `black` for automatic code formatting.
   - Set up pre-commit hooks to enforce code quality standards before committing any changes.

5. **Basic Unit Testing**:
   - Configured `pytest` for running unit tests.
   - Added initial unit tests to validate the setup and configuration of the environment, including testing the installation of dependencies via `pip`.

---

### **Fixes**
1. **Cross-Platform Compatibility**:
   - Addressed differences between Unix and Windows environments for file paths, particularly for dependency installation (`pip` path handling).
   - Updated the `EnvironmentManager` to remove virtual environment logic and focus on using system-wide `pip` for simplicity.

2. **Dependency Management**:
   - Ensured that `requirements.txt` was up-to-date with all required libraries, fixing inconsistent dependency installations reported during testing.
   - Resolved platform-specific issues, such as line-ending mismatches, by configuring `.gitattributes` for cross-platform compatibility.

---

### **Deprecations**
1. **Virtual Environment Logic**:
   - Removed the need for managing a virtual environment as the setup was simplified to use the system’s `pip` for dependency management. This change was made to streamline the development process.

---

### **Known Issues**
1. **Pre-Commit Hook Inconsistencies**:
   - Some developers reported that pre-commit hooks for `pylint` and `black` were not running consistently across environments. This is likely due to local Git configuration differences.
   - **Status**: In Progress. Detailed installation and troubleshooting instructions were added to the `README.md`.

2. **Git Branching Strategy**:
   - Team members occasionally deviated from the specified branching strategy (`feature/<feature_name>`), leading to some confusion during code reviews.
   - **Status**: Open. The issue has been addressed with clear examples added to the `README.md`.

3. **Platform-Specific Configuration Issues**:
   - Line-ending differences (CRLF vs. LF) and file permission issues were reported by some team members working on different platforms (Windows, macOS, Linux).
   - **Status**: In Progress. A `.gitattributes` file was added to handle line-ending differences, and platform-specific setup instructions were added to the documentation.

4. **Low Test Coverage**:
   - Initial test coverage is low, covering only the basic environment setup and dependency installation.
   - **Status**: Open. Additional tests will be added in future revisions to increase coverage to at least 80%.

---

### **Improvements**
1. **README Documentation**:
   - The `README.md` file was expanded to include detailed installation instructions, project structure explanations, and usage notes for contributors.
   - Added pre-commit installation, testing commands, and coding standards to streamline the onboarding process for new developers.
   - A troubleshooting section was added to address common issues encountered during the setup phase.

---
