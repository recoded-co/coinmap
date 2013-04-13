function coinmap() {
  var map = new OpenLayers.Map('map', {
    maxExtent: new OpenLayers.Bounds(-20037508.34,-20037508.34,20037508.34,20037508.34),
      numZoomLevels: 19,
      maxResolution: 156543.0399,
      units: 'm',
      projection: new OpenLayers.Projection("EPSG:900913"),
      displayProjection: new OpenLayers.Projection("EPSG:4326")
  });

  var layerMapnik = new OpenLayers.Layer.OSM.Mapnik("Mapnik");
  map.addLayers([layerMapnik]);

  var bitcoin = new OpenLayers.Layer.Text("Bitcoin", { location: "coinmap.txt", projection: map.displayProjection });
  map.addLayer(bitcoin);

  map.removeControl(map.controls[1]); // remove simple zoom buttons
  map.addControl(new OpenLayers.Control.PanZoomBar());

  var lonLat = new OpenLayers.LonLat(0,0).transform(map.displayProjection, map.projection);
  map.setCenter(lonLat, 0);
}
