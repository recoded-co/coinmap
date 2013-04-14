function coinmap() {

  var tileOSM = L.tileLayer('http://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: 'Map data by <a href="http://openstreetmap.org">OpenStreetMap</a>, under <a href="http://creativecommons.org/licenses/by-sa/3.0">CC BY SA</a>.',
    maxZoom: 18
  });

  var tileToner = L.tileLayer('http://{s}.tile.stamen.com/toner/{z}/{x}/{y}.png', {
    attribution: 'Map tiles by <a href="http://stamen.com">Stamen Design</a>, under <a href="http://creativecommons.org/licenses/by/3.0">CC BY 3.0</a>. Data by <a href="http://openstreetmap.org">OpenStreetMap</a>, under <a href="http://creativecommons.org/licenses/by-sa/3.0">CC BY SA</a>.',
    maxZoom: 18
  });

  var tileMapQuest = L.tileLayer('http://{s}.mqcdn.com/tiles/1.0.0/osm/{z}/{x}/{y}.png', {
    subdomains: ['otile1','otile2','otile3','otile4'],
    attribution: 'Map tiles by <a href="http://open.mapquestapi.com/">MapQuest</a>. Data by <a href="http://openstreetmap.org">OpenStreetMap</a>, under <a href="http://creativecommons.org/licenses/by-sa/3.0">CC BY SA</a>.',
    maxZoom: 18
  });

  var map = L.map('map', { zoom: 3, layers: [tileOSM] });

  L.control.layers({
    "OpenStreetMap": tileOSM,
    "MapQuest Open": tileMapQuest,
    "Toner": tileToner,
  }).addTo(map);

  map.locate({setView: true, maxZoom: 6});

  coinmap_populate(map);
}
