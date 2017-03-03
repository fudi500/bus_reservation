from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.client_panel_view, name='client_panel_name'),
    url(r'^panel/$', views.panel_view, name='panel'),
    url(r'^panel/edit_vehicle/(?P<pk>[0-9]+)/$', views.edit_vehicle_view, name='edit_vehicle'),
    url(r'^panel/new/$', views.new_vehicle_view, name='new_vehicle_name'),
    url('^panel/(?P<pk>\d+)/delete/$', views.delete_vehicle_view, name='delete_vehicle_name'),

    url(r'^newreservation/(?P<pk>[0-9]+)/$', views.reservation_view, name='newreservation_name'),
    url(r'^newreservation/details(?P<pk>[0-9]+)/$', views.reservation_view, name='details'),
]
