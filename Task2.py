import requests
import sqlite3

con = sqlite3.connect('stock.db')
cur = con.cursor()

cur.execute('''DROP TABLE IF EXISTS stocks''')
cur.execute(''' CREATE TABLE stocks ( DATE DATE, STOCK TEXT, OPEN REAL, HIGH REAL, LOW REAL, CLOSE REAL, VOLUME INT)''')

URL = 'https://www.alphavantage.co/query'
apikey = '6053SNAFDVUQVJVB'


#Symbol names found by googling stock names
PARAMS = {'function' : 'TIME_SERIES_WEEKLY', 'symbol' : 'TSLA', 'apikey' : apikey}
r = requests.get(url = URL, params=PARAMS)
teslaData = r.json()

PARAMS['symbol'] = 'TWTR'
r = requests.get(url = URL, params=PARAMS)
twitterData = r.json()

PARAMS['symbol'] = 'AMZN'
r = requests.get(url = URL, params=PARAMS)
amazonData = r.json()

for dates in teslaData['Weekly Time Series']:
    cur.execute(''' INSERT INTO stocks VALUES (?, ?, ?, ?, ?, ?, ?)''',
        [dates, 'TSLA', teslaData['Weekly Time Series'][dates]['1. open'], teslaData['Weekly Time Series'][dates]['2. high'],
        teslaData['Weekly Time Series'][dates]['3. low'], teslaData['Weekly Time Series'][dates]['4. close'], teslaData['Weekly Time Series'][dates]['5. volume']])
    con.commit()

for dates in twitterData['Weekly Time Series']:
    cur.execute(''' INSERT INTO stocks VALUES (?, ?, ?, ?, ?, ?, ?)''',
        [dates, 'TWTR', twitterData['Weekly Time Series'][dates]['1. open'], twitterData['Weekly Time Series'][dates]['2. high'],
        twitterData['Weekly Time Series'][dates]['3. low'], twitterData['Weekly Time Series'][dates]['4. close'], twitterData['Weekly Time Series'][dates]['5. volume']])
    con.commit()

for dates in amazonData['Weekly Time Series']:
    cur.execute(''' INSERT INTO stocks VALUES (?, ?, ?, ?, ?, ?, ?)''',
        [dates, 'AMZN', amazonData['Weekly Time Series'][dates]['1. open'], amazonData['Weekly Time Series'][dates]['2. high'],
        amazonData['Weekly Time Series'][dates]['3. low'], amazonData['Weekly Time Series'][dates]['4. close'], amazonData['Weekly Time Series'][dates]['5. volume']])
    con.commit()

con.close()
