import pandas as pd 
import seaborn as sns
import matplotlib.pyplot as pl

fip= open('/Users/nayyar/Downloads/yellow_tripdata_2016-03.csv','r')

fop= open('/Users/nayyar/Downloads/small_yellow_tripdata_2016-03.csv','w')
count = 0
for line in fip:
    fop.write(line)
    count +=1
    if count>=24000:
        break


data_nyc=pd.read_csv('/Users/nayyar/Downloads/small_yellow_tripdata_2016-03.csv')

def latlng(long, lat):
    return (str(lat)+','+str(long))
        
data_nyc['latlng'] = list(map(latlng,data_nyc['dropoff_longitude'],data_nyc['dropoff_latitude']))

import requests
def reverse_geocode(latlng):
    result = {}
    url = 'https://maps.googleapis.com/maps/api/geocode/json?latlng={}&key=AIzaSyBXCb-_ZP6zEJKI3ElHI3W112lJ-w0Ck6A'
    request = url.format(latlng)
    data = requests.get(request).json()
    if len(data['results']) > 0:
        result = data['results'][0]
    return result
data_nyc['geocode_data'] = data_nyc['latlng'].map(reverse_geocode)
def parse_city(geocode_data):
    if (not geocode_data is None) and ('address_components' in geocode_data):
        for component in geocode_data['address_components']:
            if 'locality' in component['types']:
                return component['long_name']
            elif 'postal_town' in component['types']:
                return component['long_name']
            elif 'administrative_area_level_2' in component['types']:
                return component['long_name']
            elif 'administrative_area_level_1' in component['types']:
                return component['long_name']
    return None

data_nyc['city'] = data_nyc['geocode_data'].map(parse_city)
data_nyc.head()


pl.subplots(figsize=(20,8),facecolor='yellow')
y=data_nyc['tip_amount']
x=data_nyc['city']
sns.set_style("whitegrid")
sns.stripplot(x,y,jitter=0.4)
pl.xticks(size=15) #writes strings with 45 degree angle
pl.yticks(size=15)
pl.title('Tip Amount by City Analysis ', size=30)
pl.savefig("Analysis_4.jpeg", bbox_inches='tight')
pl.show()

