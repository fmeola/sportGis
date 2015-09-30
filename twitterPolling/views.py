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
    results = twitter.search(q='ITBA')
    filtered = list()
    for result in results['statuses']:
        if result.get('coordinates'):
            filtered.append(result)
#     if results.get('statuses'):
#         for result in results['statuses']:
#             print (result['coordinates'])
#     twits = twitter.cursor(twitter.search , q='OrgulloItba')
#     for t in twits:
#         print (t['coordinates'])
#     print(twits)
    return render(request, 'index.html', {'tweets' : filtered})
    