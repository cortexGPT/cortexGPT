# API Specifications

## Overview

This document provides a detailed specification for the available endpoints, their input/output formats, request/response structures, and error handling standards used in the Cortex chatbot application.

### Table of Contents
- `/health`
- `/submit`
- HTML UI Interactions
- Error Handling Standards
- Input Validation

## Endpoint: `/health`

**Method**: `GET`

**Description**: Returns the current status of the application to indicate if the server is running correctly.

**Response Format**:
- **Status Code**: `200 OK`
- **Body**:
  - `status` (string): Indicates the health of the server.

**Response Example**:
```json
{
  "status": "running"
}
```

**Error Handling**:
- **405 Method Not Allowed**: If a method other than `GET` is used (e.g., `POST`).
  - **Response Example**:
    ```json
    {
      "error": "Method Not Allowed"
    }
    ```

## New Endpoint: `/submit`

**Method**: `POST`

**Description**: This endpoint processes the user's input submitted from the HTML form and returns a response with the sanitized content.

**Request Format**:
- Content-Type: `application/x-www-form-urlencoded`
- **Parameters**:
  - `user_input` (string): The input text provided by the user. This field is required.

**Request Example**:
```sh
POST /submit HTTP/1.1
Host: 127.0.0.1:5000
Content-Type: application/x-www-form-urlencoded

user_input=Hello%20World
```

**Response Format**:
- **Status Code**: `200 OK` (Successful input processing)
- **Body**:
  - `message` (string): The processed input message.

**Response Example**:
```json
{
  "message": "Received: Hello World"
}
```

**Error Handling**:
- **400 Bad Request**: Returned when the `user_input` field is missing or empty.
  - **Response Example**:
    ```json
    {
      "error": "Input is required"
    }
    ```

**Notes**:
- Input is sanitized using Markupsafe's `escape()` to prevent Cross-Site Scripting (XSS) attacks.

## HTML UI Interactions

**Form Submission Endpoint**:
- The HTML form at `/` sends a `POST` request to the `/submit` endpoint.
- The form data is submitted as `application/x-www-form-urlencoded` content.

**JavaScript Validation**:
- Before submission, JavaScript validates the `user_input` to ensure it is not empty.
- If `user_input` is empty, a client-side alert is triggered, and the request is not sent.

**Error Scenarios**:
- **Empty Input Field**:
  - **Client-Side**: JavaScript will prevent the form from being submitted if `user_input` is empty, with an alert message: `"Input is required!"`.
  - **Server-Side**: If the validation fails at the server level, a `400 Bad Request` response is returned.

## Error Handling Standards

- **400 Bad Request**:
  - **Context**: Missing or invalid input for required fields.
  - **Example**:
    ```json
    {
      "error": "Input is required"
    }
    ```

- **405 Method Not Allowed**:
  - **Context**: Incorrect HTTP method used for an endpoint (e.g., using `POST` on `/health`).
  - **Example**:
    ```json
    {
      "error": "Method Not Allowed"
    }
    ```

- **Cross-Site Scripting Prevention**:
  - All input data is sanitized using Markupsafe's `escape()` to mitigate the risk of XSS attacks. This is especially important for user-provided text, which is then rendered back in the HTML.

## Input Validation

**Client-Side Validation**:
- Implemented in JavaScript (`/static/script.js`) to ensure required fields are filled before form submission.
- If validation fails, an alert is displayed, and the submission is prevented.

**Server-Side Validation**:
- All inputs are validated again upon receiving the request.
- Empty or invalid `user_input` results in a `400 Bad Request` error.

---