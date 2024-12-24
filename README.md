# Polynomial Operations in Galois Fields (GF(2^m))

This project implements polynomial arithmetic in Galois Fields (GF(2^m)) with a focus on mathematical rigor, computational accuracy, and user-centered design. It provides a robust backend and an intuitive frontend to support operations such as addition, subtraction, multiplication, division, modulo reduction, and inversion. The project has wide applications in cryptography, error correction, and digital communication.

## Table of Contents

1. [Introduction](#introduction)
2. [Goals & Features](#goals--features)
3. [Core Functions](#core-functions)
4. [Backend](#backend)
5. [Frontend](#frontend)
6. [Hosting & Deployment](#hosting--deployment)
7. [Conclusion](#conclusion)
8. [GitHub Repositories](#github-repositories)

---

## Introduction

Polynomial arithmetic in GF(2^m) is a cornerstone of secure cryptographic algorithms, robust error-correcting codes, and efficient digital communication systems. This project addresses the complexities of polynomial operations in finite fields, providing a scalable solution for diverse applications.

---

## Goals & Features

### Goals:
- Develop a tool for accurate polynomial arithmetic in GF(2^m).
- Ensure a seamless user experience through an interactive frontend and reliable backend.
- Enable key operations: addition, subtraction, multiplication, division, modulo reduction, and inversion.
- Support binary and hexadecimal input with dynamic result formatting.

### Features:
- **Backend**: Built with Python, featuring modular design, robust error handling, and RESTful APIs.
- **Frontend**: Modern, responsive design using frameworks, intuitive input fields, and dynamic buttons.
- **Scalability**: Fully documented API for integration and extension.
- **Accessibility**: Secure hosting and deployment for consistent availability.

---

## Core Functions

1. **Addition/Subtraction**:
   - Unified as a single operation using XOR in GF(2^m).
2. **Multiplication**:
   - Includes bitwise operations with modulo reduction using irreducible polynomials.
3. **Modulo Reduction**:
   - Reduces polynomials to their smallest equivalent representation within GF(2^m).
4. **Division**:
   - Computes both quotient and remainder using polynomial alignment and XOR.
5. **Inversion**:
   - Uses the Extended Euclidean Algorithm to compute the multiplicative inverse.

---

## Backend

The backend serves as the computational engine, handling all polynomial operations with precision and efficiency. It includes:
- **RESTful API**: All operations exposed via a documented API.
- **Error Handling**: Structured responses for exceptions.
- **Testing**: Pytest for validation and debugging.
- **Logging**: Comprehensive logs for easy troubleshooting.

API documentation is available via Swagger: [Swagger Interface](https://rubah.pythonanywhere.com/apidocs).

---

## Frontend

The frontend provides a visually engaging and interactive interface, featuring:
- **Team Presentation**: Cards for team members with flip animations and thematic hints.
- **Operations Page**:
  - Intuitive buttons for each polynomial operation.
  - Input fields for parameters (binary/hexadecimal format, number of bits, etc.).
  - Compute button for clarity and ease of use.
  - Disabled fields for unsupported operations like Modulo and Inversion.
- **Mobile Responsiveness**: Fully responsive for mobile devices.

---

## Hosting & Deployment

The project is securely hosted on AWS Route S3, ensuring accessibility and reliable performance. Visit the tool at: [https://galois-field-operations.com/](https://galois-field-operations.com/).

---

## Conclusion

This project successfully bridges mathematical complexity and user-friendly design, enabling precise polynomial arithmetic in GF(2^m). Its scalable architecture and secure hosting make it a versatile solution for cryptography, error correction, and digital communication.

---

## GitHub Repositories

- **Frontend**: [Polynomial Arithmetic Frontend](https://github.com/hawraakhalil/Polynomial_Arithmetic_Frontend)
- **Backend**: [Polynomial Arithmetic Backend](https://github.com/RubaHoussami/Polynomial_Arithmetic)
