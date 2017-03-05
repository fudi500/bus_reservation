from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.client_panel_view, name='client_panel_name'),


    url(r'^reservation/(?P<pk>[0-9]+)/$', views.reservation_view, name='newreservation_name'),
    url(r'^reservation/new/(?P<pk>[0-9]+)/$', views.reservation_view, name='details'),
    url(r'^reservation/details/(?P<pk>[0-9]+)/(?P<bus>[0-9]+)/$', views.reservation_details_view, name='reservation_details'),

    url(r'^panel/$', views.panel_view, name='panel'),

    url(r'^panel/bus/edit/(?P<pk>[0-9]+)/$', views.edit_vehicle_view, name='edit_vehicle'),
    url(r'^panel/bus/details/(?P<pk>[0-9]+)/$', views.vehicle_details_view, name='vehicle_details'),
    url(r'^panel/bus/new/$', views.new_vehicle_view, name='new_vehicle_name'),
    url('^panel/delete/(?P<pk>\d+)/$', views.delete_vehicle_view, name='delete_vehicle_name'),


    url(r'^panel/driver/new$', views.new_driver_view, name='driver'),
    url(r'^panel/driver/edit/(?P<pk>[0-9]+)/$', views.edit_driver_view, name='edit_driver'),
    url(r'^panel/driver/delete/(?P<pk>[0-9]+)/$', views.delete_driver_view, name='delete_driver'),
]
