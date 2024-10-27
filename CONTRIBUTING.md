# **Contributing to Cortex**

We welcome your contributions to Cortex! To help you get started and ensure a smooth development process, please follow these guidelines.

## **Table of Contents**
1. [Development Workflow](#development-workflow)
2. [Branching Strategy](#branching-strategy)
3. [Code Standards](#code-standards)
4. [Testing Guidelines](#testing-guidelines)
5. [Pull Request Process](#pull-request-process)
6. [Setting Up Pre-Commit Hooks](#setting-up-pre-commit-hooks)
7. [Platform-Specific Instructions](#platform-specific-instructions)

---

## **Development Workflow**

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/cortex.git
   cd cortex
   ```

2. **Set Up the Environment**:
   - Ensure Python 3.8+ is installed.
   - Install dependencies from `requirements.txt`:
     ```bash
     pip install -r requirements.txt
     ```

3. **Run the Flask Application**:
   - Start the application locally to verify the setup:
     ```bash
     python src/app/app.py
     ```
   - Open a browser and go to `http://localhost:5000` to see the app running.

4. **Activate Pre-Commit Hooks**:
   - Ensure linting and formatting rules are applied consistently:
     ```bash
     pre-commit install
     ```

5. **Check Out a Feature Branch**:
   - Create a new branch for your work, based on the feature or issue you're addressing:
     ```bash
     git checkout -b feature/<feature-name>
     ```

---

## **Branching Strategy**

We follow the **feature branching** model to ensure clear, organized code contributions. Here are the main branch types:
- **Feature Branch**: `feature/<feature-name>` for new features or enhancements.
- **Hotfix Branch**: `hotfix/<bug-description>` for urgent bug fixes.
- **Release Branch**: `release/<version-number>` for release preparation.

Always base new branches on the latest `main` branch.

---

## **Code Standards**

We enforce strict adherence to code standards for maintainability and readability:

1. **Naming Conventions**:
   - **Variables** and **functions**: Use `snake_case`.
   - **Classes**: Use `PascalCase`.
   - **File Names**: Keep file names concise and use `snake_case`.

2. **PEP 8 Compliance**:
   - Ensure Python code follows PEP 8 standards using `pylint`.
   - Use `black` for automatic code formatting.

3. **Separation of Concerns**:
   - Separate Flask routes and business logic.
   - Keep templates and static files organized in appropriate directories (`/templates`, `/static`).

---

## **Testing Guidelines**

All code contributions must include relevant unit or integration tests to ensure code quality and prevent regression.

### **Unit Tests**:
- Place all unit tests in the `/tests` directory.
- Use `pytest` as the testing framework.

### **Example Tests**:
Here’s how to write a simple unit test for a route:

```python
def test_home_route(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b"Hello, Cortex!" in response.data
```

### **Running Tests**:
- Run all tests using:
  ```bash
  pytest tests/
  ```

- Ensure test coverage is maintained at or above **80%**. Use coverage reports to monitor the coverage:
  ```bash
  pytest --cov=src
  ```

---

## **Pull Request Process**

To contribute your work:

1. **Open a Pull Request**:
   - Once your feature is complete, open a PR to merge it into `main`.
   - Ensure the PR description is clear and includes links to any related issues or tasks.

2. **Write Meaningful Commit Messages**:
   - Format commits using `type: description`. Example:
     ```bash
     git commit -m "feat: add health check route"
     ```

3. **Pass All Checks**:
   - Your PR must pass linting, formatting, and testing checks before it can be merged.

4. **Complete the PR Template**:
   - Include all required details (e.g., what was changed, how to test the changes, related issue numbers).

---

## **Setting Up Pre-Commit Hooks**

Pre-commit hooks are set up to enforce consistent linting and formatting before any changes are committed.

### **Installing Pre-Commit Hooks**:
1. Install `pre-commit`:
   ```bash
   pip install pre-commit
   ```
2. Activate the hooks:
   ```bash
   pre-commit install
   ```

3. To run the hooks manually on all files:
   ```bash
   pre-commit run --all-files
   ```

---

## **Platform-Specific Instructions**

**Cross-Platform Setup**: We support development across Windows, macOS, and Linux. Here are platform-specific considerations:

1. **Line Endings**:
   - Ensure consistent line endings using the `.gitattributes` file.
   - Windows users should configure their Git settings to avoid CRLF issues.

2. **Running Flask**:
   - Ensure that environment-specific configurations, such as ports or file paths, are set correctly in your setup.

3. **Browser Testing**:
   - Test your changes across multiple browsers to ensure cross-browser compatibility.

---

## **Further Documentation**

- Refer to the [README.md](README.md) for project setup instructions.
