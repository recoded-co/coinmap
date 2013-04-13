function coinmap() {
  var map = L.map('map').setView([0, 0], 3);

  L.tileLayer('http://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: 'Map data &copy; <a href="http://openstreetmap.org">OpenStreetMap</a> contributors',
    maxZoom: 18
  }).addTo(map);

  map.locate({setView: true, maxZoom: 6});

  coinmap_populate(map);
}
