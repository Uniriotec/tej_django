# -*- coding: utf-8 -*-
from django.contrib import admin
from tej_django.tasks.models import Task

class TaskAdmin(admin.ModelAdmin):
    fieldsets = [
           ('General',  {
                'fields': ['label',]
                }
           ),
           ('Status',  {
                'fields': ['is_done',]
                }
           )
        ]

    list_display = ('label','is_done')


admin.site.register(Task, TaskAdmin)
