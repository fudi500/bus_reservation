from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.panel, name='panel'),
    url(r'^vehicle/(?P<pk>[0-9]+)/$', views.edit_vehicle, name='edit_vehicle'),
]


