# -*- coding: utf-8 -*-
from django import forms

from tej_django.tasks.models import Task

class TaskForm(forms.ModelForm):
    "Form do modelo de Task"

    class Meta:
        model = Task


    def clean_label(self):
        data = self.cleaned_data['label']
        if data.lower().count("bobeira") > 0:
            raise forms.ValidationError("Sem bobeira nas Tasks")

        return data
