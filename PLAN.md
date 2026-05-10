# PyQt5 Calculator — Project Plan

## Project Structure

```
calculator/
├── src/calculator/
│   ├── engine.py        # Pure logic, no Qt
│   ├── ui.py            # PyQt5 MainWindow
│   └── logger.py        # Logging setup
├── tests/
│   ├── unit/            # test_engine.py
│   ├── integration/     # test_calculator_flow.py
│   └── ui/              # test_ui.py (pytest-qt)
├── logs/
├── reports/
├── requirements.txt
├── requirements-dev.txt
├── pytest.ini
└── Jenkinsfile
```

---

## Phase 1 — Calculator App

**Operations:** `+`, `-`, `×`, `÷`, `%`, `√`, `x²`, `+/-` (negate), plus `C`, `⌫`, `.`, `=`

**Key design decision:** split engine from UI. `engine.py` holds all math logic as plain Python — no Qt. This makes it directly unit-testable without needing a display.

---

## Phase 2 — Testing

| Layer       | Tool       | What it tests                                      |
|-------------|------------|----------------------------------------------------|
| Unit        | `pytest`   | `engine.py` functions in isolation                 |
| Integration | `pytest`   | engine state across a sequence of operations       |
| UI          | `pytest-qt`| button clicks, display updates, keyboard input     |

**Edge cases to cover:** division by zero, chained ops, float precision, `√` of negative numbers.

---

## Phase 3 — Reporting & Logging

- **Logging** (`logging` stdlib) — log every operation + errors to `logs/calculator.log`, rotating file handler
- **Coverage** — `pytest-cov` → HTML report + terminal summary
- **Test report** — `pytest-html` → `reports/report.html`
- **JUnit XML** — `pytest --junitxml=reports/results.xml` → consumed by Jenkins

---

## Phase 4 — Jenkins CI

Declarative `Jenkinsfile` with stages:

```
Checkout → Install deps → Lint (flake8) → Test + Coverage → Archive Reports
```

Jenkins will publish JUnit results (test trends graph) and archive the HTML coverage + test reports as build artifacts.

---

## Open Questions

1. Do you want a `pyproject.toml` (modern) or `requirements.txt`-only setup?
2. Should the app window be fixed size or resizable?
3. Do you have Jenkins already running, or do we also need a `docker-compose.yml` to spin one up locally?
