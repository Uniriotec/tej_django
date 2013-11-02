# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response, get_object_or_404, redirect
from django.template import RequestContext

from tej_django.tasks.models import Task
from tej_django.tasks.forms import TaskForm


def index(request):
    tasks = Task.objects.all()

    return render_to_response('task_index.html',
                {'tasks': tasks},
                context_instance=RequestContext(request)
           )

def detail(request, task_id):
    task = get_object_or_404(Task,pk=task_id)
    form = TaskForm(instance=task)

    return render_to_response('task_detail.html',
                {
                'task': task,
                'form':form
                },
                context_instance=RequestContext(request)
           )

def edit(request, task_id):
    task = get_object_or_404(Task,pk=task_id)

    if request.method == 'POST':
        form = TaskForm(request.POST,instance=task)

        if form.is_valid():
            form.save()

        else:
            return render_to_response('task_detail.html',
                    {
                        'task': task,
                        'form':form
                    },
                    context_instance=RequestContext(request)
               )

    return redirect('tasks:detail',task_id=task_id)
