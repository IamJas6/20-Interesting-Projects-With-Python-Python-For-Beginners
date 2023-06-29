import phonenumbers
from phonenumbers import geocoder
import opencage
import folium

n="+916360547159"  #write phonenumber with country code
num=phonenumbers.parse(n,"CH")
loc=geocoder.description_for_number(num,"en")
print(loc)

from phonenumbers import carrier
service_num=phonenumbers.parse(n,"RO")
print(carrier.name_for_number(service_num,"en"))

from opencage.geocoder import OpenCageGeocode

api_key='0ed4e4e096e94dd4bbf4756ab206e821'
geocoder=OpenCageGeocode(api_key)
query=str(loc)
results=geocoder.geocode(query)
lat=results[0]['geometry']['lat']
lng=results[0]['geometry']['lng']
print(lat,lng)

mymap=folium.Map(location=[lat,lng],zoom_start=9)
folium.Marker([lat, lng],popup=loc).add_to(mymap)
mymap.save("mylocation.html")