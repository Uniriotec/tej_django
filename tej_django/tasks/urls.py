from django.conf.urls import patterns, url

from tej_django.tasks import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^(?P<task_id>\d+)/$', views.detail, name='detail'),
    url(r'^(?P<task_id>\d+)/edit/$', views.edit, name='edit'),
)
