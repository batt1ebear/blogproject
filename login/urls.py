from django.conf.urls import url

from . import views

app_name = 'login'
urlpatterns = [
    url(r'^login$', views.auth_view, name='login'),
    url(r'^log_out$', views.log_out, name='log_out'),
]