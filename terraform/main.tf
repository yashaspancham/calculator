resource "aws_s3_bucket" "calculator_logs_and_reports" {
  bucket        = "calculator-logs-and-reports-45367134"
  force_destroy = true #This is not best practice

  tags = {
    Name        = "Calculator Logs and Reports"
    Description = "S3 bucket for storing calculator logs and reports"
    ManagedBy   = "terraform"
    Project     = "Calculator"
  }
}


resource "aws_s3_bucket_public_access_block" "calculator_logs_and_reports" {
  bucket = aws_s3_bucket.calculator_logs_and_reports.id

  block_public_acls       = true
  block_public_policy     = true
  ignore_public_acls      = true
  restrict_public_buckets = true
}

resource "aws_s3_bucket_ownership_controls" "calculator_logs_and_reports" {
  bucket = aws_s3_bucket.calculator_logs_and_reports.id

  rule {
    object_ownership = "BucketOwnerEnforced"
  }
}

resource "aws_s3_bucket_versioning" "calculator_logs_and_reports" {
  bucket = aws_s3_bucket.calculator_logs_and_reports.id

  versioning_configuration {
    status = "Enabled"
  }
}