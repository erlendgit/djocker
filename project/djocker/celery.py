import os
from celery import Celery
from django.conf import settings


def create_application():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'djocker.settings')
    application = Celery('tasks', broker=settings.CELERY_BROKER_URL)
    application.config_from_object('django.conf:settings', namespace='CELERY')

    # Looks up for task modules in Django applications and loads them
    application.autodiscover_tasks()

    return application


app = create_application()
