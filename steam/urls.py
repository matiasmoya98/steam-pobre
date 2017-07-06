from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^', views.juego_list),
    url(r'categoria/(?P<pk>[0-9]+)/$', views.categoria_list, name='cat'),
]


