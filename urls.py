from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^tasks/add_task/$', 'frontend.views.add_task', name='add_task'),
    url(r'^tasks/delete_task/$', 'frontend.views.delete_task', name='delete_task'),
    url(r'^tasks/delete_subtask/$', 'frontend.views.delete_subtask', name='delete_subtask'),
    url(r'^tasks/$', 'frontend.views.index', name='index'),
    url(r'^.*$', 'frontend.views.index', name='default'),
    # url(r'^niezapominka/', include('niezapominka.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
