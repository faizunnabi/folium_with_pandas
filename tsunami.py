import pandas as pd
import folium
data=pd.read_csv('tsunami_data.csv')
df=pd.DataFrame(data)
df.set_index('objectid')

lats=list(data["shape"])[1]
type(lats)
lt=lats.split()
lati=lt[0].replace('(','').replace(',','')
lt=float(lati)
lati_list=[]
longi_list=[]

for lat in df["shape"]:
    lt=lat.split()
    lati=lt[0].replace('(','').replace(',','')
    lt=float(lati)
    lati_list.append(lt)

for lon in df["shape"]:
    lt=lon.split()
    longi=lt[1].replace(')','').replace(',','')
    lt=float(longi)
    longi_list.append(lt)

names_list=list(df["mapname"])

map=folium.Map(location=[20.26,-155.55],zoom_start=8,tiles="Mapbox Control Room")

fgt=folium.FeatureGroup(name="Tsunami prones")

for la,lo,name in zip(lati_list,longi_list,names_list):
    fgt.add_child(folium.CircleMarker(location=[la,lo],radius=6,popup=str(name),
                                      fill_color="red",fill=True,color="grey",stroke=1,
                                      weight=1,fill_opacity=0.7))
map.add_child(fgt)
map.add_child(folium.LayerControl())
map.save("tsunami_map.html")