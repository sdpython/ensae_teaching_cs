#coding:latin-1
import sys
sys.path.append("../../../../program/python/pyensae/src")  # ligne inutile

from pyensae import download_data
import pandas

download_data("td9_data.zip", website = 'xd')
file1 = "td9_full.txt"
tbl = pandas.read_csv (file1, sep = "\t")

from pandas.tools.plotting import scatter_plot

gr = tbl.groupby(['lng','lat'], as_index = False).agg(lambda x: len(x))

# voir http://dev.openlayers.org/docs/files/OpenLayers/Marker-js.html pour changer le marker
html = """
<html><body>
  <div id="mapdiv"></div>
  <script src="http://www.openlayers.org/api/OpenLayers.js"></script>
  <script>
    map = new OpenLayers.Map("mapdiv");
    map.addLayer(new OpenLayers.Layer.OSM());
    var proj =  new OpenLayers.Projection("EPSG:4326");
 
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
    markers.addMarker(new OpenLayers.Marker(lonLat{0}));
"""    

lines = [ ]
for i,row in enumerate(gr.values) :
    y = lat = row[1]
    x = lng = row[0]
    line = position.format(i,x,y)
    lines.append(line)
    
text = "\n".join( lines )
html = html.replace("__VELIB__", text)
with open("velib.html", "w") as f : f.write(html)

        

