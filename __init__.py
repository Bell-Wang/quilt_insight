"""
os used for various operating system actions
boto used to interface with Amazon Web Services (currently only supported for Python 2.6 and 2.7)
"""
import os
import boto

"""This python modual containts functions for Richard Inman's Insight Data Engineering Project in
Silicon Valley (Jan. 2017).

Author: Rich H. Inman
email: rinman24@gmail.com
Date Created: 26 Jan. 2017
"""

def get_s3_file_boto(bucket_name, file_path, filename):
    """Use bucket_name and file_path to return parquet file.

    This function uses access keys from environment variables. Make sure to export access keys by
    adding the following to your .bash_profile (OSX) or .profile (Ubuntu):

    export AWS_ACCESS_KEY_ID=<your-access-key-id>
    export AWS_SECRET_ACCESS_KEY=<your-secret-access-key>
    export AWS_DEFALUT_REGION=<your-region> #e.g. us-west-2

    Note: This function is intended to load a file onto a single machine that has enough local disc
        space to hold the file. If you want to load a large file only a cluster that is running
        Spark then use the HiveContext or SQLContext in Spark. 

    Positional argument(s)
    bucket_name -- S3 bucket name
    file_path -- S3 file path

    Output(s):
    file -- requested file

    ISSUES: Still need to include type checking and try: except: statements to avoid errors
    """
    # Access Key ID and Key
    aws_access_key = os.getenv('AWS_ACCESS_KEY_ID', 'default')
    aws_secret_access_key = os.getenv('AWS_SECRET_ACCESS_KEY', 'default')

    # Create connection to S3 using Boto
    conn = boto.connect_s3(aws_access_key, aws_secret_access_key)

    # Connect to the S3 bucket
    bucket = conn.get_bucket(bucket_name)

    # Get the key for the file of interest
    key = bucket.get_key(file_path)

    # Save the Parquet file to disk
    key.get_contents_to_filename(filename +'.parquet')

