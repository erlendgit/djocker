from django.http import JsonResponse
from django.utils.timezone import datetime

from home.models import BackendLog


def index(request):
    from .tasks import run_task
    response = run_task.delay("Hi!")
    return JsonResponse({"msg": "Home is where your heart is.",
                         "response": response.get(timeout=3, interval=.125)}, safe=False)


def result(request):
    return JsonResponse([(datetime.fromtimestamp(r.created_at.timestamp()),
                          r.message) for r in BackendLog.objects.order_by('-created_at').all()], safe=False)
