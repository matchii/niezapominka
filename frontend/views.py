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
    if request.POST and request.POST['new_task_name']:
        Task(name=request.POST['new_task_name']).save()
    return HttpResponseRedirect(reverse("frontend.views.index"))

def task_actions(request):
    if request.POST:
        if 'delete_task' in request.POST:
            Task.objects.get(id=request.POST['task_id']).delete()
        elif 'cross_out_task' in request.POST:
            Task.objects.get(id=request.POST['task_id']).cross_out()
        elif 'revive_task' in request.POST:
            task = Task.objects.get(id=request.POST['task_id'])
            task.is_open = True
            task.save()
        elif 'add_subtask' in request.POST and request.POST['new_subtask_name']:
            Task.objects.get(id=request.POST['task_id']).subtask_set.create(name=request.POST['new_subtask_name']).save()
    return HttpResponseRedirect(reverse("frontend.views.index"))

def subtask_actions(request):
    if request.POST:
        "%s" % request.POST
        if 'delete_subtask' in request.POST:
            SubTask.objects.get(id=request.POST['subtask_id']).delete()
        elif 'cross_out_subtask' in request.POST:
            st = SubTask.objects.get(id=request.POST['subtask_id'])
            st.is_open = False
            st.save()
        elif 'revive_subtask' in request.POST:
            task = SubTask.objects.get(id=request.POST['subtask_id'])
            task.is_open = True
            task.save()
    return HttpResponseRedirect(reverse("frontend.views.index"))

def get_list(request):
    c = Context({'lista': Task.objects.all()})
    c.update(csrf(request))
    return c
