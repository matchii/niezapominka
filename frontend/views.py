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

def task_actions(request):
    if request.POST:
        task_id = request.POST['task_id']
        if request.POST and request.POST['new_subtask_name']:
            (Task.objects.get(id=task_id).subtask_set
                .create(name=request.POST['new_subtask_name'])
                .save()
            )
        elif 'delete_task' in request.POST:
            get_object_or_404(Task, id=task_id).delete()
        elif 'cross_out_task' in request.POST:
            Task.objects.get(id=task_id).cross_out()
        elif 'revive_task' in request.POST:
            task = get_object_or_404(Task, id=task_id)
            task.is_open = True
            task.save()
    return HttpResponseRedirect(reverse("frontend.views.index"))

def subtask_action(request):
    result = { 'success': False }
    if request.method == u'GET':
        GET = request.GET
        if GET.has_key(u'id') and GET.has_key(u'action'):
            (globals()[GET['action']])(GET['id'])
            result = { 'success': True }
    json = simplejson.dumps(result)
    return HttpResponse(json, mimetype='application/json')

def do_cross_subtask(pk):
    task = SubTask.objects.get(id=pk)
    task.is_open = False
    task.save()

def do_revive_subtask(pk):
    task = SubTask.objects.get(id=pk)
    task.is_open = True
    task.save()

def do_delete_subtask(pk):
    SubTask.objects.get(id=pk).delete()
