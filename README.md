# Secure Login System

## Overview

Secure Login System is a web application developed using Python Flask. The project demonstrates secure user authentication by implementing password hashing, SQL injection protection, session management, and login activity logging.

## Features

* User Registration
* Secure User Login
* Password Hashing using bcrypt
* SQL Injection Protection
* Session Management
* Logout Functionality
* Input Validation
* Login Activity Logging
* Security Audit Report
* Future Support for Two-Factor Authentication (2FA)

## Technologies Used

* Python
* Flask
* SQLite
* bcrypt
* HTML
* Bootstrap 5

## Project Structure

```text
SecureLoginSystem
│
├── app.py
├── database.db
├── logs.txt
├── README.md
│
└── templates
    ├── login.html
    ├── register.html
    ├── dashboard.html
    └── security.html
```

## Security Features

* Passwords are stored using bcrypt hashing.
* SQL Injection attacks are prevented using parameterized queries.
* User sessions are managed securely.
* Login activities are recorded in log files.
* Input validation is implemented for user data.

## Learning Outcomes

This project helped in understanding:

* Authentication mechanisms
* Secure password storage
* Session management
* Web application security fundamentals
* Secure coding practices using Flask

## Author

Developed as part of a Cybersecurity Internship Project.
