===========================================
New York Taxi Trip Data Analysis using  Python
===========================================

## About the Data

**TLC Trip Data** contains records of yellow and green taxi operated around newyork. Each CSV is a 2.2 gb file containing details about pick-up and drop-off dates/times, pick-up and drop-off locations, trip distances, itemized fares, rate types, payment types, and driver-reported passenger counts. TLC trip data sets pick up and drop locations are in longitudes and longitudes. I used georeverse coding using google api to map longitudes and latitudes to city values.I used it for the fourth analysis,however, it has a limit of 25000 request per day. For remaining analysis, 25000 doesn't meet the requirement as data is too huge. So I used a bounding box approach and extracted the bounding box for the cities and used it to identify the latitude,longitude corrosponding to the cities. I extracted the bounding box using google maps. Further, I have used weather data set from National Centres For Environmental Information to obtain hourly temperatures for jan 2010. 

- [TLC Trip Data] (http://www.nyc.gov/html/tlc/html/about/trip_record_data.shtml)
- [Weather Data] (https://www.ncdc.noaa.gov/)
- [google api] (https://developers.google.com/maps/documentation/geocoding/start)

.

## Analysis 1

**Trend of number of taxi trips for different days of the week for different cities**

In Analysis 1, I analyzed the taxi trips taken during the whole month, grouped these trips by days of week to calculate trip counts for three different cities(Brooklyn,Queens County,Bronx). I analyzed the trends for the three cities seperately and then also plotted their normalized percentage values to compare their trends against each other. 

To run the script
```
python Analysis_1.py 
```

Outout CSV file :

I seperated the data for brooklyn in a data frame and summed up  trips taken to perform taxi trips by day of week analysis.As we can see the highest number of trips taken are 450000 on friday and saturday and minimum of 250000 on monday.

![alt tag]( https://github.com/NayyarUnda/Pythonclass/blob/master/Newyork%20Taxi%20Trip%20Analysis-Final%20Project/output%20graphs/Brooklyn_analysis1.JPG)

The highest number of trips are 440000 on friday and saturday and minim
![alt tag]( https://github.com/NayyarUnda/Pythonclass/blob/master/Newyork%20Taxi%20Trip%20Analysis-Final%20Project/output%20graphs/Queens_analysis1.JPG)
![alt tag]( https://github.com/NayyarUnda/Pythonclass/blob/master/Newyork%20Taxi%20Trip%20Analysis-Final%20Project/output%20graphs/Bronx_analysis1.JPG)

NORMALIZED OUTPUT FOR 3 CITIES

![alt tag] (https://github.com/NayyarUnda/Pythonclass/blob/master/Newyork%20Taxi%20Trip%20Analysis-Final%20Project/output%20graphs/analysis1.jpg)

Insights – As visible in the normalized graph the pattern of taxi trips for Monday ,Tuesday and Wednesday is same for the 3 cities 55% for Brooklyn 75% for queens and 50 % for Bronx, on Friday, the number of trips taken is maximum which then decreases for Saturday and Sunday (higher than mon, tue and wednesday).
As expected Brooklyn is the busiest city with maximum of 450000 trips then Queens and then Bronx.



## Analysis 2

**Which is the busiest hour of the day, what is the number of trips, and how it varies with different days**

In Analysis 2, I analyzed the Nyc trip record data for hourly traffic. I filtered the data for each day and grouped by hour.
To run the script :-
```  
python Analysis_2.py 
```

![alt tag]( https://github.com/NayyarUnda/Pythonclass/blob/master/Newyork%20Taxi%20Trip%20Analysis-Final%20Project/output%20graphs/Analysis_2.jpeg)


Insights – 
1. Trends for Monday, Tuesday, Wednesday, and Thursday are very similar.
2. Saturday and Sunday have similar trend.
3. We can see a common trend for all the days, the number of trips decrease from 12 am to morning 5 pm and then increase from morning 6 am to 11 pm. 
4. As expected we see maximum trip activity on Friday.
5. On Friday, Saturday and Sunday, we see higher activity after midnight.


## Analysis 3

**When is the trip time maximum and minimum?**

In Analysis 3, I evaluated trip timings for trip from midtown to La Guardia Airport at different time of the day. 
To run the code :-
```
python Analysis_3.py
```

output
![alt tag]( https://github.com/NayyarUnda/Pythonclass/blob/master/Newyork%20Taxi%20Trip%20Analysis-Final%20Project/output%20graphs/Analysis_3.jpeg)

Insights - As expected trip time increased from 10 mins to 35 mins in afternoon even reached around 50 for 5 pm to 6pm.  

## Analysis 4

**What is the relation between drop off location (cities) with tip amount?**

In Analysis 4, I have used google map api and reverse geocoded drop off locations latitudes and longitudes to obtain corresponding city values. Then I have mapped the tip amounts to their corresponding cities


To run the code :-
```
python Analysis_4.py JUN-2015
```





  
 ![alt tag] (https://github.com/NayyarUnda/Pythonclass/blob/master/Newyork%20Taxi%20Trip%20Analysis-Final%20Project/output%20graphs/Analysis_4.jpeg)
 
 
 

Insights - We can see that maximum tips have been given by riders to New York city, Queens county and Kings County and very few Riders are generous from Newark and Bronx County in terms of giving tips.
 

## Analysis 5


**How Does weather affect the number of trips ?**

In Analysis 5, I have joined taxi trip data set with weather data set to obtain number of trips taken during different temperatures. It contains hourly normal temperatures from January 2010


To run the code :-
```
python Analysis_5.py JUN-2015
```

![alt tag]( https://github.com/NayyarUnda/Pythonclass/blob/master/Newyork%20Taxi%20Trip%20Analysis-Final%20Project/output%20graphs/Analysis_5.jpeg)


Insights -  Number of trips increase between temperature range of 32 to 36 degree Farhenheit.




