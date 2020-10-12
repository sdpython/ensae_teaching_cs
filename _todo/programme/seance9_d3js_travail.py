#coding:latin-1
import sys
sys.path.append("../../../../program/python/pyensae/src")  # ligne inutile

from pyensae.datasource import download_data
import pandas

download_data("td9_station_travail.zip", website = 'xd')
file1 = "td9_station_travail.txt"
tbl = pandas.read_csv (file1, sep = "\t")

# voir http://dev.openlayers.org/docs/files/OpenLayers/Marker-js.html pour changer le marker
html = """
<html><body>
  <div id="mapdiv"></div>
  <script src="http://www.openlayers.org/api/OpenLayers.js"></script>
  <script>
    map = new OpenLayers.Map("mapdiv");
    map.addLayer(new OpenLayers.Layer.OSM());
    var proj =  new OpenLayers.Projection("EPSG:4326");
    
    var size = new OpenLayers.Size(10,10);
    var offset = new OpenLayers.Pixel(-(size.w/2), -size.h);

    var icon_rouge = new OpenLayers.Icon('http://www.xavierdupre.fr/blog/documents/carrerouge.png', size, offset);
    var icon_vert = new OpenLayers.Icon('http://www.xavierdupre.fr/blog/documents/carrevert.png', size, offset);
 
    var zoom=13;
 
    var markers = new OpenLayers.Layer.Markers( "Markers" );
    map.addLayer(markers);
    
    __VELIB__
 
    map.setCenter (lonLat0, zoom);
  </script>
</body></html>    
"""

position ="""
    var lonLat{0} = new OpenLayers.LonLat( {1} ,{2} ).transform(proj, map.getProjectionObject() );
    markers.addMarker(new OpenLayers.Marker(position=lonLat{0},icon=icon_{3}.clone()));
"""    

lines = [ ]
for i,row in enumerate(tbl.values) :
    x = lng = row[2]
    y = lat = row[3]
    c = row[1]
    icon = "rouge" if c > 0.5 else "vert"
    line = position.format(i,x,y, icon)
    lines.append(line)
    
text = "\n".join( lines )
html = html.replace("__VELIB__", text)
with open("velib_work.html", "w") as f : f.write(html)

#import webbrowser
#webbrowser.open("velib_work.html")
