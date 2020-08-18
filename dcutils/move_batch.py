import datetime
from google.cloud import storage
from .move import mv_blob
from tenacity import retry

@retry
def mv_batch():
    blobs = STORAGE_CLIENT.list_blobs(SRC_BUCKET)
    for blob in blobs:
        try:
            print('currently checking {}'.format(blob.name))
            folders = blob.name.split('/')
            if folders[0] == 'datasets':
                print('moving {}'.format(blob.name))
                mv_blob(blob.name, DEST_BLOB + '/' + blob.name, SRC_BUCKET, DEST_BUCKET)
        except Exception as e:
            print('Error: {}'.format(e))