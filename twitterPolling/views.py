from django.shortcuts import render
from twython import Twython
# Create your views here.

from django.http import HttpResponse

APP_KEY = 'lXx9pK9CsmCtjDcP5t0nrLD82'
APP_SECRET = 'nNeixWCJ4BdpAPxM0V9XB1IqFqKMjBAxq1TyyK0vhfpgK8NS75'

twitter = Twython(APP_KEY, APP_SECRET, oauth_version=2)
ACCESS_TOKEN = twitter.obtain_access_token()

MAX_QUERYS = 10

def index(request):
    text = "ITBA"
    return render(request, 'twitter.html', {'tweets' : getTweets(text), 'text' : text})

def searchText(request):
    if request.method == 'POST':
        text = request.POST.get('textfield', None)
        return render(request, 'twitter.html', {'tweets' : getTweets(text), 'text' : text})

def getTweets(text):
    twitter = Twython(APP_KEY, access_token=ACCESS_TOKEN)
    filtered = list()
    filtered_no_duplicates = list()
    since_id = 0
#     Voy a hacer MAX_QUERYS al search de twitter
    for i in range(1,MAX_QUERYS):
        if since_id == 0:
            results = twitter.search(q=text, count='100',result_type='recent', geocode='-34.5965096,-58.3671446,20km')
        else:
            results = twitter.search(q=text, count='100',result_type='recent',max_id=since_id, geocode='-34.5965096,-58.3671446,20km')
        for result in results['statuses']:
#           Lo tengo que hacer manualmente por que la api no me esta devolviendo el since_id
            if (result['id'] < since_id or since_id == 0):
                since_id = result['id']
            if result.get('geo'):
                if result.get('geo').get('type') == 'Point':
                    filtered.append(result)
            for twit in filtered:
                if twit not in filtered_no_duplicates:
                    filtered_no_duplicates.append(twit)
    return filtered_no_duplicates
