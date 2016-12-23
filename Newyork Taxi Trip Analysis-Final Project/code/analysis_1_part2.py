from datetime import datetime,date
import numpy as np
import pandas as pd
import numpy as np
import seaborn as sns

import matplotlib.pyplot as pl

datanyc=pd.read_csv('/Users/nayyar/Downloads/yellow_tripdata_2016-01.csv')


datanyc['day']=datanyc['tpep_pickup_datetime'].apply(lambda x:datetime.strptime(x,'%Y-%m-%d %H:%M:%S').date().strftime('%A'))
datanyc['trip']=np.where(datanyc['trip_distance']>=0, 1, 0)



b_longitude_l=datanyc['pickup_longitude'] <= -73.840
b_longitude_u=datanyc['pickup_longitude'] > -74.047
b_latitude_l=datanyc['pickup_latitude'] >= 40.569
b_latitude_u=datanyc['pickup_latitude'] < 40.737


q_longitude_l=datanyc['pickup_longitude'] <= -73.742
q_longitude_u=datanyc['pickup_longitude'] > -73.958
q_latitude_l=datanyc['pickup_latitude'] >= 40.567
q_latitude_u=datanyc['pickup_latitude'] < 40.807
q1_longitude_l=datanyc['pickup_longitude'] <= -73.732
q1_longitude_u=datanyc['pickup_longitude'] > -73.813
q1_latitude_l=datanyc['pickup_latitude'] >= 40.633
q1_latitude_u=datanyc['pickup_latitude'] < 40.807


br_longitude_l=datanyc['pickup_longitude'] <= -73.797
br_longitude_u=datanyc['pickup_longitude'] > -73.939
br_latitude_l=datanyc['pickup_latitude'] >= 40.779
br_latitude_u=datanyc['pickup_latitude'] < 40.872

br1_longitude_l=datanyc['pickup_longitude'] <= -73.922
br1_longitude_u=datanyc['pickup_longitude'] > -73.748
br1_latitude_l=datanyc['pickup_latitude'] >= 40.837
br1_latitude_u=datanyc['pickup_latitude'] < 40.920

datanyc[b_longitude_l & b_longitude_u & b_latitude_l & b_latitude_u]
datanyc[(q_longitude_l & q_longitude_u & q_latitude_l & q_latitude_u )|( q1_longitude_l & q1_longitude_u & q1_latitude_l & q1_latitude_u)]
datanyc[(br_longitude_l & br_longitude_u & br_latitude_l & br_latitude_u )|( br1_longitude_l & br1_longitude_u & br1_latitude_l & br1_latitude_u)]

brooklyn=pd.DataFrame(data=datanyc[b_longitude_l & b_longitude_u & b_latitude_l & b_latitude_u].groupby(by=['day'])['trip'].sum()).reset_index()


weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
mapping = {day: i for i, day in enumerate(weekdays)}
key = brooklyn['day'].map(mapping)    
brooklyn = brooklyn.iloc[key.argsort()]

queens=pd.DataFrame(data=datanyc[(q_longitude_l & q_longitude_u & q_latitude_l & q_latitude_u )|( q1_longitude_l & q1_longitude_u & q1_latitude_l & q1_latitude_u)].groupby(by=['day'])['trip'].sum()).reset_index()
queens.head()
key = queens['day'].map(mapping)
queens = queens.iloc[key.argsort()]

bronx=pd.DataFrame(data=datanyc[(br_longitude_l & br_longitude_u & br_latitude_l & br_latitude_u )|( br1_longitude_l & br1_longitude_u & br1_latitude_l & br1_latitude_u)].groupby(by=['day'])['trip'].sum()).reset_index()
bronx.head()
weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
mapping = {day: i for i, day in enumerate(weekdays)}
key = bronx['day'].map(mapping)
bronx = bronx.iloc[key.argsort()]


max_brook= brooklyn['trip'].max()
brook_norm=(brooklyn['trip']/max_brook) *100
max_queens= queens['trip'].max()
queens_norm=(queens['trip']/max_queens) *100
max_bronx= bronx['trip'].max()
bronx_norm=(bronx['trip']/max_bronx) *100
norm=pd.DataFrame(data=brooklyn['day'])
norm['Brooklyn']=brook_norm
norm['Queens']=queens_norm
norm['Bronx']=bronx_norm



pl.subplots(figsize=(20,8))
x = [0,1,2,3,4,5,6]
xTicks = brooklyn['day']
y =brooklyn['trip']
pl.xticks(x, xTicks)
pl.xticks(range(7), xTicks, rotation=45, size=20) #writes strings with 45 degree angle
p=pl.bar(X,y,color="#9b59b6",width = 0.45,label='Brooklyn',align='center')
pl.yticks(size=20)
pl.xlabel('Days', size=25)
pl.ylabel('No of Trips', size=25)
pl.legend(loc=2,prop={'size':22})
pl.title('Taxi Trips By Day Of Week  ', size=30)
pl.savefig("Analysis_1_brooklyn.jpeg", bbox_inches='tight')