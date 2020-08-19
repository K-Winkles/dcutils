# Common utilities for data center functions

1. copy_batch
    Indicate parent folder and this script will copy all files under that parent folder from a source bucket to a destination bucket.

2. newly_upladed_blobs
    This script will return a list of blobs that have have been newly uploaded. I.e. blobs that are not present in the target bucket will be marked newly uploaded.