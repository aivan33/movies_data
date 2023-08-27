# I don't have gCloud free trial so I can't really use this script
# but I would've implemented something similar if I had

from google.cloud import storage
import os

def download_data(bucket_name, blob_name, destination_file_name):
    """ Downloads a blob from a gCloud bucket. """
    client = storage.Client()
    bucket = client.bucket(bucket_name)
    blob = bucket.blob(blob_name)

    blob.download_to_filename(destination_file_name)

    print(f"Downloaded {blob_name} to {destination_file_name}")

if __name__ == "__main__":
    bucket_name = ""
    blob_name = ""
    destination_file_name = ""

    download_data(bucket_name, blob_name, destination_file_name)
    