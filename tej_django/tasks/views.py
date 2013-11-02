# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response, get_object_or_404, redirect
from django.template import RequestContext

from tej_django.tasks.models import Task

def index(request):
    tasks = Task.objects.all()

    return render_to_response('task_index.html',
                {'tasks': tasks},
                context_instance=RequestContext(request)
           )

def detail(request, task_id):
    task = get_object_or_404(Task,pk=task_id)

    return render_to_response('task_detail.html',
                {'task': task},
                context_instance=RequestContext(request)
           )

def edit(request, task_id):
    task = get_object_or_404(Task,pk=task_id)

    if request.method == 'POST':
        is_done = request.POST.get('is_done',False)
        task.is_done = is_done
        task.save()

    return redirect('tasks:detail',task_id=task_id)
