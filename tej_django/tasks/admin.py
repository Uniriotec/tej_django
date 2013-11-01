# -*- coding: utf-8 -*-
from django.contrib import admin
from tej_django.tasks.models import Task

admin.site.register(Task, admin.ModelAdmin)
