from django.shortcuts import render
from twython import Twython
# Create your views here.

from django.http import HttpResponse

APP_KEY = 'lXx9pK9CsmCtjDcP5t0nrLD82'
APP_SECRET = 'nNeixWCJ4BdpAPxM0V9XB1IqFqKMjBAxq1TyyK0vhfpgK8NS75'

twitter = Twython(APP_KEY, APP_SECRET, oauth_version=2)
ACCESS_TOKEN = twitter.obtain_access_token()

def index(request):
    twitter = Twython(APP_KEY, access_token=ACCESS_TOKEN)
    twits = twitter.search(q='python')
    for t in twits:
        print(t.place)
        print(t.place.bounding_box)
    print(twits)
    return render(request, 'index.html', {'twits' : twits})
    