# -*- coding: utf-8 -*-
"""WeatherAPI.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ooIJhTyb9PJIR-GTlFiw3HCwf26FWDgR
"""

import requests
from datetime import datetime

api_key = 'ef8b40b1e30fa9b90291a4a525e7c669'
location = input("Enter the city name: ")

weather_api_link = "https://api.openweathermap.org/data/2.5/weather?q="+location+"&appid="+api_key
api_link_wd = requests.get(weather_api_link)
api_data_wd = api_link_wd.json()

lati = str(api_data_wd['coord']['lat'])
longi = str(api_data_wd['coord']['lon'])
temp_city = (((api_data_wd['main']['temp']) - 273.15))
temp_city = str(float("{0:.2f}".format(temp_city)))
weather_desc = str(api_data_wd['weather'][0]['description'])
humidity = str(api_data_wd['main']['humidity'])
wind_spd = str(api_data_wd['wind']['speed'])
date_time = str(datetime.now().strftime("%d %b %Y | %I:%M:%S %p"))

print("-------------------------------------------------------------")
print("Weather Stats for - {}  || {}".format(location.upper(), date_time))
print("-------------------------------------------------------------")

print("Latitude for the location   :",lati)
print("Longitude for the location  :",longi)
print("Current temperature is      : {} deg C".format(temp_city))
print("Current Weather condition   :",weather_desc)
print("Current Humidity            :",humidity, '%')
print("Current wind speed          :",wind_spd ,'kmph\n\n')

lati_str = str(lati)
longi_str = str(longi)
air_pollution_api_link = "http://api.openweathermap.org/data/2.5/air_pollution?lat="+lati_str+"&lon="+longi_str+"&appid="+api_key
api_link_ap = requests.get(air_pollution_api_link)
api_data_ap = api_link_ap.json()

aqi = str(api_data_ap['list'][0]['main']['aqi'])
co = str(api_data_ap['list'][0]['components']['co'])
no = str(api_data_ap['list'][0]['components']['no'])
no2 = str(api_data_ap['list'][0]['components']['no2'])
o3 = str(api_data_ap['list'][0]['components']['o3'])
so2 = str(api_data_ap['list'][0]['components']['so2'])
pm2_5 = str(api_data_ap['list'][0]['components']['pm2_5'])
pm10 = str(api_data_ap['list'][0]['components']['pm10'])
nh3 = str(api_data_ap['list'][0]['components']['nh3'])


print("-------------------------------------------------------------")
print("AIR POLLUTION STATS - {}  || {}".format(location.upper(), date_time))
print("-------------------------------------------------------------")

print("Possible values for Air Quality Index : 1, 2, 3, 4, 5 \nWhere \n1 = Good, \n2 = Fair, \n3 = Moderate, \n4 = Poor, \n5 = Very Poor.")
print("Air Quality Index in your city : ",aqi)
print("Now let's see the components present in the air.\n")
print("??oncentration of CO (Carbon monoxide), ??g/m3             : "+co)
print("??oncentration of NO (Nitrogen monoxide), ??g/m3           : "+no)
print("??oncentration of NO2 (Nitrogen dioxide), ??g/m3           : "+no2)
print("??oncentration of O3 (Ozone), ??g/m3                       : "+o3)
print("??oncentration of SO2 (Sulphur dioxide), ??g/m3            : "+so2)
print("??oncentration of PM2.5 (Fine particles matter), ??g/m3    : "+pm2_5)
print("??oncentration of PM10 (Coarse particulate matter), ??g/m3 : "+pm10)
print("??oncentration of NH3 (Ammonia), ??g/m3                    : "+nh3)

with open('weather_data.txt','wb') as f:
  f.write(api_link_wd.content)

location = location.upper()
temp_city = str(temp_city)
with open('result.txt','w') as f:
  f.write("-------------------------------------------------------------\n"
  "Weather Stats for - " + location + "  || " + date_time +
  "\n-------------------------------------------------------------\n\n"
  "Latitude for the location   :"+lati+
  "\nLongitude for the location  :"+longi+
  "\nCurrent temperature is      :"+temp_city+" deg C\n"
  "Current Weather condition   :"+weather_desc+
  "\nCurrent Humidity            :"+humidity+ "%\n"
  "Current wind speed          :"+wind_spd+"kmph\n\n\n")

with open('result.txt','a') as f:
  f.write("-------------------------------------------------------------\n"
  "AIR POLLUTION STATS - " + location + "  || " + date_time +
  "\n-------------------------------------------------------------\n\n"  
  "Possible values for Air Quality Index : 1, 2, 3, 4, 5 \nWhere \n1 = Good, \n2 = Fair, \n3 = Moderate, \n4 = Poor, \n5 = Very Poor.\n"
  "Air Quality Index in your city : \n"
  "Now let's see the components present in the air.\n"
  "??oncentration of CO (Carbon monoxide), ??g/m3             : "+co+
  "\n??oncentration of NO (Nitrogen monoxide), ??g/m3           : "+no+
  "\n??oncentration of NO2 (Nitrogen dioxide), ??g/m3           : "+no2+
  "\n??oncentration of O3 (Ozone), ??g/m3                       : "+o3+
  "\n??oncentration of SO2 (Sulphur dioxide), ??g/m3            : "+so2+
  "\n??oncentration of PM2.5 (Fine particles matter), ??g/m3    : "+pm2_5+
  "\n??oncentration of PM10 (Coarse particulate matter), ??g/m3 : "+pm10+
  "\n??oncentration of NH3 (Ammonia), ??g/m3                    : "+nh3)

with open('air_pollution_data.txt','wb') as f:
  f.write(api_link_ap.content)