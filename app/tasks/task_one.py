from . import celery
import datetime

@celery.task
def one():
    return "task one run at %s"%datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")