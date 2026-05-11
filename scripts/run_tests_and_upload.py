from datetime import datetime
import subprocess
import sys

timestamp: str = datetime.now().strftime("%Y%m%d_%H%M%S")

mkdir_cmd = "mkdir -p logs reports/test-report reports/coverage reports/allure/allure-$timestamp-results reports/allure-$timestamp-report".split(" ")
subprocess.run(mkdir_cmd)

log_file = f"logs/{timestamp}.log"
cmd = [
        sys.executable, "-m", "pytest",
                f"--html=reports/test-report/{timestamp}.html", "--self-contained-html",
                "--cov=src/calculator", f"--cov-report=html:reports/coverage/{timestamp}",
                f"--alluredir=reports/allure/allure-{timestamp}-results",
]

with open(log_file, "w") as log:
                proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
        text=True)
        for line in proc.stdout:
                print(line, end="")
                log.write(line)
        proc.wait()

# store exit code from proc.returncode

# if exit code is 0 or 1:
#     create s3 client
#
#     upload log file
#     upload test report html
#     upload coverage directory (walk and upload each file)
#     upload allure results directory (walk and upload each file)

# exit with pytest's exit code

