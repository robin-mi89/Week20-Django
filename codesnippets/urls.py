from django.conf.urls import url

from . import views

app_name = 'codesnippets'
urlpatterns = [
    url(r'', views.CodeListView.as_view(), name='index'),

    url(r'^detail/(?P<pk>[0-9]+)/$', 
        views.CodeDetailView.as_view(), name='detail'),

    url(r'^add/$', views.add, name='add'),
]
