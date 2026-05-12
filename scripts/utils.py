import os
import boto3

s3 = boto3.client("s3")

def upload_file_to_s3(file_path: str):
        try:
                print(f"Uploading {file_path}...")
                s3.upload_file(
                        file_path,
                        "calculator-logs-and-reports-45367134",
                        file_path
                )
                print(f"File {file_path} uploaded")
        except Exception as e:
                print(f"Error uploading {file_path}: {e}")


# def upload_folder_to_s3(folder_path: str):
#         for root, dirs, files in os.walk(folder_path):
#                 for file in files:
#                         local_path 
