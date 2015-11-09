from django.conf.urls import url
from . import views

urlpatterns = [
        url(r'^$', views.register, name = 'index'),
        url(r'^register/', views.register, name = 'register'),
        url(r'^subregister/', views.submit_register, name = 'submit_register'),
        ]
