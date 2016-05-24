from django.db import models


class Task(models.Model):
    session_key = models.CharField(max_length=128, null=True)
    title = models.CharField(max_length=64)
    text = models.CharField(max_length=256)

    def __unicode__(self):
        return '%s'.format(self.title)
