from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^', views.juego_list),
    url(r'juego/(?P<pk>[0-9]+)/$', views.listado_categoria, name='cat'),
]


