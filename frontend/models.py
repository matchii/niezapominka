# -*- coding: utf-8 -*-
from django.db import models

class Task(models.Model):
    name = models.CharField(max_length=255)
    priority = models.IntegerField(default=0)
    is_open = models.BooleanField(default=True)

    def __unicode__(self):
        return self.name

    def get_open_subtasks(self):
        return self.subtask_set.filter(is_open=True)

    def delete(self):
        self.subtask_set.all().delete()
        super(Task, self).delete()

    def cross_out(self):
        """ skreśla zadanie """
        self.is_open=False
        self.save()

    def as_dict(self):
        return { 'name': self.name }

class SubTask(models.Model):
    id = models.AutoField(primary_key=True)
    task = models.ForeignKey(Task)
    name = models.CharField(max_length=255)
    is_open = models.BooleanField(default=True)

    def __unicode__(self):
        return self.name
