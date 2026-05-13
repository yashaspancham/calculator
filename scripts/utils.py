import os
import boto3

s3 = boto3.client("s3")

def upload_file_to_s3(file_path: str, prefix: str):
        try:
                print(f"Uploading {file_path}...")
                s3.upload_file(
                        file_path,
                        "calculator-logs-and-reports-45367134",
                        prefix
                )
                print(f"File {file_path} uploaded")
        except Exception as e:
                print(f"Error uploading {file_path}: {e}")


def upload_folder_to_s3(folder_path, bucket_name, s3_prefix=""):
        print(f"Uploading {folder_path}...")
        for root, dirs, files in os.walk(folder_path):
                for file in files:
                        local_path = os.path.join(root, file)

                        relative_path = os.path.relpath(local_path, folder_path)

                        s3_path = f"{s3_prefix}/{relative_path}".replace("\\", "/")

                        s3.upload_file(local_path, bucket_name, s3_path)

        print(f"Uploaded {folder_path}.")
