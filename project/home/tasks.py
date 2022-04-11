import logging

from celery import shared_task
from djocker.celery import app
from home.models import BackendLog

logger = logging.getLogger(__name__)


@app.task
def run_task(argument):
    BackendLog.objects.create(message=str(argument))
    logger.info("Getting at the task with {}".format(argument))
    return argument


@shared_task
def unimportant_result():
    ...
