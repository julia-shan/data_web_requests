import requests
import sqlite3

#Create connection with sqlite 
con = sqlite3.connect('stock.db')
cur = con.cursor()

#Delete old table
cur.execute('''DROP TABLE IF EXISTS stocks''')
#Create new table
cur.execute(''' CREATE TABLE stocks ( DATE DATE, STOCK TEXT, OPEN REAL, HIGH REAL, LOW REAL, CLOSE REAL, VOLUME INT)''')

#Retrieved from alpha vantage API documentation
URL = 'https://www.alphavantage.co/query'
apikey = '6053SNAFDVUQVJVB'

#Weekly time series for requrests for weekly stock data
PARAMS = {'function' : 'TIME_SERIES_WEEKLY', 'symbol' : 'TSLA', 'apikey' : apikey}

#Retrieve stock data for Tesla
r = requests.get(url = URL, params=PARAMS)
teslaData = r.json()

#Retrieve stock data for Twitter
PARAMS['symbol'] = 'TWTR'
r = requests.get(url = URL, params=PARAMS)
twitterData = r.json()

#Retrieve stock data for Amazon
PARAMS['symbol'] = 'AMZN'
r = requests.get(url = URL, params=PARAMS)
amazonData = r.json()

#Insert Tesla stock data into sqlite database
for dates in teslaData['Weekly Time Series']:
    cur.execute(''' INSERT INTO stocks VALUES (?, ?, ?, ?, ?, ?, ?)''',
        [dates, 'TSLA', teslaData['Weekly Time Series'][dates]['1. open'], teslaData['Weekly Time Series'][dates]['2. high'],
        teslaData['Weekly Time Series'][dates]['3. low'], teslaData['Weekly Time Series'][dates]['4. close'], teslaData['Weekly Time Series'][dates]['5. volume']])
    con.commit()

#Insert Twitter stock data into sqlite database
for dates in twitterData['Weekly Time Series']:
    cur.execute(''' INSERT INTO stocks VALUES (?, ?, ?, ?, ?, ?, ?)''',
        [dates, 'TWTR', twitterData['Weekly Time Series'][dates]['1. open'], twitterData['Weekly Time Series'][dates]['2. high'],
        twitterData['Weekly Time Series'][dates]['3. low'], twitterData['Weekly Time Series'][dates]['4. close'], twitterData['Weekly Time Series'][dates]['5. volume']])
    con.commit()

#Insert Amazon stock data into sqlite database
for dates in amazonData['Weekly Time Series']:
    cur.execute(''' INSERT INTO stocks VALUES (?, ?, ?, ?, ?, ?, ?)''',
        [dates, 'AMZN', amazonData['Weekly Time Series'][dates]['1. open'], amazonData['Weekly Time Series'][dates]['2. high'],
        amazonData['Weekly Time Series'][dates]['3. low'], amazonData['Weekly Time Series'][dates]['4. close'], amazonData['Weekly Time Series'][dates]['5. volume']])
    con.commit()

#Close sqlite connection
con.close()