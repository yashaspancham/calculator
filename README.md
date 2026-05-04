# Desktop Calculator

A desktop calculator application built with Python and PyQt5, featuring a clean UI, full arithmetic and scientific operations, three-layer test coverage, and a CI pipeline running on AWS EC2 with artifacts stored in AWS S3.

---

## Features

- Basic arithmetic: `+`, `−`, `×`, `÷`
- Scientific operations: `√`, `x²`, `±`, `%`
- Input controls: `C` (clear), `⌫` (backspace), `.` (decimal)
- Edge case handling: division by zero, square root of negatives, chained operations
- Clean dark-themed UI built with PyQt5

---

## Project Structure

```
calculator/
├── src/calculator/
│   ├── engine.py          # Pure math logic, no Qt
│   ├── ui.py              # PyQt5 main window
│   ├── theme.py           # Centralised UI theme
│   └── widgets/
│       ├── display.py     # Display widget
│       └── keyboard.py    # Button grid
├── tests/
│   ├── unit/              # Engine unit tests
│   ├── integration/       # Multi-step operation tests
│   ├── ui/                # pytest-qt UI tests
│   └── logger.py          # Test logging setup
├── logs/
├── reports/
├── requirements.txt
├── requirements-dev.txt
├── pytest.ini
├── Jenkinsfile
├── REQUIREMENTS.md
└── .gitignore
```

---

## Getting Started

### Prerequisites

- Python 3.12+
- PyQt5

### Setup

```bash
# Clone the repository
git clone https://github.com/<your-username>/calculator.git
cd calculator

# Create and activate virtual environment
python3 -m venv v_env
source v_env/bin/activate

# Install dependencies
pip install -r requirements-dev.txt
```

### Run the application

```bash
python3 -m src.calculator.ui
```

---

## Running Tests

```bash
# Run all tests with coverage
pytest --cov=src --cov-report=html:reports/coverage --html=reports/report.html --junitxml=reports/results.xml
```

---

## CI Pipeline

The Jenkins pipeline runs on an AWS EC2 instance and triggers on every push to the GitHub repository via webhook.

**Stages:**

1. **Checkout** — pull latest code from GitHub
2. **Install Dependencies** — set up virtual environment and install packages
3. **Lint** — run `flake8` across the source
4. **Test** — run the full test suite with coverage
5. **Upload** — push reports and artifacts to AWS S3

A failed lint or test stage marks the build as failed.

---

## Tech Stack

| Layer | Technology |
|---|---|
| Language | Python 3.12 |
| UI Framework | PyQt5 |
| Testing | pytest, pytest-qt, pytest-cov, pytest-html |
| Linting | flake8 |
| CI | Jenkins |
| Infrastructure | AWS EC2 |
| Artifact Storage | AWS S3 |
| Version Control | GitHub |
