# Desktop Calculator

A desktop calculator application built with Python and PyQt5, featuring a clean UI, full arithmetic and scientific operations, three-layer test coverage, and a CI pipeline running on AWS EC2 with artifacts stored in AWS S3.

---

## Features

- Basic arithmetic: `+`, `−`, `×`, `÷`
- Scientific operations: `√`, `x²`, `±`, `%`
- Input controls: `C` (clear), `⌫` (backspace), `.` (decimal)
- Edge case handling: division by zero, square root of negatives, chained operations
- macOS-inspired UI built with PyQt5

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
├── scripts/
│   ├── run_tests.py       # Test runner with S3 upload
│   └── build.py           # PyInstaller build with S3 upload
├── terraform/
│   └── main.tf            # S3, IAM, EC2, security group
├── logs/
├── reports/
├── requirements.txt
├── requirements-dev.txt
├── pytest.ini
├── Jenkinsfile
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
git clone https://github.com/yashaspancham/calculator.git
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
python3 -m scripts.run_tests
```

---

## CI Pipeline

The Jenkins pipeline runs on an AWS EC2 instance and triggers on every push to the GitHub repository via webhook (`yas-jenkins.redirectme.net`).

**Stages:**

1. **Checkout** — pull latest code from GitHub
2. **Install** — set up virtual environment and install packages
3. **Lint** — run `flake8` across `src/`, `scripts/`, and `tests/`
4. **Test** — run the full test suite; logs, reports, and allure results uploaded to S3
5. **Build** — run PyInstaller to produce a standalone executable and upload to S3 (main branch only)

A failed lint or test stage marks the build as failed and blocks merging via GitHub branch protection.

---

## Article

A full writeup of this project is available on Medium: [From Code to Cloud: Automated Testing, Jenkins CI, and AWS Infrastructure on a Python Calculator App](https://medium.com/@yashaspancham/from-code-to-cloud-automated-testing-jenkins-ci-and-aws-infrastructure-on-a-python-calculator-0aca8cd6e952)

---

## Tech Stack

| Layer | Technology |
|---|---|
| Language | Python 3.12 |
| UI Framework | PyQt5 |
| Testing | pytest, pytest-qt, pytest-cov, pytest-html, allure |
| Linting | flake8 |
| CI | Jenkins (Multibranch Pipeline) |
| Infrastructure | AWS EC2 |
| Artifact Storage | AWS S3 |
| IaC | Terraform |
| Build | PyInstaller |
| Version Control | GitHub |
