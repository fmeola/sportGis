from django.contrib.gis import admin
from twitterPolling.models import States

admin.site.register(States, admin.GeoModelAdmin)