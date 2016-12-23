

from datetime import datetime,date
import pandas as pd 
import numpy as np
import numpy as np
import seaborn as sns
import matplotlib.pyplot as pl

datanyc=pd.read_csv('/Users/nayyar/Downloads/yellow_tripdata_2016-01.csv')
datanyc['trip']=np.where(datanyc['trip_distance']>=0, 1, 0)
datanyc['day']=datanyc['tpep_pickup_datetime'].apply(lambda x:datetime.strptime(x,'%Y-%m-%d %H:%M:%S').date().strftime('%A'))

datanyc['hour']=datanyc['tpep_pickup_datetime'].apply(lambda x:datetime.strptime(x,'%Y-%m-%d %H:%M:%S').time().strftime('%H'))

mon=datanyc['day']=='Monday'
monday=pd.DataFrame(data=datanyc[mon].groupby(by=['hour'])['trip'].sum()).reset_index()

tue=datanyc['day']=='Tuesday'
tuesday=pd.DataFrame(data=datanyc[tue].groupby(by=['hour'])['trip'].sum()).reset_index()

wed=datanyc['day']=='Wednesday'
wednesday=pd.DataFrame(data=datanyc[wed].groupby(by=['hour'])['trip'].sum()).reset_index()

thu=datanyc['day']=='Thursday'
thursday=pd.DataFrame(data=datanyc[thu].groupby(by=['hour'])['trip'].sum()).reset_index()

fri=datanyc['day']=='Friday'
friday=pd.DataFrame(data=datanyc[fri].groupby(by=['hour'])['trip'].sum()).reset_index()

sat=datanyc['day']=='Saturday'
saturday=pd.DataFrame(data=datanyc[sat].groupby(by=['hour'])['trip'].sum()).reset_index()

sun=datanyc['day']=='Sunday'
sunday=pd.DataFrame(data=datanyc[sun].groupby(by=['hour'])['trip'].sum()).reset_index()



pl.subplots(figsize=(20,8))
x = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23]
xTicks =monday['hour']
pl.xticks(x,xTicks)
pl.xticks(range(24), xTicks, rotation=45, size=20) #writes strings with 45 degree angle
pl.yticks(size=20)
pl.xlabel('Time (24 hour format)', size=25)
pl.ylabel('Number of Trips', size=25)
p=pl.plot(x,monday['trip'],color="#9b59b6",linewidth=6,label='Monday')
p=pl.plot(x,tuesday['trip'],color="#e74c3c",linewidth=6, label='Tuesday')
p=pl.plot(x,wednesday['trip'],color="#2ecc71",linewidth=6,label='Wednesday')
p=pl.plot(x,thursday['trip'],color="#3498db",linewidth=6,label='Thursday')
p=pl.plot(x,friday['trip'],color="#95a5a6", linewidth=6,label='Friday')
p=pl.plot(x,saturday['trip'],color="yellow",linewidth=6,label='Saturday')
p=pl.plot(x,sunday['trip'],color="#34495e",linewidth=6,label='Sunday')
pl.legend(loc=2,prop={'size':22})
pl.title('Number of Taxi Trips During Different times of the Day, for All Days of the Week', size=30)
pl.savefig("Analysis_2.jpeg", bbox_inches='tight')
pl.show()