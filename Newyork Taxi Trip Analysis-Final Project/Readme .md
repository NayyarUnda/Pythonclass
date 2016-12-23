===========================================
New York Taxi Trip Data Analysis using  Python
===========================================

## About the Data

**TLC Trip Data** contains records of yellow and green taxi operated around newyork. Each Csv is a 2.2 gb file containing details about pick-up and drop-off dates/times, pick-up and drop-off locations, trip distances, itemized fares, rate types, payment types, and driver-reported passenger counts.TLC trip data sets. Pick up and drop locations are in longitudes and longitudes. I used geo reverse coding using google api to extract city values but google api has a limit of 25000 request and for converting  coordinates of one file will require over 1000000 requests. Further, I have used weather data set from National Centres For Environmental Information to obtain hourly temperatures for jan 2010. 

- [TLC Trip Data] (http://www.nyc.gov/html/tlc/html/about/trip_record_data.shtml)
- [Weather Data] (https://www.ncdc.noaa.gov/)
- [google api] (https://developers.google.com/maps/documentation/geocoding/start)



## Analysis 1

**Which city has the maximum taxi traffic and at which day of week ?**

In Analysis 1, I analyzed the taxi trips taken during the whole month, Grouped these trips by days of week to calculate trip counts.

To run the script
```
python Analysis_1.py 
```

Outout CSV file :
NORMALIZED OUTPUT FOR 3 CITIES

![alt tag] (https://github.com/NayyarUnda/Pythonclass/blob/master/Newyork%20Taxi%20Trip%20Analysis-Final%20Project/output%20graphs/analysis1.jpg)

![alt tag]( https://github.com/NayyarUnda/Pythonclass/blob/master/Newyork%20Taxi%20Trip%20Analysis-Final%20Project/output%20graphs/Bronx_analysis1.JPG)

![alt tag]( https://github.com/NayyarUnda/Pythonclass/blob/master/Newyork%20Taxi%20Trip%20Analysis-Final%20Project/output%20graphs/Brooklyn_analysis1.JPG)

![alt tag]( https://github.com/NayyarUnda/Pythonclass/blob/master/Newyork%20Taxi%20Trip%20Analysis-Final%20Project/output%20graphs/Queens_analysis1.JPG)


Insights – As visible in the normalized graph the pattern of taxi trips for Monday ,Tuesday and Wednesday is same for the 3 cities 55 for Brooklyn 75 for queens and 50 % for Bronx and on Friday the traffic reaches its maximum for Friday and then decreases for Sunday and Monday.
As expected Brooklyn is the busiest city with maximum of 450000 trips then Queens and then Bronx.



## Analysis 2

**Which is the busiest hour of the day and what is the number of trips?**

In Analysis 2, I analyzed the Nyc trip record data for hourly traffic. I filtered the data for each day and grouped by hour.
To run the script :-
```  
python Analysis_2.py 
```

![alt tag]( https://github.com/NayyarUnda/Pythonclass/blob/master/Newyork%20Taxi%20Trip%20Analysis-Final%20Project/output%20graphs/Analysis_2.jpeg)


Insights – As we can the common trend for all the days is the trips decrease from 12 am to morning 5 pm and then increase from morning 6 am to 11 pm. As expected trips maximum trips are taken on Friday evening and Saturday evening.


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




