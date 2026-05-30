# Calculator Project Log

A running record of what's been built, what's broken, and what's next.

---

## Infrastructure

| Component | Detail |
|---|---|
| App | PyQt5 desktop calculator, Python 3.12 |
| CI Server | Jenkins on AWS EC2 |
| Webhook routing | No-IP hostname: `yas-jenkins.redirectme.net` |
| Artifact storage | AWS S3 |
| IaC | Terraform (`terraform/`) |
| Repo | GitHub, branch protection via ruleset "jenkins ci" |

---

## CI Pipeline Stages

```
Checkout → Install → Lint (flake8) → Test → Build (PyInstaller)
```

- **Test** runs only on PRs or `main` branch
- **Build** runs only on `main` branch
- JUnit XML published on every run (`post { always }`)
- `sys.exit` in `run_tests.py` ensures test failures block the Build stage

---

## Session Log

### Session 1 — App build
- Built `engine.py` (pure math, no Qt): `calculate_expression`, `square_root`, `square`, `negate`, `_handle_percentage`, `extract_last_number`
- Built PyQt5 UI: dark theme, full button grid, display widget
- Three-layer test suite: unit / integration / UI (pytest-qt), all driven by CSV test case files
- Logging to `logs/calculator.log`, coverage HTML + pytest-html reports

### Session 2 — CI/CD pipeline
- Set up Jenkins Multibranch Pipeline on AWS EC2
- Configured No-IP hostname `yas-jenkins.redirectme.net` to route GitHub webhooks to EC2 dynamic IP
- Wrote `Jenkinsfile` with all 5 stages
- Added `githubPush()` trigger and `QT_QPA_PLATFORM=offscreen` for headless PyQt5
- Fixed Python 3.9 type syntax (`Union[int, float, str]`) in `engine.py` and `unit_test.py`
- Added `.flake8` config suppressing formatting-only errors
- GitHub branch protection ruleset requiring `continuous-integration/jenkins/branch` to pass before merge
- Updated GitHub PAT with `repo:status` scope in Jenkins credentials

---

## Current Status

| Item | Status |
|---|---|
| Jenkinsfile | Done |
| GitHub webhook via No-IP | Done |
| Branch protection ruleset | Done |
| Test failure blocks build | Done |
| S3 artifact uploads | Blocked — EC2 has no IAM role attached |
| All tests passing | Blocked — 4 test cases failing |
| EC2 AMI snapshot | Not started |
| Terraform AMI ID | Not started — placeholder in `terraform/main.tf` |

---

## Pending Work

1. **Fix 4 failing test cases** — failing locally and in CI; identify and fix them so pipeline goes green
2. **Attach IAM role to EC2** — `jenkins-ec2-profile` via AWS Console → EC2 → Actions → Security → Modify IAM role — needed for S3 uploads
3. **Verify pipeline passes** — check Jenkins build for latest `Yashas_test` PR (commit `2e59315`)
4. **Create EC2 AMI** — snapshot the instance after IAM role is attached and pipeline is green
5. **Fill in AMI ID** — update `ami = ""` placeholder in `terraform/main.tf`

---

## Known Issues

- EC2 lacks an IAM instance profile → S3 uploads fail with "Unable to locate credentials"
- 4 unit test cases fail (reproduce locally with `pytest tests/unit/`)
