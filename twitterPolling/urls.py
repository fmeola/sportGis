from django.conf.urls import url
from django.contrib.gis import admin

from . import views

urlpatterns = [
    # ex: /twitter/
    url(r'^$', views.index, name='index'),
    url(r'^searchText/$', views.searchText, name='searchText'),
    url(r'^download_csv/$', views.download_csv, name='download_csv'),
    url(r'^admin/', admin.site.urls),
    url(r'^api/request_tweet', views.compare, name='request_tweet')
]