# Surfs_up


## Project Overview

An investor wants to learn more about the weather before committing to build a Surf and Ice Cream shop in Oahu, Hawaii. The investor's main concern is the precipitation forcing the shop to close too frequently. We will be analyzing the weather for the month of June and December. To analyze Hawaii's weather data, SQLAlchemy was used to query the SQLite database.

## Results

### Temperature statistics for the month of June :

<img width="140" alt="Screen Shot 2021-10-19 at 6 00 25 PM" src="https://user-images.githubusercontent.com/88418201/138010778-c8bf2afe-bf26-4a2b-82ef-7b7dee1930a0.png">

### Temperature statistics for the month of December :

<img width="143" alt="d1" src="https://user-images.githubusercontent.com/88418201/138007254-ee3ee854-778b-48b2-8c9e-6477b78e87ff.png">

From the above statistics for the months of June and December we can infer that -

1. We compared June and December data to describe summer and winter temperatures.. During this time period, both June and December had an average temperature of 75°F and and 71°F, respectively.
2. June had a low temperature of 64°F and a high temperature of 85°F whereas December had a low temperature of 56°F and a high temperature of 83°F. 
3. In addition, both June and December had roughly similar standard deviations. June's standard deviation of 3.26 and December's standard deviation of 3.75 tells me that their temperature records are concentrated around both of their average temperatures. 
4. Lastly, June and December had a 75th percentile of 77°F and 74°F, respectively, which indicates that these two seasons had relatively warm temperatures.

## Summary

We can conclude that Hawaii is an excellent place to open up a surf and shake shack based on the temperature data however to gather more weather data for the investor to build his shop successfully we carried forward our analysis and calculated the precipitation levels for the months of June and December. Below is the combined Temperature and Precipitation statistics :

### Temperature and Precipitation statistics for the month of June :

<img width="231" alt="june" src="https://user-images.githubusercontent.com/88418201/138007060-8831f4a4-ff20-4abd-adc6-1febdb736f2b.png">

### Temperature and Precipitation statistics for the month of December :

<img width="221" alt="dec" src="https://user-images.githubusercontent.com/88418201/138007055-34fbb25c-a3a0-46a1-9a40-5b5e49c8ba04.png">

We have executed queries for the months of June and December that plot the precipitation recordings at our target location (station USC00519281) in order to ensure we are indeed making the correct data-based decision for our venture location.

<img width="756" alt="june2" src="https://user-images.githubusercontent.com/88418201/138010232-6602b8c7-8728-452f-87a4-a76662736a73.png">

<img width="829" alt="dec2" src="https://user-images.githubusercontent.com/88418201/138010223-7586d422-5298-4719-90cb-5aa46716d403.png">

The precipitation histogram for the month of June shows 120 instances of no precipitation with only a few occurances of more than 1 inch of rain. The December histogram shows similar results with over 140 instances of no precipitation, but more instances of precipitation exceeding 1 inch of rain. Therefore we can conclude that it will be a good decision to build a Surf and Ice Cream shop in Oahu, Hawaii. 
