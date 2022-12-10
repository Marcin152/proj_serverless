import os.path
import pathlib
import boto3

s3_client = boto3.s3_client("s3")
bucket_name = "my-bucket"
object_name = "example1.txt"
file_name = os.path.join(pathlib.Path(object_name).parent.resolve(), "example_file.txt")
response = s3_client.upload_file(file_name, bucket_name,object_name)
