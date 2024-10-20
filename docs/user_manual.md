# **Cortex v0.0.0.1 - User Manual**

---

## **Table of Contents**
1. [Introduction](#introduction)
2. [System Requirements](#system-requirements)
3. [Installation Guide](#installation-guide)
4. [Basic Usage](#basic-usage)
5. [Development Workflow](#development-workflow)
6. [Troubleshooting](#troubleshooting)
7. [FAQ](#faq)

---

## **1. Introduction**

Cortex is a locally-hosted chatbot framework designed for sophisticated interactions, natural language understanding (NLU), and task management. In this initial version, **v0.0.0.1**, the focus is on setting up the development environment, managing dependencies, and creating the project structure.

This manual guides users through the process of setting up Cortex, running the system, and troubleshooting common issues.

---

## **2. System Requirements**

Before setting up Cortex, ensure that your system meets the following requirements:

- **Python**: Version 3.8 or higher
- **pip**: Python package installer
- **Git**: For version control
- **Operating Systems Supported**: Windows, macOS, and Linux

---

## **3. Installation Guide**

### **Step 1: Clone the Repository**
Clone the Cortex repository to your local machine:
```bash
git clone https://github.com/cortexGPT/cortexGPT.git
cd cortexGPT
```

### **Step 2: Set Up Virtual Environment**
Create and activate a virtual environment to manage dependencies. The virtual environment ensures that all necessary packages are installed in an isolated environment, avoiding conflicts with system packages.

#### **For Unix-based systems (macOS, Linux):**
```bash
python3 -m venv venv
source venv/bin/activate
```

#### **For Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

### **Step 3: Install Dependencies**
Install the required dependencies by running:
```bash
pip install -r requirements.txt
```

### **Step 4: Run Unit Tests**
Verify the installation by running the pre-configured unit tests:
```bash
pytest
```

If all tests pass, your installation is complete.

---

## **4. Basic Usage**

### **Running the Application**
Currently, **v0.0.0.1** focuses on project setup and environment configuration. To interact with the system:

1. **Activate the Virtual Environment**:
   - On Unix-based systems:
     ```bash
     source venv/bin/activate
     ```
   - On Windows:
     ```bash
     venv\Scripts\activate
     ```

2. **Run Unit Tests**:
   ```bash
   pytest
   ```
   This will ensure your environment is properly set up.

### **Project Structure**
The project is organized as follows:
```plaintext
cortex_project/
├── src/          # Core logic and source code
├── tests/        # Unit tests for the project
├── docs/         # Project documentation
└── requirements.txt  # Dependency tracker
```

### **Basic Commands**
- **Activate virtual environment**:
  ```bash
  source venv/bin/activate  # Unix
  venv\Scripts\activate  # Windows
  ```

- **Deactivate virtual environment**:
  ```bash
  deactivate
  ```

- **Run linter**:
  ```bash
  pylint src/
  ```

- **Run formatter**:
  ```bash
  black src/
  ```

---

## **5. Development Workflow**

### **Step 1: Creating a New Feature**
1. Create a feature branch:
   ```bash
   git checkout -b feature/<feature_name>
   ```

2. Implement your changes.

### **Step 2: Lint and Format Your Code**
Before committing your changes, ensure your code meets quality standards:
```bash
pylint src/
black src/
```

### **Step 3: Run Tests**
Always run the tests before submitting a pull request:
```bash
pytest
```

### **Step 4: Submit a Pull Request**
Push your changes and submit a pull request following the project’s contribution guidelines.

---

## **6. Troubleshooting**

### **Issue 1: Virtual Environment Activation Fails**
- **Symptom**: You cannot activate the virtual environment on Windows or Unix.
- **Solution**: Ensure that you’re using the correct activation command for your operating system. If permission errors occur on Unix-based systems, check that your `venv/bin/activate` script has the correct permissions:
  ```bash
  chmod +x venv/bin/activate
  ```

### **Issue 2: Dependency Installation Errors**
- **Symptom**: `pip install -r requirements.txt` fails to install dependencies.
- **Solution**: Ensure you are using Python 3.8 or higher. If issues persist, check for any version conflicts in `requirements.txt`.

### **Issue 3: Linter or Formatter Not Working**
- **Symptom**: Pre-commit hooks for `pylint` or `black` are not working as expected.
- **Solution**: Ensure that `pre-commit` is installed:
  ```bash
  pip install pre-commit
  pre-commit install
  ```

### **Issue 4: Tests Failing**
- **Symptom**: Tests fail after running `pytest`.
- **Solution**: Review the test results and ensure your environment is properly set up. Verify that you followed all steps in the setup process.

### **Cross-Platform Issues**
Ensure you're using the correct commands for your operating system:
- **Windows**: Use backslashes (`\`) for paths.
- **Unix-based systems**: Use forward slashes (`/`).

---

## **7. FAQ**

### **Q1: Do I need a virtual environment?**
Yes, a virtual environment is recommended to isolate project dependencies and avoid conflicts with system-wide packages.

### **Q2: How do I deactivate the virtual environment?**
Simply run:
```bash
deactivate
```

### **Q3: What should I do if `pytest` fails?**
Check the error message provided by `pytest`. Ensure you have followed the setup instructions properly. Also, confirm that all required libraries are installed.

### **Q4: How can I contribute to the project?**
To contribute, follow the branching strategy outlined in the contribution guidelines:
1. Fork the repository.
2. Create a new branch (`feature/<feature_name>`).
3. Make your changes.
4. Submit a pull request for review.

---
