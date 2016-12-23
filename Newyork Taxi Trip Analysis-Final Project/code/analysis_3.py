import pandas as pd 
from datetime import datetime
import numpy as np
import seaborn as sns
import matplotlib.pyplot as pl
data_nyc=pd.read_csv('/Users/nayyar/Downloads/green_tripdata_2016-03.csv')
data_nyc.head()
longitude_l=data_nyc['Dropoff_longitude'] <= -73.870
longitude_u=data_nyc['Dropoff_longitude'] > -73.879
latitude_l=data_nyc['Dropoff_latitude'] >= 40.770
latitude_u=data_nyc['Dropoff_latitude'] < 40.779
midtown_long_l=data_nyc['Pickup_longitude'] <= -73.950
midtown_long_u=data_nyc['Pickup_longitude'] > -74.00
midtown_lat_l=data_nyc['Pickup_latitude'] >= 40.72
midtown_lat_u=data_nyc['Pickup_latitude'] < 40.77
df=pd.DataFrame(data_nyc[latitude_l & latitude_u & longitude_u & longitude_l& midtown_long_l & midtown_long_u & midtown_lat_l & midtown_lat_u])




def trip_time(x,y):
    # first check whether the date in x and y are same or not
    # if same use same method as earlier
    tx_date = datetime.strptime(x, '%Y-%m-%d %H:%M:%S').date()
    ty_date = datetime.strptime(y, '%Y-%m-%d %H:%M:%S').date()
    
    tx_date1 = str(datetime.strptime(x, '%Y-%m-%d %H:%M:%S').time())
    ty_date1 = str(datetime.strptime(y, '%Y-%m-%d %H:%M:%S').time())
    drop=tx_date1.split(':')
    
    pick=ty_date1.split(':')
    trip_length = 0.0
    #tx = datetime.datetime(x)
    #ty = datetime.datetime(y)
    if tx_date == ty_date:
        trip_length= (float(drop[0])*60 + float(drop[1]))-(float(pick[0])*60+float(pick[1]))
    
    if tx_date != ty_date :   
        trip_length= ((23- float(pick[0]))*60+ 60.0 - float(pick[1])) + (float(drop[0])*60 + 60*24 + float(drop[1]))
        
    # else return modified trip time 
    if trip_length >60:
        trip_length = 10
    return trip_length

df['trip_time'] = list(map(trip_time,df['Lpep_dropoff_datetime'],df['lpep_pickup_datetime']))

df['hour']=(pd.to_datetime(df['Lpep_dropoff_datetime']).apply(lambda x: (x.hour + (x.minute/60))))




pl.subplots(figsize=(20,8))
sns.set_style("whitegrid")
x = df['hour']
xTicks =[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24]
pl.xticks(x,xTicks)
pl.xticks(range(24), xTicks, rotation=45, size=20) #writes strings with 45 degree angle
pl.yticks(size=20)
pl.xlabel('Time (24 hour format)', size=25)
pl.ylabel('Trip Time', size=25)
p=pl.scatter(x,df['trip_time'],color="#3498db",linewidth=6)
pl.legend(loc=2,prop={'size':22})
pl.title('Trip time analysis from MidTown to LaGuardia on different times of the day ', size=30)
pl.show()
pl.savefig("Analysis_3.jpeg", bbox_inches='tight')
