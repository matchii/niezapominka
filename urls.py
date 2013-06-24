from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('frontend.views',
    # Examples:
    url(r'^add_task/$', 'add_task', name='add_task'),
    url(r'^delete_task/$', 'action'),
    url(r'^cross_out_task/$', 'action'),
    url(r'^revive_task/$', 'action'),
    url(r'^add_subtask/$', 'action'),

    url(r'^cross_out_subtask/$', 'action'),
    url(r'^revive_subtask/$', 'action'),
    url(r'^delete_subtask/$', 'action'),

    url(r'^$', 'index', name='index'),
    url(r'^.*$', 'index', name='default'),
    # url(r'^niezapominka/', include('niezapominka.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
