# Web Vulnerability Scanner

A simple web tool to check for basic web security vulnerabilities such as SQL Injection, Cross-Site Scripting (XSS), and Directory Traversal.

## Table of Contents

- [Description](#description)
- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Contributing](#contributing)


## Description

This project is a simple Web Vulnerability Scanner developed using Flask and Python. It allows users to input a URL and checks for vulnerabilities such as SQL Injection, XSS, and Directory Traversal.

## Features

- **SQL Injection Scan**: Checks if a URL is vulnerable to SQL Injection attacks.
- **XSS Scan**: Checks if a URL is vulnerable to Cross-Site Scripting (XSS) attacks.
- **Directory Traversal Scan**: Checks if a URL is vulnerable to Directory Traversal attacks.

## Prerequisites

Ensure the following packages are installed on your system:

- Python 3
- Pip
- Virtual Environment (optional but recommended)
- Git

## Installation

1. Clone the repository:
   ```sh
   git clone <repository-url>
   cd web_vulnerability_scanner

2. Create and activate a virtual environment (optional but recommended):
   virtualenv venv
   source venv/bin/activate

3. Install the dependencies:
    pip install -r requirements.txt


# Usage

1. Start the Flask app:
    python run.py

2. Open your web browser and navigate to http://127.0.0.1:5000/.
3. Enter a URL you want to scan and click on "Scan".


# Project Structure
  web_vulnerability_scanner/
  │
  ├── app/
  │   ├── __init__.py
  │   ├── routes.py
  │   ├── static/
  │   │   └── styles.css
  │   └── templates/
  │       └── index.html
  │
  ├── scanner/
  │   ├── __init__.py
  │   ├── sql_injection.py
  │   ├── xss.py
  │   ├── directory_traversal.py
  │
  ├── tests/
  │   ├── __init__.py
  │   ├── test_scanner.py
  │
  ├── run.py
  └── requirements.txt

    app/: Contains the Flask application and routes.
    scanner/: Contains the scanner modules for SQL Injection, XSS, and Directory Traversal.
    tests/: Contains tests for the scanner modules.
    run.py: Starts the Flask application.
    requirements.txt: Lists the Python dependencies.


  # Contributing
    Contributions are welcome! Please create an issue before making changes and open a pull request for your changes.

  







