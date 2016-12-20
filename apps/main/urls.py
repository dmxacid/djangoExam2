from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name = 'index'),
    url(r'^register$', views.register, name = 'register'),
    url(r'^login$', views.login, name = 'login'),
    url(r'^appointments$', views.appointments, name = 'appointments'),
    url(r'^logout$', views.logout, name = 'logout'),
    url(r'^addAppointment$', views.addAppointment, name = 'addAppointment'),
    url(r'^editAppointment$', views.editAppointment, name = 'editAppointment'),
    url(r'^delete/(?P<appointments_id>\d*)$', views.delete, name = 'delete'),
    url(r'^edit/(?P<appointments_id>\d*)$', views.edit, name = 'edit'),
]
