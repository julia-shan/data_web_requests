# data_web_requests
Author: Julia Shan

This repo was for me to learn about web requests, how to extract data from APIs, and how to manipulate data
Refer to requirements.txt to set up environment and packages

#Task 1

Task 1 was using the NDCC api to find climate data
Run Task1.py. The data for average precipitaton in Hawaii on the 2nd of July 2000 should be printed. However, there was no data recorded for this time, for both hourly and 15 min precipitation.

#Task 2
Task 2 was using the Alpha Vantage api to collect stock data. I collected the weekly time series data for Tesla, Twitter and Amazon for the last 15 years and stored them in a SQLite database. I then wrote an SQl query to retrieve the average volume per year for each stock and stored the result in stocks.csv

Run Task2.py. The data should be stored in the database 'stock.db'. This can be deleted and will be created again when re-running the script

#Task 3
Task 3 was creating a REST API using the Python framework flask. The GET/stocks endpoint lists the names of the available stocks from task 2. The GET/volume endpoint  displays a plot of the volume of stocks over team for each stock

To run the REST API webserver, run the Task3.py script. Make sure the script is running while accessing endpoints

Paste the following in a web browser:
 http://127.0.0.1:5000/ - this is the home page (should just display 'Julia Shan's Stocks API')

To access the GET/stocks endpoint, paste the following into a web browser
 http://127.0.0.1:5000/stocks

To access the GET/volume endpoint, paste the following into a web browser
 http://127.0.0.1:5000/volume
