{% load i18n %}
var map = new L.map('map',{fullscreenControl: true,
                            scrollWheelZoom: false,
                            fullscreenControlOptions:{position: 'topleft'}
                          }).setView([19.031, -73.048], 6);
L.tileLayer('http://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    maxZoom: 18,
    attribution: 'Map data &copy; <a href="http://openstreetmap.org">OpenStreetMap</a> contributors, ' +
        '<a href="http://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>'
}).addTo(map);


{# comment 'put all entries geolocalizable in an array[ [marker_title, marker_lat, marker_lon, marker_popup] ]' #}
//~ var entries = [
    //~ {% for entry in object_list %}
    //~ {% if entry.lat %}[
        //~ "{{ entry.name }} ({{ entry.category }})",
        //~ {{ entry.lat }},
        //~ {{ entry.lon }},
        //~ "<b>{% if entry.web %}<a href='{{ entry.web }}'>{{ entry.name }}</a>{% else %}{{ entry.name }}{% endif %}</b><br>{{ entry.category }}<ul class='list-inline'>{% if entry.web %}<li><a href='{{ entry.web }}'><i class='fa fa-globe'></i></a></li>{% endif %}{% if entry.twitter %}<li><a href='https://twitter.com/{{ entry.twitter }}'><i class='fa fa-twitter'></i></a></li>{% endif %}{% if entry.facebook %}<li><a href='{{ entry.facebook }}'><i class='fa fa-facebook-official'></i></a></li>{% endif %}{% if entry.googleplus %}<li><a href='{{ entry.googleplus }}'><i class='fa fa-google-plus'></i></a></li>{% endif %}{% if entry.linkedin %}<li><a href='{{ entry.linkedin }}'><i class='fa fa-linkedin'></i></a></li>{% endif %}</ul>",
        //~ ],
    //~ {% endif %}
    //~ {% endfor %}
//~ ];

var markers = L.markerClusterGroup();

//~ for (var i = 0; i < entries.length; i++) {
    //~ var entry = entries[i];
    //~ var title = entry[0];
    //~ var popup = entry[3];
    //~ var marker = L.marker(new L.LatLng(entry[1], entry[2]), { title: title });
    //~ marker.bindPopup(popup);
    //~ markers.addLayer(marker);
//~ }


var entries = {"1":['toto', 1, 1],
               "3":['tata', 10, 10],
               "4":['titi', 20, 30],
               "6":['tutu', 30, 30],
               "8":['lulu', 30, 60],
               "9":['lili', 300, 50],
               "10":['lala', 20, 10],
               "42":['lolo', 42, 42]
              };

var tags_all = ["1", "3", "4", "6", "8", "9", "10", "42"];
var tag_t = ["1", "3", "4", "6"];


var tag_a = ["3", "10"];

//
var tags_layers = new Array();

//~ var mapcat52 = new MyCustomLayer(latlng);
//~ // save to layers list
//~ layers["mapcat52"] = mapcat52;
//~ ...
//~ // remove layers
//~ $.each(someObj.idsChecked,function(id, val) {
    //~ // look up layer object by id
    //~ var layerObj = layers[val];
    //~ // remove layer
    //~ map.removeLayer(layerObj);
  //~ });
//~ //

for (var i = 0; i < tags_all.length; i++) {
    var indice = tags_all[i];
    var entry = entries[indice];
    var title = entry[0];
    var marker = L.marker(new L.LatLng(entry[1], entry[2]), { title: title });
    //marker.bindPopup(popup);
    markers.addLayer(marker);
}


map.addLayer(markers);
tags_layers['all'] = markers;
map.fitBounds(markers.getBounds());

$("#show_all").click(function(event) {
    map.removeLayer(markers);
    //var markers = L.markerClusterGroup();
    for (var i = 0; i < tags_all.length; i++) {
        var indice = tags_all[i];
        var entry = entries[indice];
        var title = entry[0];
        var marker = L.marker(new L.LatLng(entry[1], entry[2]), { title: title });
        //marker.bindPopup(popup);
        markers.addLayer(marker);
    }
    map.addLayer(markers);
    map.fitBounds(markers.getBounds());
    return false;
});
$("#show_t").click(function(event) {
    map.removeLayer(markers);
    var markers_t = L.markerClusterGroup();
    var tag_t = ["1", "3", "4", "6"];
    for (var i = 0; i < tag_t.length; i++) {
        var indice = tag_t[i];
        var entry = entries[indice];
        var title = entry[0];
        var marker = L.marker(new L.LatLng(entry[1], entry[2]), { title: title });
        //marker.bindPopup(popup);
        markers_t.addLayer(marker);
    }
    map.addLayer(markers_t);
    map.fitBounds(markers_t.getBounds());
    return false;

});

$("#show_t2").click(function(event) {
    map.removeLayer(markers);
    var markers_t = L.markerClusterGroup();
    var tag_t = ["1", "3", "4", "6"];
    for (var i = 0; i < tag_t.length; i++) {
        var indice = tag_t[i];
        var entry = entries[indice];
        var title = entry[0];
        var marker = L.marker(new L.LatLng(entry[1], entry[2]), { title: title });
        //marker.bindPopup(popup);
        markers_t.addLayer(marker);
    }
    map.addLayer(markers_t);
    map.fitBounds(markers_t.getBounds());
    return false;

});

$("#show_t3").click(function(event) {
    map.clearLayers();
    //(markers);
    var markers_t = L.markerClusterGroup();
    var tag_t = ["1", "3", "4", "6"];
    for (var i = 0; i < tag_t.length; i++) {
        var indice = tag_t[i];
        var entry = entries[indice];
        var title = entry[0];
        var marker = L.marker(new L.LatLng(entry[1], entry[2]), { title: title });
        //marker.bindPopup(popup);
        markers_t.addLayer(marker);
    }
    map.addLayer(markers_t);
    map.fitBounds(markers_t.getBounds());
    return false;
});


$("#show_l").click(function(event) {
    map.removeLayer(markers);
    map.eachLayer(function (layer) {
        if (layer != L.tileLayer){
            map.removeLayer(layer);
        }
    });
    var markers_l = L.markerClusterGroup();
    var tag_l = ["8", "9", "10", "42"];
    for (var i = 0; i < tag_t.length; i++) {
        var indice = tag_l[i];
        var entry = entries[indice];
        var title = entry[0];
        var marker = L.marker(new L.LatLng(entry[1], entry[2]), { title: title });
        //marker.bindPopup(popup);
        markers_l.addLayer(marker);
    }
    map.addLayer(markers_l);
    map.fitBounds(markers_l.getBounds());
    return false;
});

$("#show_o").click(function(event) {
    map.removeLayer(markers);
    //delete markers;

    var markers = L.markerClusterGroup();
    var tag_o = ["1", "42"];
    for (var i = 0; i < tag_o.length; i++) {
        var indice = tag_t[i];
        var entry = entries[indice];
        var title = entry[0];
        var marker = L.marker(new L.LatLng(entry[1], entry[2]), { title: title });
        //marker.bindPopup(popup);
        markers.addLayer(marker);
    }

    map.addLayer(markers);
    map.fitBounds(markers.getBounds());
    return false;
});

$("#show_u").click(function(event) {
    map.removeLayer(markers);

    for (var i = 0; i < tags_layers.length; i++) {
        var layerObj = layers[i];
        map.removeLayer(layerObj);
    }


    var markers_u = L.markerClusterGroup();
    var tag_u = ["6", "8"];
    for (var i = 0; i < tag_u.length; i++) {
        var indice = tag_u[i];
        var entry = entries[indice];
        var title = entry[0];
        var marker = L.marker(new L.LatLng(entry[1], entry[2]), { title: title });
        //marker.bindPopup(popup);
        markers_u.addLayer(marker);
    }
    map.addLayer(markers_u);
    map.fitBounds(markers_u.getBounds());
    return false;

});
