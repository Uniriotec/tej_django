from django.db import models

class Task(models.Model):

    label = models.CharField("Label", max_length=250)

    def __unicode__(self):
        return self.content
