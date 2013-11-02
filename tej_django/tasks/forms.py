# -*- coding: utf-8 -*-
from django import forms

from tej_django.tasks.models import Task

class TaskForm(forms.ModelForm):
    "Form do modelo de Task"

    class Meta:
        model = Task

