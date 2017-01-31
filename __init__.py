"""
os used for various operating system actions
boto used to interface with Amazon Web Services (supported for Python 2 and 3)
numpy used for random number generation
pandas used for creating DataFrames
fastparquet used for writing Parquet files
"""
import os
import boto
import numpy as np
import pandas as pd
try:
    import fastparquet as fpq
except ImportError:
    print('Fastparquet is only available for Python 3.')

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

def gen_pd_dataframe(col_len=int(1e7)):
    """Generate a large-ish pandas DataFrame.

    This function generates a pandas DataFrame with two columns, 'ints' and 'floats'. The two
    columns are populated with random integers and random floats, respectively. The integers are
    random integers from the 'discrete uniform' distribution in the 'half-open' interval [0, 1000).
    The floats are sampled from a univariate 'normal' (Gaussian) distribution of mean 0 and variance
    1. Both columns are of lenght N, which is a specified by a kwarg N (default -> int(1e7)).

    Keyword arguments(s):
    N -- length of the columns in the DataFrame

    Output(s):
    df -- pandas DataFrame with two columns: 'ints' and 'floats'
    """
    # Build the DataFrame
    dataframe = pd.DataFrame({'ints': np.random.randint(0, 1000, size=col_len),
                       'floats': np.random.randn(col_len)})
    # return the DataFrame
    return dataframe

def write_df_to_parquet(dataframe, filename='test', cmpr='UNCOMPRESSED'):
    """Write a pandas DataFrame to Parquet file.

    Positional arguments(s):
    dataframe -- pandas DataFrame to be converted to Parquet file

    Keywork argument(s):
    filename -- name of file to be written without extension (default -> 'test')
    cmpr     -- type of compression to be used (default -> 'UNCOMPRESSED')

    Output(s):
    none
    """
    # write data
    fpq.write(filename + '.parquet', dataframe, compression=cmpr)
