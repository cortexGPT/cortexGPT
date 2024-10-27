# **Cortex**

## **Overview**

Cortex is a Flask-based web application that serves as the backend for a larger project. The initial setup includes a minimal Flask application, basic routing, and integration with HTML templates. This version (v0.0.0.2) introduces the foundation of the backend and sets up initial routes and templates.

## **Table of Contents**
1. [Features](#features)
2. [Installation](#installation)
3. [Running the Application](#running-the-application)
4. [Testing](#testing)
5. [Contribution Guidelines](#contribution-guidelines)
6. [Known Issues](#known-issues)

---

## **Features**

### **v0.0.0.2 - Flask Application Bootstrapping**
- **Flask Backend**: A minimal Flask app serves the backend and handles HTTP requests.
- **HTML Frontend**: The application renders an HTML template using Jinja2.
- **Routes**:
  - `/`: Renders the homepage with a simple HTML message.
  - `/health`: Returns the server status as JSON (`{"status": "running"}`).
- **Testing**: Unit tests ensure that routes behave correctly.

---

## **Installation**

To get started with Cortex, follow these steps to set up the development environment:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/cortex.git
   cd cortex
   ```

2. **Set Up a Virtual Environment (Optional but Recommended)**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Linux/macOS
   .\venv\Scripts\activate   # On Windows
   ```

3. **Install Dependencies**:
   Install the required dependencies listed in `requirements.txt`:
   ```bash
   pip install -r requirements.txt
   ```

4. **Install Flask** (if not already installed):
   ```bash
   pip install Flask
   ```

---

## **Running the Application**

Once all dependencies are installed, you can run the Flask application locally:

1. **Run the Flask Server**:
   ```bash
   python src/app/app.py
   ```

2. **Access the Application**:
   - Open a browser and go to `http://127.0.0.1:5000` to view the homepage.
   - Go to `http://127.0.0.1:5000/health` to check the server status.

---

## **Testing**

Cortex uses `pytest` for unit testing. Tests are written to validate the behavior of the Flask routes and ensure correct responses. To run the tests:

1. **Install pytest**:
   ```bash
   pip install pytest
   ```

2. **Run the Tests**:
   ```bash
   pytest tests/
   ```

3. **Test Coverage**:
   - Routes like `/` and `/health` are tested for expected output.
   - The application handles both valid and invalid requests, ensuring robustness.

---

## **Contribution Guidelines**

We welcome contributions to Cortex. Please follow these steps when contributing:

1. **Branching Strategy**:
   - Create feature branches using the format `feature/<feature-name>`.
   - Avoid committing directly to `main`.

2. **Code Formatting and Linting**:
   - Use `pylint` for linting and `black` for code formatting.
   - Set up pre-commit hooks to automatically run these tools before committing:
     ```bash
     pre-commit install
     ```

3. **Testing**:
   - Write unit tests for any new features or bug fixes.
   - Ensure tests pass before submitting a pull request.

4. **Pull Requests**:
   - Submit pull requests with a detailed description of changes.
   - Ensure all checks pass before requesting a review.

For more detailed contribution instructions, refer to the **CONTRIBUTING.md**.

---

## **Known Issues**

1. **Cross-Platform Compatibility**:
   - Differences in file handling across operating systems (Windows, Linux, macOS) may cause issues. Be sure to use the correct paths and line endings. The `.gitattributes` file is set up to handle this, but double-check when contributing.

2. **Incomplete Documentation**:
   - The documentation (e.g., troubleshooting) is still being expanded. Please report any gaps you find during onboarding or while working on the project.

3. **Pre-Commit Hook Inconsistencies**:
   - Some users may experience issues with pre-commit hooks not running as expected. Ensure your environment is set up correctly following the instructions in the **CONTRIBUTING.md**.

---