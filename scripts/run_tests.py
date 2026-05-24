from datetime import datetime
import os
import subprocess
import sys
import shutil
from scripts.utils import upload_file_to_s3

timestamp: str = datetime.now().strftime("%Y%m%d_%H%M%S")

mkdir_cmd = "mkdir -p logs/test_logs reports/test-report reports/coverage reports/allure/".split(" ")
subprocess.run(mkdir_cmd)

log_file = f"logs/test_logs/{timestamp}.log"
cmd = [
    sys.executable, "-m", "pytest",
    f"--html=reports/test-report/{timestamp}.html", "--self-contained-html",
    "--cov=src/calculator", f"--cov-report=html:reports/coverage/{timestamp}",
    f"--alluredir=reports/allure/allure-{timestamp}-results",
    f"--junitxml=reports/test-report/{timestamp}.xml"
]

with open(log_file, "w") as log:
    proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
    for line in proc.stdout:
        print(line, end="")
        log.write(line)
    proc.wait()

exit_code = proc.returncode

upload_file_to_s3(log_file, log_file)

if os.path.exists(f"./reports/test-report/{timestamp}.html"):
    upload_file_to_s3(
        f"./reports/test-report/{timestamp}.html",
        f"reports/test-report/{timestamp}.html"
    )

if os.path.exists(f"./reports/test-report/{timestamp}.xml"):
    upload_file_to_s3(
        f"./reports/test-report/{timestamp}.xml",
        f"reports/test-report/{timestamp}.xml"
    )

coverage_dir = f"./reports/coverage/{timestamp}"
if os.path.exists(coverage_dir):
    shutil.make_archive(coverage_dir, "zip", coverage_dir)
    upload_file_to_s3(f"{coverage_dir}.zip", f"reports/coverage/{timestamp}.zip")

allure_dir = f"reports/allure/allure-{timestamp}-results"
if os.path.exists(allure_dir):
    shutil.make_archive(f"./{allure_dir}", "zip", allure_dir)
    upload_file_to_s3(f"./{allure_dir}.zip", f"{allure_dir}.zip")

sys.exit(exit_code)