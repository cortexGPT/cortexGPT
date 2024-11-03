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

Cortex is a locally-hosted chatbot framework designed for sophisticated interactions, natural language understanding (NLU), and task management. Cortex now features a **basic HTML User Interface** that allows users to interact directly with the backend. The UI provides a simple form where users can input their queries, submit them to the backend, and receive a response—all from their web browser.

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

1. **Run the Application**:
   ```bash
   python src/app/app.py
   ```

---

## **5. UI Functionality**
### Using the HTML User Interface

1. **Accessing the Interface**:
   - Open your browser and navigate to **http://127.0.0.1:5000/**.
   - The page will display a simple form labeled **"Enter Input:"**.

2. **Submitting a Form**:
   - Enter your query or message in the input box.
   - Click the **Submit** button to send the data to the backend.
   - Once submitted, the server processes your input and returns a response that will be displayed on the page.

3. **Form Validation**:
   - If the input field is empty, JavaScript will prevent the form from being submitted and show an alert saying, **"Input is required!"**.

4. **Example Scenario**:
   - Enter "Hello World" and click submit.
   - You should receive a response: **"Received: Hello World"**.

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

## **6. Troubleshooting and FAQ**

**Q1: The server is not starting or cannot be accessed at http://127.0.0.1:5000/**  
- **Solution**: Ensure the virtual environment is activated before running the server.
- Check if another application is using port **5000** and stop it or use a different port by running:
  ```sh
  python src/app/app.py --port 5001

**Q2: Form submission is not working, and nothing happens when I click Submit**
- **Solution:** Make sure JavaScript is enabled in your browser. Also, ensure you are entering text in the input box before clicking Submit.

**Q3: I see "Input is required!" even after entering text**
- **Solution:** This might be a cross-browser compatibility issue. Try using Chrome or Firefox. Ensure that the latest version of JavaScript is enabled.

**Q4: Changes to index.html or script.js are not reflected**
- **Solution:** Clear your browser cache or use Ctrl + F5 to force-refresh the page.

**Q5: How do I stop the server?**
- **Solution:** Use Ctrl + C in the terminal where the server is running to shut it down.
