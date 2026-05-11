output "bucket_name" {
  value = aws_s3_bucket.calculator_logs_and_reports.bucket
}


output "bucket_arn" {
  value = aws_s3_bucket.calculator_logs_and_reports.arn
}