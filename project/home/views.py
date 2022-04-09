from django.http import JsonResponse
from django.shortcuts import render

def index(request):
    return JsonResponse({"msg": "Home is where your heart is."})