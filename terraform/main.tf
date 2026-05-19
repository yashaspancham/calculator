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


resource "tls_private_key" "jenkins_key" {
  algorithm = "RSA"
  rsa_bits  = 4096
}

resource "aws_key_pair" "jenkins_key" {
  key_name   = "jenkins-key"
  public_key = tls_private_key.jenkins_key.public_key_openssh
}


resource "aws_instance" "jenkins_server" {
  ami = ""
  instance_type = "t2.micro"
  tags = {
    Name        = "Jenkins server"
    Description = "Jenkins server for CI pipeline tests and builds Calculator"
    ManagedBy   = "terraform"
    Project     = "Calculator"
  }
}


resource "aws_security_group" "jenkins_sg" {
  name = "jenkins-sg"
  description = "Security group for jenkins server"

  ingress {
    description = "jenkins UI"
    from_port = 8080
    to_port = 8080
    protocol = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  ingress {
    description = "ssh"
    from_port = 22
    to_port = 22
    protocol = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  egress {
    description = "all outbound"
    from_port = 0
    to_port = 0
    protocol = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
}
