# -*- coding: utf-8 -*-
from django.http import HttpResponse, Http404
from django.shortcuts import render_to_response
from django.template import RequestContext

from tej_django.tasks.models import Task

def index(request):
    tasks = Task.objects.all()

    return render_to_response('task_index.html',
                {'tasks': tasks},
                context_instance=RequestContext(request)
           )

def detail(request, task_id):
    try:
        task = Task.objects.get(pk=task_id)
    except Task.DoesNotExist:
        raise Http404

    return render_to_response('task_detail.html',
                {'task': task},
                context_instance=RequestContext(request)
           )
