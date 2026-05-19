from datetime import datetime
import subprocess
import sys
import shutil
from scripts.utils import upload_file_to_s3, upload_folder_to_s3

timestamp: str = datetime.now().strftime("%Y%m%d_%H%M%S")

mkdir_cmd = "mkdir -p logs/test_logs reports/test-report reports/coverage reports/allure/".split(" ")
subprocess.run(mkdir_cmd)

log_file = f"logs/test_logs/{timestamp}.log"
cmd = [
        sys.executable, "-m", "pytest",
                f"--html=reports/test-report/{timestamp}.html", "--self-contained-html",
                "--cov=src/calculator", f"--cov-report=html:reports/coverage/{timestamp}",
                f"--alluredir=reports/allure/allure-{timestamp}-results",
]

with open(log_file, "w") as log:
        proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
        for line in proc.stdout:
                print(line, end="")
                log.write(line)
        proc.wait()


upload_file_to_s3(log_file, log_file)

upload_file_to_s3(f"./reports/test-report/{timestamp}.html", f"reports/test-report/{timestamp}.html")



shutil.make_archive(
        f"./reports/coverage/{timestamp}",
        "zip",
        f"./reports/coverage/{timestamp}"
        )
upload_file_to_s3(
        f"./reports/coverage/{timestamp}.zip",
        f"reports/coverage/{timestamp}.zip"
)

shutil.make_archive(
        f"./reports/allure/allure-{timestamp}-results",
        "zip",
        f"reports/allure/allure-{timestamp}-results"
)
upload_file_to_s3(
        f"./reports/allure/allure-{timestamp}-results.zip",
        f"reports/allure/allure-{timestamp}-results.zip"
)