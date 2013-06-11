from django.db import models

class Task(models.Model):
    name = models.CharField(max_length=255)
    is_open = models.BooleanField(default=True)

    def __unicode__(self):
        return self.name

    def get_open_subtasks(self):
        return self.subtask_set.filter(is_open=True)

class SubTask(models.Model):
    task = models.ForeignKey(Task)
    name = models.CharField(max_length=255)
    is_open = models.BooleanField(default=True)

    def __unicode__(self):
        return self.name
