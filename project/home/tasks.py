from celery import shared_task
from djocker.celery import app
from home.models import BackendLog


@app.task
def run_task(argument):
    BackendLog.objects.create(message=str(argument))
    return argument


@shared_task
def unimportant_result():
    ...
