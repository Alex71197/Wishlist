from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name = 'index'),
    url(r'^create/$', views.create, name = 'create'),
    url(r'^create_item/$', views.create_item, name = 'create_item'),
    url(r'^home/$', views.home, name = 'home'),
    url(r'^show_item/(?P<id>\d+)/$', views.show_item, name = 'show_item'),
    url(r'^join_item/(?P<id>\d+)/$', views.join_item, name = 'join_item'),
    url(r'^remove_item/(?P<id>\d+)/$', views.remove_item, name = 'remove_item'),
    url(r'^delete_item/(?P<id>\d+)/$', views.delete_item, name = 'delete_item')
]
