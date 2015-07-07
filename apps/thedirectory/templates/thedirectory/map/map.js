{% load i18n %}
{% load tag_cloud %}
{% load slug2js %}
var map = new L.map('map',{fullscreenControl: true,
                            scrollWheelZoom: false,
                            fullscreenControlOptions:{position: 'topleft'}
                          }).setView([19.031, -73.048], 6);


L.tileLayer('http://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    maxZoom: 18,
    attribution: 'Map data &copy; <a href="http://openstreetmap.org">OpenStreetMap</a> contributors, ' +
        '<a href="http://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>'
}).addTo(map);

map.attributionControl.setPosition("bottomleft");
map.attributionControl.setPrefix('<a href="http://www.ipeos.com">powered by IPEOS</a>');

var sidebar = L.control.sidebar('sidebar').addTo(map);
//~
var markers = L.markerClusterGroup();
var entries = {
    {% for entry in object_list %}
    {% if entry.lat %}"{{ entry.pk }}":['{{ entry.name }}', {{ entry.lat }}, {{ entry.lon }}, "<h3>{{ entry.name }}</h3>{% if entry.tags %}<ul class=\"list-inline\">{% for tag in entry.tags.slugs %}<li><a id=\"tag_{{ tag|slug2js }}\" href=\"#\" >#{{ tag }}</a></li>{% endfor %}</ul><p>{{ entry.category }}</p><p class=\"text-right\"><a href=\"/directory/entries/{{ entry.slug }}/\" class=\"small\">Read more <i class=\"fa fa-arrow-circle-right\"></i></a></p>{% endif %}"],
    {% endif %}
    {% endfor %}};
var tags_all = [{% for entry in object_list %}
    {% if entry.lat %}"{{ entry.pk }}",{% endif %}
    {% endfor %}
];
var tags_layers = new Array();

for (var i = 0; i < tags_all.length; i++) {
    var indice = tags_all[i];
    var entry = entries[indice];
    var title = entry[0];
    var popup = entry[3];
    var marker = L.marker(new L.LatLng(entry[1], entry[2]), { title: title });
    marker.bindPopup(popup);
    markers.addLayer(marker);
}



map.addLayer(markers);
tags_layers['tags_all'] = markers;
map.fitBounds(markers.getBounds());

$("#tags_show_all").click(function(event) {
    for (tags_layer in tags_layers){
        var layerObj = tags_layers[tags_layer];
        map.removeLayer(layerObj);
    }
    var markers = L.markerClusterGroup();
    for (var i = 0; i < tags_all.length; i++) {
        var indice = tags_all[i];
        var entry = entries[indice];
        var title = entry[0];
        var popup = entry[3];
        var marker = L.marker(new L.LatLng(entry[1], entry[2]), { title: title });
        marker.bindPopup(popup);
        markers.addLayer(marker);
    }
    map.addLayer(markers);
    tags_layers['tags_all'] = markers;
    map.fitBounds(markers.getBounds());
    return false;
});

{% tag_cloud_for_model 'thedirectory.Entry' as tags %}
{% for tag in tags %}
//~ $("#tag_{{tag.pk}}").click(function(event){
    $("#tag_{{ tag.slug|slug2js }}").click(function(event){
    {# hide all layer markers #}
    for (tags_layer in tags_layers){
        var layerObj = tags_layers[tags_layer];
        map.removeLayer(layerObj);
    }
    {# (re)create a new layer for current tag #}
    //~ var markers_{{ tag.pk }} = L.markerClusterGroup();
    var markers_{{ tag.slug|slug2js }} = L.markerClusterGroup();
    {# retrieve pk entries list for current tag #}
    $.ajax({
        url: "{% url 'thedirectory:json_map_entries_by_tags' tag.name %}",
        dataType: "json",
        success: function(data) {
            //~ var tag_{{ tag.pk }} = $.parseJSON(data);
            var tag_{{ tag.slug|slug2js }} = $.parseJSON(data);
        }
    });

    $.getJSON("{% url 'thedirectory:json_map_entries_by_tags' tag.name %}", function(data){
           //~ tag_{{ tag.pk }} = data;
           tag_{{ tag.slug|slug2js }} = data;
            //~ for (var i = 0; i < tag_{{ tag.pk }}.length; i++) {
            for (var i = 0; i < tag_{{ tag.slug|slug2js }}.length; i++) {
                //~ var indice = tag_{{ tag.pk }}[i];
                var indice = tag_{{ tag.slug|slug2js }}[i];

                var entry = entries[indice];
                var title = entry[0];
                var popup = entry[3];
                var marker = L.marker(new L.LatLng(entry[1], entry[2]), { title: title });
                marker.bindPopup(popup);
                //~ markers_{{ tag.pk }}.addLayer(marker);
                markers_{{ tag.slug|slug2js }}.addLayer(marker);
            }
            //~ map.addLayer(markers_{{ tag.pk }});
            map.addLayer(markers_{{ tag.slug|slug2js }});
            //~ tags_layers['tag_{{ tag.pk }}'] = markers_{{ tag.pk }};
            tags_layers['tag_{{ tag.slug|slug2js }}'] = markers_{{ tag.slug|slug2js }};
            //~ map.fitBounds(markers_{{ tag.pk }}.getBounds());
            map.fitBounds(markers_{{ tag.slug|slug2js }}.getBounds());
    });
    return false;
});
{% endfor %}
