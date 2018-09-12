var map = L.map('map', 
{ crs: L.CRS.Simple, minZoom:-3, maxZoom:8 }); 
var bounds = [[0,0], [768,1000], 1]; 
var image = L.imageOverlay('etasje1.png', bounds).addTo(map); 
map.fitBounds(bounds);
var plassering = L.latLng([333, 444]);
L.marker(plassering).addTo(map).bindPopup('h4');
map.setView( [384, 500], 0);