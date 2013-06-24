from django.core.context_processors import csrf
from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.template import Context, RequestContext, loader
from django.utils import simplejson
from frontend.models import Task, SubTask

# Create your views here.
def index(request):
    return render_to_response("tasks/list.html", {'lista': Task.objects.order_by('-priority', 'id').all()}, RequestContext(request))

def add_task(request):
    if request.POST and request.POST['new_task_name']:
        Task(
            name=request.POST['new_task_name'],
            priority=request.POST['priority']
        ).save()
    return HttpResponseRedirect(reverse("frontend.views.index"))

def action(request):
    result = { 'success': False }
    if request.method == u'GET':
        GET = request.GET
        if GET.has_key(u'id') and GET.has_key(u'action'):
            r = (globals()[GET['action']])(GET)
            result = { 'success': True }
            if isinstance(r, dict):
                result.update(r)
    json = simplejson.dumps(result)
    return HttpResponse(json, mimetype='application/json')

def delete_task(GET):
    get_object_or_404(Task, id=GET['id']).delete()

def cross_out_task(GET):
    Task.objects.get(id=GET['id']).cross_out()

def revive_task(GET):
    task = Task.objects.get(id=GET['id'])
    task.is_open = True
    task.save()

def add_subtask(GET):
    sub = Task.objects.get(id=GET['id']).subtask_set.create(name=GET['name'])
    sub.save()
    return { 'id': sub.id }

def cross_out_subtask(GET):
    task = SubTask.objects.get(id=GET['id'])
    task.is_open = False
    task.save()

def revive_subtask(GET):
    task = SubTask.objects.get(id=GET['id'])
    task.is_open = True
    task.save()

def delete_subtask(GET):
    SubTask.objects.get(id=GET['id']).delete()

def set_task_priority(GET):
    task = Task.objects.get(id=GET['id'])
    task.priority = GET['priority']
    task.save()
