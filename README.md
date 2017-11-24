# Uber-Cool
Rob, Elly and Farah slaying


Welcome to our repository! Here you shall find all sorts of treasures which can aid your quest to discover 
how Uber has affected London, since time itself began( well actually, just from around 2011, because Uber only arrived in 2012).
*********************************************************************************************************************************

## Tableau Public Analytics
Please follow these links to Tableau Public, and you can see our analysis on the data gathered so far.
https://public.tableau.com/profile/farah.shair#!/vizhome/UberTweetSentiment/Story1

************
## Data Sources
*************

### LondonUnemployment.csv
This file contains quarterly London unemployment rates, from 2011 Q1 until 2017 Q2.
### TaxiDrivers.csv
This file contains annual national data about the number of taxi drivers in the UK, segmented by part time and full time, and employed and self employed.
### uber_twitter 
This file contains all the tweets used in the analysis on Tableau Public, and their sentiment score
### CO2 Emissions
Contains boroughs of London and the kilotonnes of CO2 emitted from transport

*****************
## Historical Tweets
*****************

This folder contains the code used to scrape tweets since 2012 and generate sentiment for each one. The sentiment is averaged for all the tweets each day, and then the dataframe is saved to a csv. This is what was plotted on Tableau.

****************************
## Reddit Scrape and wordcloud
****************************

Enter the cavernous Reddit folder to find the creation of a wordcloud from a Reddit Comment thread as well as a copy of the cloud.

****************************************************
## SciKit learn predictions for unemployment in London 
****************************************************

The code found in the file unemployment_prediction uses previous unemployment data to predict the future. 
This link shows the results with the red based on real data and the blue a prediction:
https://plot.ly/~RobDavies1995/27

**********
## TFL V UBER
**********
This contains data supplied by TFL and Data.London as well as the SQL extracts and Tableau workbook.
The following link will take you to our visualistaions of this data.
https://public.tableau.com/profile/robert.davies8295#!/vizhome/TFLanduber/Story1
