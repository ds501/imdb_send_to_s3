import os
import boto
from boto.s3.key import Key
from boto.s3.connection import OrdinaryCallingFormat
from urllib.request import urlopen
import logging

log = logging.getLogger()
log.setLevel(logging.DEBUG)

log.debug('Initiating sending imdb to s3')

def adtr_imdb_send_to_s3(event, context):
    try:
        upload_status = 'success'
        connection = boto.connect_s3(calling_format=OrdinaryCallingFormat())
        log.debug('connection defined')
        bucket_name = os.environ['bucket_name']
        bucket = connection.get_bucket(bucket_name)
        log.debug('got bucket')
        file_obj = Key(bucket)
        file_obj.key = event['dataset_name']
        fp = urlopen(event['url'])
        log.debug('got url from events')
        result = file_obj.set_contents_from_string(fp.read())
        log.debug('put object in s3')
    except Exception:
        upload_status = 'fail'
    finally:
        return log.debug(upload_status)