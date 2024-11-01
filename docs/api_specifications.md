Here’s an updated **API Specifications** document based on the enhancements in **v0.0.0.2**:

---

# **API Specifications**

This document outlines the API endpoints for Cortex **v0.0.0.2**, detailing request/response structures, data formats, and error handling. This version introduces the foundational routes with basic response handling for testing the Flask application.

---

## **Table of Contents**
1. [Overview](#overview)
2. [Endpoints](#endpoints)
   - [Root Route `/`](#root-route-)
   - [Health Check Route `/health`](#health-check-route-health)
3. [Request and Response Formats](#request-and-response-formats)
4. [Error Handling](#error-handling)
5. [Future Additions](#future-additions)

---

## **Overview**

The initial version of the Cortex API is designed to:
1. Provide a basic web page with the root route (`/`).
2. Offer a health check endpoint (`/health`) to verify server status.

The Flask application processes HTTP GET requests for both routes, utilizing HTML templating for the root and JSON response for health checks.

---

## **Endpoints**

### **Root Route `/`**

- **Description**: Serves the home page as an HTML document.
- **Endpoint**: `/`
- **HTTP Method**: `GET`
- **Response**: Renders the `index.html` template, which displays a welcome message.
- **Example Request**:
  ```http
  GET / HTTP/1.1
  Host: localhost:5000
  ```
- **Example Response**:
  ```html
  <!DOCTYPE html>
  <html lang="en">
  <head>
      <meta charset="UTF-8">
      <title>Welcome to Cortex</title>
  </head>
  <body>
      <h1>Hello, Cortex!</h1>
      <p>This is the landing page for Cortex v0.0.0.2.</p>
  </body>
  </html>
  ```

### **Health Check Route `/health`**

- **Description**: Provides server status, confirming the backend is running.
- **Endpoint**: `/health`
- **HTTP Method**: `GET`
- **Response**: JSON response with server status information.
- **Example Request**:
  ```http
  GET /health HTTP/1.1
  Host: localhost:5000
  ```
- **Example Response**:
  ```json
  {
      "status": "running"
  }
  ```

---

## **Request and Response Formats**

1. **Request Formats**:
   - Both endpoints accept standard HTTP GET requests.
   - `/` route returns an HTML document.
   - `/health` route returns a JSON response.
   
2. **Response Formats**:
   - `/` route renders HTML via Flask’s `render_template()` function.
   - `/health` route uses Flask’s `jsonify()` to return JSON.

---

## **Error Handling**

### **1. Unsupported Methods**
   - Routes `/` and `/health` only support the `GET` method.
   - **Error Response**:
     - **Status Code**: `405 Method Not Allowed`
     - **Response Body**:
       ```json
       {
           "error": "Method Not Allowed"
       }
       ```

### **2. Template Not Found**
   - If the `index.html` template is missing or misconfigured, the server will respond with an error.
   - **Error Response**:
     - **Status Code**: `500 Internal Server Error`
     - **Response Body** (Default Flask error message):
       ```html
       <!DOCTYPE html>
       <html lang="en">
       <head>...</head>
       <body>
           <h1>Internal Server Error</h1>
           <p>The server encountered an internal error and could not complete your request.</p>
       </body>
       </html>
       ```

### **3. General Error Handling**
   - All unhandled errors will return a `500 Internal Server Error` status code, indicating that an internal issue has occurred.

---

## **Future Additions**

Future versions will introduce:
1. **Input Validation**: Validation rules for new routes and forms to ensure data integrity.
2. **Authentication**: Secure access for restricted endpoints.
3. **Error Page Customization**: Define custom templates for error codes (404, 500) to improve user experience.
