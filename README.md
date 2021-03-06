Example Docker/Django/Celery project
===

The aim with this project was to create a django/celery project using python only from within a docker container.

Setup docker
---

My considerations about how to set up docker is documented here:

- Dockerfile
- docker-compose.project.yml
- docker-compose.yml

Create a celery app (djocker.celery)
---

```python
import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'djocker.settings')
app = Celery('Djocker task processor')
app.config_from_object('django.conf:settings', namespace='CELERY')

# Looks up for task modules in Django applications and loads them
app.autodiscover_tasks()
```

Add configuration (djocker.settings)
---

The setting names matter. 'CELERY' relates to the namespace argument.

CELERY_BROKER and CELERY_BACKEND are URL's to the redis or rabbitmq applications. See also the docker-compose.yml file in this project.

```python
import os

CELERY_BROKER_URL = os.getenv("CELERY_BROKER")
CELERY_RESULT_BACKEND = os.getenv("CELERY_BACKEND")
```

Add the celery app to settings-root (djocker.\_\_init\_\_.py)
---

In order for celery to work with django the app needs to be:

1. in this position in the project tree, relative to the settings module that you defined at DJANGO_SETTINGS_MODULE.
2. defined with this name.

I found this part confusing. The 'celery' command at deployment refers to the file where the app is created, but
still you need to import the app in this fashion. Not sure why.

```python
from .celery import app as celery_app

__all__ = ('celery_app',)
```

Use the celery app to decorate tasks (home.tasks)
---

In this way you can use Celery's full potential.

```python
from djocker.celery import app


@app.task
def run_task(argument):
    ...
```

The next method is scheduled fine, but you have no access to the result via the result backend if your task is decorated in this fashion.

```python
from celery import shared_task


@shared_task
def unimportant_result():
    ...
```