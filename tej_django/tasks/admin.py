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

    list_display = ('label','is_done','is_urgent')
    list_editable = ('is_done',)

    list_filter = ['is_done',]
    search_fields = ['label',]


admin.site.register(Task, TaskAdmin)
