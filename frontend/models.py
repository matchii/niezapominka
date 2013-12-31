# -*- coding: utf-8 -*-
from django.db import models
import datetime

class Task(models.Model):
    name = models.CharField(max_length=255)
    priority = models.IntegerField(default=0)
    is_open = models.BooleanField(default=True)
    added_at = models.DateTimeField(default=datetime.datetime.now())

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

    @property
    def age(self):
        """ liczba dni od utworzenia zadania """
        return max((datetime.datetime.now() - self.added_at).days, 0)

    @property
    def color(self):
        """ kod koloru zależny od wieku zadania: im starsze, tym intensywniejsza czerwień """
        x = hex(255 - min(self.age, 255))[2:].zfill(2)
        return '#FF%s%s' % (x, x)

class SubTask(models.Model):
    id = models.AutoField(primary_key=True)
    task = models.ForeignKey(Task)
    name = models.CharField(max_length=255)
    is_open = models.BooleanField(default=True)

    def __unicode__(self):
        return self.name
