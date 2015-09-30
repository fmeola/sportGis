from django.shortcuts import render
from twython import Twython
# Create your views here.

from django.http import HttpResponse

APP_KEY = 'lXx9pK9CsmCtjDcP5t0nrLD82'
APP_SECRET = 'nNeixWCJ4BdpAPxM0V9XB1IqFqKMjBAxq1TyyK0vhfpgK8NS75'

twitter = Twython(APP_KEY, APP_SECRET, oauth_version=2)
ACCESS_TOKEN = twitter.obtain_access_token()

def index(request):
    text = "ITBA"
    return render(request, 'twitter.html', {'tweets' : getTweets(text), 'text' : text})

def searchText(request):
    if request.method == 'POST':
        text = request.POST.get('textfield', None)
        return render(request, 'twitter.html', {'tweets' : getTweets(text), 'text' : text})

def getTweets(text):
    twitter = Twython(APP_KEY, access_token=ACCESS_TOKEN)
    results = twitter.search(q=text, count='100', geocode='-34.5965096,-58.3671446,20km')
    #print(results['statuses'].__len__())
    filtered = list()
    for result in results['statuses']:
        if result.get('geo'):
            if result.get('geo').get('type') == 'Point':
                filtered.append(result)
    return filtered
