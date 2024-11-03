# **Technical Documentation for Cortex**

## **Overview**

This document provides a technical overview of Cortex, including architectural details, module descriptions, endpoint specifications, error handling, and dependencies. Cortex is an advanced, locally-hosted chatbot designed to provide a rich offline user experience. As of **revision v0.0.0.3**, a basic **HTML User Interface (UI)** has been implemented to allow users to interact with the chatbot via a simple form.

---

## **Architecture**

### **System Architecture**

**Frontend (HTML, CSS, JavaScript)**:
- **HTML**: Located in `/src/app/templates/`, this component serves as the user interface for interacting with the backend.
- **CSS**: The style sheet (`style.css`) is located in `/src/static/` and ensures the form is responsive and visually appealing.
- **JavaScript**: Enhances interactivity by providing client-side validation (`script.js` in `/src/static/`).

**Backend (Flask)**:
- **Flask Application**: Located in `/src/app/app.py`, responsible for routing requests from the HTML frontend and providing appropriate responses.
- **Interaction Flow**:
  - **User Request**: A form submission from the HTML page is sent to the `/submit` route.
  - **Backend Processing**: Flask handles the request, sanitizes the input, and returns a response.
  - **Response Flow**: The response is rendered back on the page for the user to see.

The interaction between the frontend and backend follows a traditional request-response model using HTTP POST.


### **File Structure**
The Cortex file structure follows best practices for separation of concerns:
```plaintext
cortexGPT/
├── /docs/                        # Documentation files, including API and technical details
│   ├── api_specifications.md     # API details for each endpoint
│   ├── technical_documentation.md # This file, covering system architecture and modules
│   └── user_manual.md            # User guide with setup and usage instructions
├── /src/
│   ├── /app/
│   │   └── app.py                # Main Flask application file with route definitions
│   ├── /templates/
│   │   └── index.html            # HTML template for the landing page
├── /tests/                       # Unit and integration tests
│   ├── test_environment.py       # Test to validate environment setup
│   └── test_routes.py            # Tests for route functionality
├── .pre-commit-config.yaml       # Configurations for pre-commit linting and formatting
├── CHANGELOG.md                  # Records changes for each release version
└── README.md                     # Setup and contribution instructions
```

---

## **Modules and Components**

**Frontend Modules**:
- **`/src/app/templates/index.html`**: The HTML page that serves as the main UI. Contains a form for submitting user input.
- **`/src/static/style.css`**: Provides basic styling, ensuring consistency across different devices.
- **`/src/static/script.js`**: Implements JavaScript to validate form inputs before submission.

**Backend Modules**:
- **`/src/app/app.py`**: Flask application that processes form submissions and routes them to appropriate backend logic.

---

## **Flow Diagrams**

### **Application Request Flow**

```plaintext
[User Interaction]
       |
       v
[Flask Server]
       |
       v
  [Route Handler]
       |
       +--> [Template Rendering (home route)]
       |         |
       |         v
       |    Rendered HTML Page
       |
       +--> [JSON Response (health_check)]
       |
       v
 [User Feedback]
```

### **File and Module Interaction Flow**
- **Flask App** -> `render_template()` -> **HTML Template (`index.html`)**
- **Flask App** -> `jsonify()` -> **JSON Response (`{"status": "running"}`)**
- **Unit Tests** -> Flask Endpoints -> **Routes (`/`, `/health`)**

---

## **Third-Party Dependencies**

1. **Flask**: Provides the backend infrastructure to handle new form routes (`/submit`).
2. **Jinja2**: Template engine integrated with Flask to render dynamic HTML content.
3. **Markupsafe**: Used to sanitize user inputs on the backend to prevent XSS.
4. **pytest**: Testing framework for writing unit and integration tests.

---

### HTML User Interface (UI) Details

**Form Integration**:
- The new form in `index.html` allows users to input data, which is then submitted to the backend using a POST request.
- **Client-Side JavaScript** ensures that empty input fields are not submitted, providing real-time validation to improve user experience.

**CSS Styling**:
- The `style.css` file makes the form responsive and visually consistent across different devices and browsers.

**JavaScript for Form Validation**:
- The script (`script.js`) handles basic validation to ensure user input is present before allowing form submission.

---

## **API Endpoints**

| Endpoint | Method | Description                   | Response Format |
|----------|--------|-------------------------------|-----------------|
| `/`      | `GET`  | Renders the main HTML page    | HTML           |
| `/health`| `GET`  | Provides server status        | JSON           |

For detailed request/response structures and error handling, refer to **api_specifications.md**.

---

## **Error Handling**

### **Error Scenarios**
1. **Missing Template**: Returns a `500` error if the `index.html` file is missing.
2. **Unsupported HTTP Methods**: Returns `405` if a non-`GET` request is sent to the `/` or `/health` endpoints.
3. **Invalid Form Submission**: The `/submit` endpoint now returns a `400 Bad Request` if the `user_input` field is missing or empty.
  - **Client-Side**: Alerts users when required input is missing.
  - **Server-Side**: Validates form submission and returns appropriate error messages.
4. **HTTP Method Handling**:
- Added error handling for unsupported HTTP methods at key endpoints, such as `/health`.
- Custom 405 messages are returned to improve clarity.

### **Error Codes and Responses**
| Status Code | Scenario                       | Response               |
|-------------|--------------------------------|------------------------|
| `500`       | Missing Template               | `Internal Server Error`|
| `405`       | Unsupported HTTP Method        | `Method Not Allowed`   |

### **Logging and Debugging**
- **Debug Mode**: Enabled by default in development, providing error tracebacks.
- **Production**: Disable debug mode and configure error handling for production deployment.

---

## **Known Challenges**

1. **Cross-Platform Compatibility**:
   - Addressing file path and line-ending differences across Windows, macOS, and Linux.
   - Documented in `README.md` with solutions, including `.gitattributes` setup for line ending consistency【379†source】.

2. **Pre-Commit Hook Inconsistencies**:
   - Ensuring pre-commit hooks for linting and formatting are configured correctly across team environments【382†source】.

3. **Template Rendering Issues**:
   - Ensuring templates render as expected, with testing on multiple browsers to validate consistent UI【379†source】.

4. **Limited Initial Test Coverage**:
   - Expansion planned for test cases to include new routes and template scenarios, with a goal of achieving 80% coverage by version `0.0.0.3`【380†source】.

---

## **Future Directions**

1. **v0.0.0.3 - Basic HTML UI Setup**:
   - Introduce a minimal interactive UI with form fields and basic CSS styling【381†source】.

2. **v0.0.0.4 - Backend-UI Integration**:
   - Establish an API endpoint for form data submission and display responses on the HTML interface.

3. **Documentation Updates**:
   - Enhance **user_manual.md** for detailed usage instructions.
   - Include architecture diagrams and additional endpoint specifications.



### Error Handling Improvements

**New Error Scenarios**:



