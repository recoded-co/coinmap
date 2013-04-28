function coinmap() {

  var tileOSM = L.tileLayer('http://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: 'Data by <a href="http://openstreetmap.org">OpenStreetMap</a>, under <a href="http://creativecommons.org/licenses/by-sa/3.0">CC BY SA</a>.',
    maxZoom: 18
  });

  var tileToner = L.tileLayer('http://{s}.tile.stamen.com/toner/{z}/{x}/{y}.png', {
    attribution: 'Map tiles by <a href="http://stamen.com">Stamen Design</a>, under <a href="http://creativecommons.org/licenses/by/3.0">CC BY 3.0</a>. Data by <a href="http://openstreetmap.org">OpenStreetMap</a>, under <a href="http://creativecommons.org/licenses/by-sa/3.0">CC BY SA</a>.',
    maxZoom: 18
  });

  var tileMapQuest = L.tileLayer('http://{s}.mqcdn.com/tiles/1.0.0/map/{z}/{x}/{y}.png', {
    subdomains: ['otile1','otile2','otile3','otile4'],
    attribution: 'Map tiles by <a href="http://open.mapquestapi.com/">MapQuest</a>. Data by <a href="http://openstreetmap.org">OpenStreetMap</a>, under <a href="http://creativecommons.org/licenses/by-sa/3.0">CC BY SA</a>.',
    maxZoom: 18
  });

  var tileMapQuestAerial = L.tileLayer('http://{s}.mqcdn.com/tiles/1.0.0/sat/{z}/{x}/{y}.png', {
    subdomains: ['otile1','otile2','otile3','otile4'],
    attribution: 'Portions Courtesy NASA/JPL-Caltech and U.S. Depart. of Agriculture, Farm Service Agency. Data by <a href="http://openstreetmap.org">OpenStreetMap</a>, under <a href="http://creativecommons.org/licenses/by-sa/3.0">CC BY SA</a>.',
    maxZoom: 18
  });


  var map = L.map('map', { zoom: 3, layers: [tileOSM] });

  L.control.layers({
    "OpenStreetMap": tileOSM,
    "MapQuest Open": tileMapQuest,
    "MapQuest Open Aerial": tileMapQuestAerial,
    "Toner": tileToner,
  }).addTo(map);

  var markers = new L.MarkerClusterGroup({showCoverageOnHover: false, maxClusterRadius: 32});

  coinmap_populate(markers);

  map.addLayer(markers);

/*  map.locate({setView: true, maxZoom: 6}); */
}
