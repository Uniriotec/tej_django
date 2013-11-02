# -*- coding: utf-8 -*-
from django.http import HttpResponse

def index(request):
    return HttpResponse("This is DJAAANNGOOO!!.")

def detail(request, task_id):
    return HttpResponse("Essa eh a task %s." % task_id)
