from django.http import JsonResponse

from home.models import BackendLog


def index(request):
    from .tasks import run_task
    run_task.delay("Hi!")
    return JsonResponse({"msg": "Home is where your heart is."})


def result(request):
    return JsonResponse([(r.created_at, r.message) for r in BackendLog.objects.all()], safe=False)
