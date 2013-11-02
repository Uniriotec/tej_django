# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.template import RequestContext, loader

from tej_django.tasks.models import Task

def index(request):
    tasks = Task.objects.all()

    template = loader.get_template('task_index.html')
    context = RequestContext(request, {
        'tasks': tasks,
    })
    return HttpResponse(template.render(context))

def detail(request, task_id):
    return HttpResponse("Essa eh a task %s." % task_id)
