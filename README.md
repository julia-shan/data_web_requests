# Quantiful_data_test
Author: Julia Shan

Refer to requirements.txt to set up environment and packages

#Task 1

Run Task1.py. The data for average precipitaton in Hawaii on the 2nd of July 2000 should be printed. However, there was no data recorded for this time, for both hourly and 15 min precipitation
Part 2 of this task is typed in Task1_Part2.txt

#Task 2

Run Task2.py. The data should be stored in the database 'stock.db'. This can be deleted and will be created again when re-running the script
The SQLite Query executed for part 2 of this task was:

SELECT strftime('%Y', DATE) as year, AVG(VOLUME), STOCK
FROM stocks
GROUP BY STOCK, year; 

I used DBBrowser (SQLite) to view the database and to execute the above query. I then stored the result in stocks.csv

#Task 3

To run the REST API webserver, run the Task3.py script. Make sure the script is running while accessing endpoints

Paste the following in a web browser:
 http://127.0.0.1:5000/ - this is the home page (should just display 'Stocks API')

To access the GET/stocks endpoint, paste the following into a web browser
 http://127.0.0.1:5000/stocks

To access the GET/volume endpoint, paste the following into a web browser
 http://127.0.0.1:5000/volume

This was my original endpoint, which displays a plot of the volume of stocks over team for each stock, Tesla, Amazon and Twitter
I used the matplotlib package to plot the data which I then saved as a png file
I then returned this png as to the GET/volume endpoint.