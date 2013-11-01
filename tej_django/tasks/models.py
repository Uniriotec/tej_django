# -*- coding: utf-8 -*-
from django.db import models

class Task(models.Model):
    """
    Model que é responsavel pelas Tasks
    """
    label = models.CharField("Label", max_length=250)

    is_done = models.BooleanField("Is Done?", default=False)

    def __unicode__(self):
        return "%s - %s" % (self.label, self.is_done)