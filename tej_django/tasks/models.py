from django.db import models

class Task(models.Model):
    """
    Model que é responsavel pelas Tasks
    """
    label = models.CharField("Label", max_length=250)

    def __unicode__(self):
        return self.label
