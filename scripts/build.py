import subprocess 
import shutil
from datetime import datetime
from scripts.utils import upload_file_to_s3, upload_folder_to_s3


print("Creating build....")

timestamp: str = datetime.now().strftime("%Y%m%d_%H%M%S")

subprocess.run(["mkdir", "-p", "logs/build_logs/"])
log_file=f"logs/build_logs/{timestamp}.log"

cmd = [
        "pyinstaller", 
        "--onefile",
        "--windowed",
        "--name",
        "calculator",
        "src/calculator/ui.py"
        ]

with open(log_file, "w") as log:
        proc = subprocess.Popen(cmd, 
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        text=True
        )
        for line in proc.stdout:
                print(line, end="")
                log.write(line)
        proc.wait()


upload_file_to_s3(log_file, log_file)

mkdir_cmd = "mkdir -p dist-zips".split(" ")
subprocess.run(mkdir_cmd)
shutil.make_archive(f"dist-zips/build-linux-{timestamp}", "zip", "dist")
upload_file_to_s3(
        f'dist-zips/build-linux-{timestamp}.zip',
        f"build/dist-{timestamp}.zip"
        )

