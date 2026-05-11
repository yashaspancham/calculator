# Calculator Application — Requirements Document

**Project:** Desktop Calculator  
**Version:** 1.0  
**Date:** 2026-05-02  
**Status:** Draft  

---

## 1. Overview

A desktop calculator application built with Python and PyQt5. The application provides standard arithmetic and scientific operations through a graphical user interface, with full test coverage and CI integration via Jenkins hosted on AWS EC2. Source code is managed in GitHub and build artifacts are stored in AWS S3.

---

## 2. Functional Requirements

### 2.1 Arithmetic Operations

| ID   | Requirement                                               |
|------|-----------------------------------------------------------|
| F-01 | The application shall support addition (`+`)              |
| F-02 | The application shall support subtraction (`-`)           |
| F-03 | The application shall support multiplication (`×`)        |
| F-04 | The application shall support division (`÷`)              |
| F-05 | The application shall support percentage (`%`)            |
| F-06 | The application shall support square root (`√`)           |
| F-07 | The application shall support squaring a number (`x²`)    |
| F-08 | The application shall support sign negation (`+/-`)       |

### 2.2 Input Controls

| ID   | Requirement                                                        |
|------|--------------------------------------------------------------------|
| F-09 | The application shall provide digit buttons `0` through `9`        |
| F-10 | The application shall provide a decimal point (`.`) button         |
| F-11 | The application shall provide a clear (`C`) button to reset state  |
| F-12 | The application shall provide a backspace (`⌫`) button to delete the last character |
| F-13 | The application shall provide an equals (`=`) button to evaluate the current expression |

### 2.3 Display

| ID   | Requirement                                                                 |
|------|-----------------------------------------------------------------------------|
| F-14 | The display shall show the current input in real time                       |
| F-15 | The display shall show the result after `=` is pressed                      |
| F-16 | The display shall be read-only (no direct keyboard text entry into the field)|
| F-17 | The display shall right-align all content                                   |

### 2.4 Edge Case Handling

| ID   | Requirement                                                              |
|------|--------------------------------------------------------------------------|
| F-18 | Division by zero shall display a clear error message, not crash          |
| F-19 | Square root of a negative number shall display a clear error message     |
| F-20 | Chained operations shall evaluate correctly without requiring `=`        |
| F-21 | Repeated pressing of `=` shall not alter the last result                 |

---

## 3. Non-Functional Requirements

### 3.1 Architecture

| ID   | Requirement                                                                          |
|------|--------------------------------------------------------------------------------------|
| N-01 | Business logic shall be fully separated from UI code (`engine.py` vs `ui.py`)       |
| N-02 | `engine.py` shall contain no Qt imports, making it independently unit-testable       |
| N-03 | Theming shall be centralised in a single `theme.py` module                           |

### 3.2 Performance

| ID   | Requirement                                                    |
|------|----------------------------------------------------------------|
| N-04 | The application shall launch within 3 seconds on target hardware |
| N-05 | All button responses shall register within 100 ms              |

### 3.3 Usability

| ID   | Requirement                                                              |
|------|--------------------------------------------------------------------------|
| N-06 | The UI shall follow the dark theme defined in `theme.py`                 |
| N-07 | Button labels shall be legible at the default window size                |

---

## 4. Logging Requirements

Logging is scoped to the test pipeline only — the application itself does not log at runtime.

| ID   | Requirement                                                                           |
|------|---------------------------------------------------------------------------------------|
| L-01 | Every test operation and assertion shall be logged with a timestamp                   |
| L-02 | Test errors and failures shall be logged at `ERROR` level                             |
| L-03 | Logs shall be written to `logs/calculator.log`                                        |
| L-04 | The log file shall use a rotating file handler (max 5 MB per file, 3 backups)         |
| L-05 | Logging shall be configured in a dedicated `logger.py` module used by the test suite  |

---

## 5. Testing Requirements

### 5.1 Unit Tests

| ID   | Requirement                                                              |
|------|--------------------------------------------------------------------------|
| T-01 | All functions in `engine.py` shall have corresponding unit tests         |
| T-02 | Edge cases F-18 through F-21 shall each have a dedicated unit test       |

### 5.2 Integration Tests

| ID   | Requirement                                                                    |
|------|--------------------------------------------------------------------------------|
| T-03 | Tests shall verify correct state across a sequence of chained operations       |
| T-04 | Tests shall verify that `C` fully resets engine state                          |

### 5.3 UI Tests

| ID   | Requirement                                                                      |
|------|----------------------------------------------------------------------------------|
| T-05 | UI tests shall use `pytest-qt`                                                   |
| T-06 | Tests shall simulate button clicks and verify display output                     |
| T-07 | Keyboard input tests are deferred until keyboard support is implemented          |

### 5.4 Coverage & Reporting

| ID   | Requirement                                                                    |
|------|--------------------------------------------------------------------------------|
| T-08 | Test coverage shall be measured with `pytest-cov`                              |
| T-09 | An HTML coverage report shall be generated to `reports/coverage/`              |
| T-10 | A test report shall be generated to `reports/report.html` via `pytest-html`    |
| T-11 | A JUnit XML report shall be generated to `reports/results.xml`                 |

---

## 6. CI Requirements

| ID   | Requirement                                                                             |
|------|-----------------------------------------------------------------------------------------|
| C-01 | A `Jenkinsfile` shall define a declarative CI pipeline                                      |
| C-02 | The pipeline shall include stages: Checkout, Install Dependencies, Lint, Test, Upload        |
| C-03 | Jenkins shall be hosted on an AWS EC2 instance                                               |
| C-04 | Source code shall be version-controlled in GitHub                                         |
| C-05 | The Jenkins pipeline shall trigger on commits via GitHub webhooks                         |
| C-06 | Linting shall use `flake8`                                                                   |
| C-07 | Jenkins shall publish JUnit test results for trend tracking                                  |
| C-08 | Build artifacts (HTML coverage report, test report, JUnit XML) shall be uploaded to AWS S3  |
| C-09 | A failed lint or test stage shall mark the build as failed                                   |

---

## 7. Project Structure

```
calculator/
├── src/calculator/
│   ├── engine.py
│   ├── ui.py
│   ├── theme.py
│   └── widgets/
│       └── display.py
├── tests/
│   ├── unit/
│   ├── integration/
│   ├── ui/
│   └── logger.py
├── logs/
├── reports/
├── requirements.txt
├── requirements-dev.txt
├── pytest.ini
└── Jenkinsfile
```

---

## 8. Out of Scope

- Scientific/trigonometric functions (sin, cos, tan, log)
- Expression history or memory registers
- Keyboard input support and keyboard-driven UI tests
- Multi-window or multi-instance support
- Mobile or web deployment
