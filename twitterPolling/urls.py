from django.conf.urls import url

from . import views

urlpatterns = [
    # ex: /twitter/
    url(r'^$', views.index, name='index'),
]