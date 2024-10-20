# **Contributing to Cortex**

Thank you for your interest in contributing to Cortex! This document outlines the guidelines and best practices for making contributions to ensure that the project remains maintainable and scalable.

---

## **Table of Contents**
1. [How to Contribute](#how-to-contribute)
2. [Branching Strategy](#branching-strategy)
3. [Commit Message Format](#commit-message-format)
4. [Pull Request Guidelines](#pull-request-guidelines)
5. [Code Quality and Formatting](#code-quality-and-formatting)
6. [Testing Guidelines](#testing-guidelines)
7. [Contribution Workflow](#contribution-workflow)
8. [Code of Conduct](#code-of-conduct)

---

## **1. How to Contribute**

There are several ways to contribute to Cortex:

- **Bug Reports**: Submit detailed bug reports to help us improve.
- **Feature Requests**: Suggest new features or enhancements.
- **Code Contributions**: Submit bug fixes, new features, or other improvements.
- **Documentation**: Help improve our project documentation by suggesting updates or clarifications.

### **Fork and Clone the Repository**

1. Fork the repository on GitHub by clicking the "Fork" button at the top right of the repo page.
2. Clone your fork to your local machine:
   ```bash
   git clone https://github.com/<your-username>/cortexGPT.git
   cd cortexGPT
   ```

---

## **2. Branching Strategy**

All contributions must be made in separate feature branches, not directly in the `main` branch. This ensures that multiple features and bug fixes can be developed independently and reviewed in isolation.

- **Naming Convention**: Branch names should follow the pattern `feature/<feature-name>` or `fix/<issue-name>`.
  
  **Examples**:
  - `feature/new-api-endpoint`
  - `fix/documentation-typo`

- **Creating a New Branch**:
  ```bash
  git checkout -b feature/<feature-name>
  ```

---

## **3. Commit Message Format**

All commit messages should follow a standard format to maintain clarity in the project history. We use the format: `type(scope): subject`.

- **Types**:
  - `feat`: New feature
  - `fix`: Bug fix
  - `docs`: Documentation update
  - `style`: Code style or formatting (non-functional changes)
  - `refactor`: Refactoring code
  - `test`: Adding or updating tests
  - `chore`: Maintenance tasks (e.g., build scripts, dependency updates)

- **Scope**: The scope should specify what part of the project the change affects.

- **Example**:
  ```bash
  git commit -m "feat(api): add new authentication endpoint"
  ```

---

## **4. Pull Request Guidelines**

When your feature or bug fix is ready for review, submit a pull request (PR) following these guidelines:

1. **Ensure Your Code is Tested and Linted**:
   - Run all tests using `pytest` to ensure no functionality is broken.
   - Ensure your code passes linting and formatting checks using `pylint` and `black`.
  
2. **Pull Request Format**:
   - Title: Use the same format as a commit message (e.g., `feat(api): add new authentication endpoint`).
   - Description: Provide a detailed description of what the PR does, why it's needed, and any relevant details.

3. **Tagging Reviewers**: Tag the project maintainers for a review.

4. **PR Checklist**:
   - [ ] All tests pass (`pytest`).
   - [ ] Code is linted (`pylint`).
   - [ ] Code is formatted (`black`).

---

## **5. Code Quality and Formatting**

We follow strict coding standards to ensure maintainability and consistency across the codebase.

- **Code Linting**:
  We use `pylint` to enforce code quality standards. Ensure your code passes linting before committing:
  ```bash
  pylint src/
  ```

- **Code Formatting**:
  We use `black` to automatically format code. Run the following command to format your code before committing:
  ```bash
  black src/
  ```

- **Pre-Commit Hooks**:
  Pre-commit hooks are set up to automatically lint and format your code before any commit is made. To ensure these hooks are installed, run:
  ```bash
  pip install pre-commit
  pre-commit install
  ```

---

## **6. Testing Guidelines**

Testing is crucial to maintain the stability of the project. All new features and bug fixes must include tests.

- **Testing Framework**: We use `pytest` for unit and integration testing. Ensure that your feature is accompanied by relevant test cases located in the `/tests` directory.
  
- **Running Tests**:
  Run tests locally before pushing your changes to the repository:
  ```bash
  pytest
  ```

- **Test Coverage**: Aim for at least 80% test coverage for all new code. Make sure to include edge cases and error handling in your tests.

- **Directory Structure for Tests**:
  - All test files should be placed in the `/tests/` directory.
  - Use the naming convention `test_<module>.py`.

---

## **7. Contribution Workflow**

### **Step 1: Fork the Repository**
Fork the Cortex repository to your own GitHub account.

### **Step 2: Clone the Repository**
Clone the forked repository to your local machine:
```bash
git clone https://github.com/<your-username>/cortexGPT.git
```

### **Step 3: Create a New Branch**
Create a branch for your feature or fix:
```bash
git checkout -b feature/<feature-name>
```

### **Step 4: Write Code**
Write your feature or fix, ensuring it follows the coding standards mentioned above.

### **Step 5: Lint, Format, and Test**
Before committing your changes, make sure to:
- Lint your code with `pylint`.
- Format your code with `black`.
- Run all tests using `pytest`.

### **Step 6: Commit and Push**
Commit your changes following the commit message format, and push to your fork:
```bash
git push origin feature/<feature-name>
```

### **Step 7: Submit a Pull Request**
Submit a pull request (PR) to the main repository, following the PR guidelines outlined above.

---

## **8. Code of Conduct**

We are committed to fostering an inclusive and respectful community. Please review our [Code of Conduct](CODE_OF_CONDUCT.md) to ensure a welcoming environment for all contributors.

---

Thank you for contributing to Cortex! Your efforts help make this project better for everyone.
