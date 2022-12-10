#adres arn

output "bucket_arn" {
  value       = local.enabled ? join("", aws_s3_bucket.default.*.arn) : ""
  description = "Bucket ARN"
}

#bucket name

output "bucket_id" {
  value       = local.enabled ? join("", aws_s3_bucket.default.*.id) : ""
  description = "Bucket Name (aka ID)"
}

#bucket domain name

output "bucket_domain_name" {
  value       = local.enabled ? join("", aws_s3_bucket.default.*.bucket_domain_name) : ""
  description = "FQDN of bucket"
}

#bucket website endpoint

output "bucket_website_endpoint" {
  value       = join("", aws_s3_bucket_website_configuration.default.*.website_endpoint, aws_s3_bucket_website_configuration.redirect.*.website_endpoint)
  description = "The bucket website endpoint, if website is enabled"
}