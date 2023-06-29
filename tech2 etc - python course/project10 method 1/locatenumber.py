import phonenumbers
from phonenumbers import geocoder

n="+917019906805"  #write phonenumber with country code
num=phonenumbers.parse(n,"CH")
print(geocoder.description_for_number(num,"en"))

from phonenumbers import carrier
service_num=phonenumbers.parse(n,"RO")
print(carrier.name_for_number(service_num,"en"))