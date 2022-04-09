from celery import shared_task

from home.models import BackendLog


@shared_task
def run_task(argument):
    BackendLog.objects.create(message=str(argument))
    return argument
