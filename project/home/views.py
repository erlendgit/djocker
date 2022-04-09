from django.http import JsonResponse

from home.models import BackendLog


def index(request):
    from .tasks import run_task
    response = run_task.delay("Hi!")
    return JsonResponse({"msg": "Home is where your heart is.",
                         "response": response.get(timeout=1, interval=1)}, safe=False)


def result(request):
    return JsonResponse([(r.created_at, r.message) for r in BackendLog.objects.order_by('-created_at').all()], safe=False)
