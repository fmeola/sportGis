from django.conf.urls import url
from django.contrib.gis import admin

from . import views

urlpatterns = [
    # ex: /twitter/
    url(r'^$', views.compare, name='index'),
    url(r'^searchText/$', views.searchText, name='searchText'),
    url(r'^download_csv/$', views.download_csv, name='download_csv'),
    url(r'^admin/', admin.site.urls)
]