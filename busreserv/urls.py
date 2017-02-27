from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^panel/$', views.panel_view, name='panel'),
    url(r'^panel/edit_vehicle/(?P<pk>[0-9]+)/$', views.edit_vehicle_view, name='edit_vehicle'),
    url(r'^panel/new/$', views.new_vehicle_view, name='new_vehicle_name'),   
]


