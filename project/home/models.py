from django.db import models


class BackendLog(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    message = models.TextField(null=True)
