from turtle import color
import folium
import pandas
import json


data=pandas.read_csv("Volcanoes.txt")
lat=list(data["LAT"])
lon=list(data["LON"])
elev=list(data["ELEV"])

def color_producer(elevation):
    if (elevation<1000):
        return "blue"
    elif (1000<=elevation<3000):
        return "orange"
    else:
        return "red"        

map=folium.Map(location=[38.58,-99.89],
zoom_start=6)
fgv=folium.FeatureGroup(name="My Map")

for lt,ln,el in zip(lat,lon,elev):
    fgv.add_child(folium.CircleMarker(location=[lt,ln],radius=10,
    popup=str(el)+"m",fill_color=color_producer(el),fill=True,color="black",fill_opacity=0.5))
fgp=folium.FeatureGroup(name="Population")    
fgp.add_child(folium.GeoJson(data=open('world.json','r',encoding='utf-8-sig').read(),
style_function=lambda x : {'fillColor':'green' if x['properties']['POP2005']<1000000
else 'orange' if 10000000 <= x['properties']['POP2005']<20000000 else 'red'} ))   
map.add_child(fgv)
map.add_child(fgp)
map.add_child(folium.LayerControl())
map.save("aman.html")


