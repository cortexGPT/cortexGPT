# **Cortex v0.0.0.2 - User Manual**

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

Cortex is a locally-hosted chatbot framework designed for sophisticated interactions, natural language understanding (NLU), and task management. In this version, **v0.0.0.2**, the focus is on implementing a basic Flask application, establishing foundational routes, and creating a simple HTML landing page.

---

## **2. System Requirements**

- **Python**: Version 3.8 or higher
- **pip**: Python package installer
- **Flask**: Lightweight web framework (included in `requirements.txt`)
- **Operating Systems Supported**: Windows, macOS, and Linux

---

## **3. Installation Guide**

### **Step 1: Clone the Repository**
Clone the Cortex repository to your local machine:
```bash
git clone https://github.com/cortexGPT/cortexGPT.git
cd cortexGPT
```

### **Step 2: Install Dependencies**
Activate your virtual environment and install the required dependencies:
```bash
pip install -r requirements.txt
```

---

## **4. Basic Usage**

### **Running the Application**

To run the application in this version:

1. **Navigate to the Source Directory**:
   ```bash
   cd src/app
   ```

2. **Run the Application**:
   ```bash
   python app.py
   ```
   - **Access the Application**:
     - **Landing Page**: [http://localhost:5000](http://localhost:5000)
     - **Health Check Endpoint**: [http://localhost:5000/health](http://localhost:5000/health)

### **Project Structure**
Key additions in **v0.0.0.2**:
```plaintext
cortexGPT/
├── /src/app/                # Main Flask application file
├── /templates/              # Contains HTML templates (index.html)
├── /tests/                  # Unit tests for Flask routes
```

---

## **5. Development Workflow**

### **Step 2: Define Routes and HTML Template**
In this version, two routes are defined for basic functionality:
- **Home Route (`/`)**: Returns a simple HTML landing page.
- **Health Route (`/health`)**: Provides JSON output with server status.

### **Commit Guidelines** (New):
- **Feature Additions**: `feat: <description>`
- **Testing**: `test: <description>`
- **Documentation**: `docs: <description>`

---

## **6. Troubleshooting**

### **Issue 1: Flask Route Error**
- **Symptom**: `TemplateNotFound` error when accessing `/`.
- **Solution**: Ensure `index.html` is present in the `/templates` folder.

---

## **7. FAQ**

**Q1: What’s new in v0.0.0.2?**
   - A basic Flask backend and HTML template for the landing page.
