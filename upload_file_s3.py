#!/usr/bin/python
#
# This script is used to upload a file S3 bucket.

# Import module
import boto3

# Define a function to upload a file to S3 bucket.
# If the upload is not completed, print the error.
# If no error, then print an upload complete message.
def upload_trap_file(trapFile):
    # Let's use Amazon S3
    s3 = boto3.resource('s3')
    # Set S3 bucket name.
    bucket="test_bucket"
    # Set the file name.
    file = "test.txt"
    # Set the data of the file.
    data = open(file, 'rb')
    # Defile an error message.
    upload_err_msg = ' Error while uploading Trap File to S3 Bucket '
    # Define a successful upload message.
    upload_msg = ' {} test file uploaded to S3 \r\n'.format(file)
    try:
        s3.Bucket(bucket).put_object(Key=file, Body=data)
        print(upload_msg)
    except Exception as e:
        uploadExceptionMessage = upload_err_msg + str(e) + '\r\n'
        print(uploadExceptionMessage)