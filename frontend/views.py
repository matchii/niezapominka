from django.core.context_processors import csrf
from django.shortcuts import render_to_response, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.template import Context, loader
from frontend.models import Task, SubTask

# Create your views here.
def index(request):
    return render_to_response("tasks/index.html", get_list(request))

def add_task(request):
    if request.POST:
        Task(name=request.POST['new_task_name']).save()
    return HttpResponseRedirect(reverse("frontend.views.index"))

def delete_task(request):
    if (request.POST):
        if 'delete_task' in request.POST:
            Task.objects.get(id=request.POST['task_id']).delete()
        elif 'add_subtask' in request.POST:
            Task.objects.get(id=request.POST['task_id']).subtask_set.create(name=request.POST['new_subtask_name']).save()
    return HttpResponseRedirect(reverse("frontend.views.index"))

def delete_subtask(request):
    if (request.POST):
        SubTask.objects.get(id=request.POST['subtask_id']).delete()
    return HttpResponseRedirect(reverse("frontend.views.index"))

def get_list(request):
    c = Context({'lista': Task.objects.filter(is_open=True)})
    c.update(csrf(request))
    return c
