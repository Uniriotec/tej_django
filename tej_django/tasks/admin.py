# -*- coding: utf-8 -*-
from django.contrib import admin
from tej_django.tasks.models import Task

class TaskAdmin(admin.ModelAdmin):

    list_display = ('label',)


admin.site.register(Task, TaskAdmin)
