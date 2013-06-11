from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^add_task/$', 'frontend.views.add_task', name='add_task'),
    url(r'^task_actions/$', 'frontend.views.task_actions', name='task_actions'),
    url(r'^subtask_actions/$', 'frontend.views.subtask_actions', name='subtask_actions'),
    url(r'^$', 'frontend.views.index', name='index'),
    url(r'^.*$', 'frontend.views.index', name='default'),
    # url(r'^niezapominka/', include('niezapominka.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
