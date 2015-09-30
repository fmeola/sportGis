var mapId = 'francoroman.cif6y5apf0sufs5ktwl0j56l1'
var mapAccessToken = 'pk.eyJ1IjoiZnJhbmNvcm9tYW4iLCJhIjoiY2lmNnk1Ynl2MGxpYnRxbTV5dWQ4cHpveCJ9.0AvZR59EKIGrOwWbzkhJMw'
var map = L.map('map').setView([-34.613864, -58.444999], 12);
L.tileLayer('https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token={accessToken}', {
    attribution: 'Map data &copy; <a href="http://openstreetmap.org">OpenStreetMap</a> contributors, <a href="http://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, Imagery © <a href="http://mapbox.com">Mapbox</a>',
    maxZoom: 18,
    id: mapId,
    accessToken: mapAccessToken
}).addTo(map);