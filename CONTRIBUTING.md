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

- Follow the `feature/<feature_name>` naming convention for all feature development.
- Create separate branches for bug fixes (`bugfix/<issue_description>`) and documentation updates (`docs/<update_description>`).


Always base new branches on the latest `main` branch.

---

## **Code Standards**

- **Python**: Use `pylint` and `black` to enforce linting and formatting. Ensure `black` is run before submitting any pull requests to maintain consistency.
- **JavaScript**: Use `ESLint` for JavaScript linting. Ensure code follows the modular approach described in the `Design Document` to maintain readability and reusability.
- **HTML & CSS**: Use semantic HTML5 tags and descriptive class names (`kebab-case`). All form inputs must include ARIA labels to enhance accessibility.

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
   - Use the following commit message format:
   - `feat:` for new features.
   - `fix:` for bug fixes.
   - `style:` for formatting, CSS, and appearance changes.
   - `test:` for adding or modifying tests.
   - `docs:` for documentation updates.
   - Example: `feat: add JavaScript form validation for input field`.

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
