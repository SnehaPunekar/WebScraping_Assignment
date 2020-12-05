from bs4 import BeautifulSoup
import requests as r
from geopy.exc import GeocoderTimedOut
from geopy.geocoders import Nominatim
import numpy as np

my_url='https://www.beyondbank.com.au/locate-us'
response = r.get(my_url)
src=response.content
soup_page = BeautifulSoup(src,'lxml')
ans=soup_page.find_all("div")

filename="Stores.csv"
f = open(filename,"w")
headers="Beyond Bank Branches\n"
f.write(headers)

ul_tag = soup_page.find_all("li")
for i in range(65,110):
	a_tag = ul_tag[i].find('a')
	f.write(a_tag.string)
	f.write("\n")
f.close()

filename2="Store_Details.csv"
f2 = open(filename2,"w")

headers="Store_name,Latitude,Longitude,Postal Code,Subarb,City,Country,URL Details,Phone_no,Off_days\n"
f2.write(headers)

store_name = soup_page.find_all("li")[108].string

url2 = my_url + "/melbourne.html"

result = r.get(url2)
src1 = result.content
soup_page1 = BeautifulSoup(src1,'lxml')
p = soup_page1.find_all("p")[3]
q = str(p)
code=(q[69:73])
suburb=(q[55:65])
city1=(q[65:68])
p2 = soup_page1.find_all("p")[4]
q2 = str(p2)
phone = (q2[62:74])
p3 = soup_page1.find_all("p")[16]
q3 = str(p3)
country = q3[30:40]
print(country)
tags = soup_page1.find_all("strong")[3]
a = str(tags)
day1 = (a[8:41])
tags = soup_page1.find_all("strong")[4]
a = str(tags)
day2 = (a[8:17])
day = day1 +", "+ day2
day.replace(",","")
tags = soup_page1.find_all("strong")[5]
a = str(tags)
off=(a[8:25])
address=(q[55:69])
print(address)

longitude = ""
latitude = ""

def findGeocode(city):
    try:
        geolocator = Nominatim(user_agent="http")
        return geolocator.geocode(city)
    except GeocoderTimedOut:
        return findGeocode(city)
if findGeocode(address)!= None:
	loc = findGeocode(address)
	latitude = loc.latitude
	longitude = loc.longitude
else:
    latitude = np.nan
    longitude = np.nan

data=store_name + "," + str(latitude) + "," + str(longitude) + "," + str(code) + "," + suburb + "," + city1 + "," + country + "," +str(url2)+ "," + str(phone) + ","  + off + "\n"
f2.write(data)
f2.close()
