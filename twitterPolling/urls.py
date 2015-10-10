from django.conf.urls import url

from . import views

urlpatterns = [
    # ex: /twitter/
    url(r'^$', views.index, name='index'),
    url(r'^searchText/$', views.searchText, name='searchText'),
    url(r'^download_csv/$', views.download_csv, name='download_csv')
]