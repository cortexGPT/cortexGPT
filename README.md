# **Cortex**

## **Overview**

Cortex is a locally-hosted chatbot application designed to deliver an advanced, private AI experience. With the addition of **revision v0.0.0.3**, a basic **HTML User Interface (UI)** has been introduced, enabling users to interact with the backend through a simple web form.

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
   This project uses the following dependencies:

   - Flask: Handles the web server.
   - Pytest: For running unit and integration tests.
   - Markupsafe: For sanitizing user inputs to prevent vulnerabilities like XSS.
   - JavaScript and CSS: Used for frontend interaction and styling.

   Install the dependencies using the following command:
   ```sh
   pip install -r requirements.txt

---

### Setting Up the Project

1. **Clone the Repository**:
   ```sh
   git clone https://github.com/your-repository/cortex
   cd cortex

2. **Set Up Virtual Environment**:
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate

3. **Install Requirements**:
   pip install -r requirements.txt

4. Running the Application: Start the Flask server to view the HTML User Interface:
   python src/app/app.py

5. Open your browser and navigate to http://127.0.0.1:5000/ to view and use the form interface.

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

### **Run the Tests**:
Revision v0.0.0.3 introduces a **basic HTML UI**. Testing has been expanded to cover both backend routes and the new UI functionality:

1. **Unit Tests**:
   - Flask routes are tested using **pytest**.
   - Tests can be found in `/tests/test_routes.py`.
   - Run tests using:
     ```sh
     pytest tests/
     ```

2. **Integration Tests**:
   - Test the integration between the UI and backend, ensuring that form submissions are properly handled.
   - Use the test client to simulate form submissions.

3. **Cross-Browser Testing**:
   - Ensure that the HTML UI works properly across major browsers like Chrome, Firefox, and Safari.
   - Manual testing should include verifying interactions such as button clicks, form submission, and validation.

4. **Accessibility Testing**:
   - Tools like **WAVE** or **Lighthouse** are recommended to audit the accessibility of the HTML page.
   - Ensure that all input elements have ARIA labels and that the page is navigable using only a keyboard.


---
### New Features and Functionalities in v0.0.0.3

**Basic HTML User Interface**:
- A minimal HTML page (`index.html`) has been added in `/src/app/templates/`. It contains a form that users can fill out and submit to interact with the backend.

**CSS Styling for Basic Responsiveness**:
- **File Location**: `/src/static/style.css`.
- Provides basic styling to make the form visually appealing and responsive across devices.

**JavaScript for Form Interactivity**:
- **File Location**: `/src/static/script.js`.
- JavaScript has been added to enhance the user experience with features like form validation to ensure inputs are not empty before submission.

Example:
```javascript
document.querySelector('form').addEventListener('submit', function(event) {
    const input = document.querySelector('#userInput').value;
    if (!input) {
        alert('Input is required!');
        event.preventDefault();
    }
});

---

## **Contribution Guidelines**

We welcome contributions to Cortex. Please follow these steps when contributing:

1. **Branching Strategy**:
   - Follow the `feature/<feature_name>` naming convention for branches.

2. **Code Formatting and Linting**:
   - Use **pylint** and **black** for Python code.
   - JavaScript should be linted with **ESLint**.

3. **Testing**:
   - Write unit tests for any new features or bug fixes.
   - Ensure tests pass before submitting a pull request.

4. **Pull Requests**:
   - Submit pull requests with a detailed description of changes.
   - Ensure all checks pass before requesting a review.

For more detailed contribution instructions, refer to the **CONTRIBUTING.md**.

---

## **Known Issues**

- **JavaScript Inconsistencies**:
  JavaScript validation has shown inconsistencies across different browsers, especially in Safari. Consider adding **try-catch** blocks and using feature detection to mitigate these issues.

- **Platform-Specific Path Handling**:
  Differences in file paths between operating systems (e.g., Windows vs. Linux/macOS) might cause issues. Ensure you follow the platform-specific instructions in the setup steps.

- **Accessibility Gaps**:
  Conduct a thorough audit of form labels and ARIA attributes using tools like **WAVE** to ensure all input elements are accessible.

---