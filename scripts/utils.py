import boto3

s3 = boto3.client("s3")

def upload_file_to_s3(file_path: str, prefix: str):
        bucket_name="calculator-logs-and-reports-45367134"#change this as needed
        try:
                print(f"Uploading {file_path}...")
                s3.upload_file(
                        file_path,
                        bucket_name,
                        prefix
                )
                print(f"File {file_path} uploaded")
        except Exception as e:
                print(f"Error uploading {file_path}: {e}")
