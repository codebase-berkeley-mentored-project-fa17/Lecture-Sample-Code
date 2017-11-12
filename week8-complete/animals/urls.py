from django.conf.urls import url
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    url(r'^getage', views.get_info, name='get_info'),
    url(r'^killanimals', views.kill_animals, name='kill_animals'),
    url(r'^login', auth_views.login, name='login'),
    url(r'^comment', views.comment, name='comment'),
]