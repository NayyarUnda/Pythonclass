import numpy as np 
from datetime import datetime
import seaborn as sns
import matplotlib.pyplot as pl
import pandas as pd 

data_nyc=pd.read_csv('/Users/nayyar/Downloads/yellow_tripdata_2010-01.csv')


def strip(string):
    parts=string.split(':')
    year=str(parts[0][:4])
    month=str(parts[0][5:-6])
    day=str(parts[0][8:-3])
    hours=str(parts[0][-2:])
    mins=str(parts[1])
    secs='00'
    return(year+'-'+month+'-'+day+' '+hours)

data_nyc['datetime']=data_nyc['pickup_datetime'].map(strip)
#data_nyc=data_nyc.set_index(['datetime'],inplace=True)

data_nyc['trip']=np.where(data_nyc['trip_distance']>=0, 1, 0)


longitude_l=data_nyc['pickup_longitude'] <= -73.870
longitude_u=data_nyc['pickup_longitude'] > -73.879
latitude_l=data_nyc['pickup_latitude'] >= 40.770
latitude_u=data_nyc['pickup_latitude'] < 40.779



data_nyc[longitude_l & longitude_u & latitude_l & latitude_u]



weather_2010_01=pd.read_csv('/Users/nayyar/Downloads/860655.csv')
LaGuardiaAirport=weather_2010_01['STATION_NAME']=='LA GUARDIA AIRPORT NY US'
def strip(string):
    parts=string.split(':')
    year=str(parts[0][:4])
    month=str(parts[0][4:-5])
    day=str(parts[0][6:-3])
    hours=str(parts[0][-2:])
    mins=str(parts[1])
    secs='00'
    return(year+'-'+month+'-'+day+' '+hours)
 
weather_2010_01['datetime'] = weather_2010_01['DATE'].map(strip)

LaGuardia=weather_2010_01['STATION_NAME']=='LA GUARDIA AIRPORT NY US'


merged_inner = pd.merge(left=weather_2010_01[LaGuardia],right=data_nyc[longitude_l & longitude_u & latitude_l & latitude_u],
                        left_on='datetime', right_on='datetime')


pl.subplots(figsize=(20,8),facecolor='yellow')
sns.set_style("whitegrid")

p=merged_inner.groupby(by=['HLY-TEMP-NORMAL'])['trip'].sum()
p.plot(color='#2ecc71')
pl.xticks(size=20, rotation=45,)
pl.yticks(size=20)
pl.xlabel('Hourly Temperature °F', size=25)
pl.ylabel('No. of Trips',size=25)
pl.title('Effect of Temperature on Number of Taxi Trips  ', size=30)
pl.savefig("Analysis_5.jpeg", bbox_inches='tight')				
pl.show()
		