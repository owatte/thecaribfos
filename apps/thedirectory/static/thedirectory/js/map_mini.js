var map = new L.map('map',{fullscreenControl: false,
                            scrollWheelZoom: false,
                            fullscreenControlOptions:{position: 'topleft'}
                          }).setView([19.031, -73.048], 4);
L.tileLayer('http://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    maxZoom: 18,
    attribution: 'Map data &copy; <a href="http://openstreetmap.org">OpenStreetMap</a> contributors, ' +
        '<a href="http://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>'
}).addTo(map);

var marker = null;
var found;


function geosearch(address)
{
      found = false;
      if (marker !== null) {
          map.removeLayer(marker);
      }

     $.ajax({
     async: false,
     url:'//nominatim.openstreetmap.org/search/?format=json&q=' + address,
     dataType: "json",
     success: function(data){
        if (!data.length){
            found = 0;
        } else {

            $("#id_lat").attr("value", data[0].lat);
            $("#id_lon").attr("value", data[0].lon);
            marker = L.marker([data[0].lat, data[0].lon]).addTo(map);
            map.on(map.setView(([data[0].lat, data[0].lon]), 13));
            found = 1;
        }
     },
     error: function(e){
        alert('Error during Nomatim query, ask the administrator');
        found = 2;
     }
    })
}


function onMapClick(e) {

    if (marker !== null) {
        map.removeLayer(marker);
    }
    $("#id_lat").attr("value", e.latlng.lat);
    $("#id_lon").attr("value", e.latlng.lng);
    marker = L.marker([e.latlng.lat, e.latlng.lng]).addTo(map);

}
map.on('click', onMapClick);

$("#geosearch-button").click(function(){
    var country = $("#id_country").val();
    if (country){
        var country_name = ", " + $("#id_country option[value=" + country + "]").text();
    } else {
        var country_name = "";
    }
    var address = "";
    address = $("#id_address").val() + country_name;
    address = address.replace('\n', ',');
    var ret = geosearch(encodeURIComponent(address));
    if (found == 0){
        ret = geosearch(encodeURIComponent(country_name));
        if (found == 0)
            alert('No correspondance found, try do indicate geolocation by clicking on the map');
    }
})
