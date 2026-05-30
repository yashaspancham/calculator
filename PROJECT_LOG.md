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

- **Test** runs on every branch — ensures branch protection gets accurate signal
- **Build** runs only on `main` branch
- JUnit XML published on every run (`post { always }`)
- `sys.exit` in `run_tests.py` ensures test failures block the Build stage
- Last 10 builds kept, older ones auto-discarded (`buildDiscarder`)
- Workspace wiped after every build (`cleanWs()`) to prevent disk fill

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

### Session 4 — No-IP boot persistence, AMI prep
- Created `/etc/systemd/system/noip2.service` unit file for No-IP dynamic DNS client
- Killed orphaned `noip2` process (was running as `nobody`, not managed by systemd)
- Enabled and started service via systemd — `active (running)`, survives reboots
- EC2 instance is now AMI-ready: Jenkins `enabled`, No-IP `enabled`

### Session 3 — Bug fixes, pipeline hardening, IAM prep
- Fixed 2 failing integration tests: `√` of negated number returning wrong result, backspace on "Welcome" display stripping characters
- Fixed Jenkins branch discovery strategy ("All branches") so webhooks trigger builds when a PR is open
- Moved Test stage to run on all branches (not just PRs/main) so branch protection accurately reflects test results
- Verified branch protection blocks merge on failing tests end-to-end
- Added `buildDiscarder` (keep last 10 builds) and `cleanWs()` to Jenkinsfile to manage EC2 disk space
- Uncommented IAM resources in `terraform/main.tf`: role, policy (`s3:PutObject`), attachment, instance profile — ready to `terraform apply`
- Added `PROJECT_LOG.md` for session tracking

---

## Current Status

| Item | Status |
|---|---|
| Jenkinsfile | Done |
| GitHub webhook via No-IP | Done |
| Branch protection ruleset | Done |
| Test failure blocks merge | Done — verified end-to-end |
| All tests passing | Done — 228 passed on main |
| PyInstaller build | Done — produces `dist/calculator` on main |
| Jenkins branch discovery | Fixed — "All branches" strategy |
| Workspace auto-cleanup | Done — `cleanWs()` + `buildDiscarder(10)` |
| IAM role Terraform resources | Done — uncommented, ready to apply |
| S3 artifact uploads | Blocked — IAM role not yet attached to EC2 |
| JUnit trend graph in Jenkins | Fixed — path corrected to `reports/test-report/*.xml` |
| No-IP systemd service | Done — `enabled`, `active (running)` |
| EC2 AMI snapshot | Not started |
| Terraform AMI ID | Not started — placeholder in `terraform/main.tf` |

---

## Pending Work

1. **Create EC2 AMI** — AWS Console → EC2 → select Jenkins instance → Actions → Image and templates → Create image (name: `jenkins-calculator-v1`)
2. **`terraform apply`** — creates IAM role, policy, attachment, instance profile
3. **Attach IAM role to EC2** — `jenkins-ec2-profile` via AWS Console → EC2 → Actions → Security → Modify IAM role — needed for S3 uploads
4. **Verify S3 uploads** — run a build on main after IAM role is attached
5. **Fill in AMI ID** — update `ami = ""` placeholder in `terraform/main.tf`

---

## Known Issues

- EC2 lacks an IAM instance profile → S3 uploads fail with "Unable to locate credentials" (fix: `terraform apply` then attach `jenkins-ec2-profile` via console)
