from django.conf.urls import url
from . import views

urlpatterns = [
        url(r'^register/', views.register, name = 'register'),
        url(r'^test/', views.test, name = 'test'),
        url(r'^subregister/', views.submit_register, name = 'submit_register'),
        url(r'^userinfo/', views.show_user_info, name = 'userinfo'),
        url(r'^sublogin/', views.sub_login, name = 'sub_login'),
        url(r'^login/', views.show_login, name = 'show_login'),
        url(r'^getcount/', views.get_count, name = 'get_count'),
        url(r'^initial/', views.initial, name = 'initial'),
        ]
