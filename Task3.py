from flask import Flask, jsonify, send_from_directory
from flask_restful import Resource, Api
import sqlite3
import matplotlib.pyplot as plt
from dateutil import parser

#Set up API
app = Flask(__name__)
api = Api(app)

#Debugging mode helpful for identifying bugs
app.config["DEBUG"] = True

#Function for JSON format conversion sourced from https://programminghistorian.org/en/lessons/creating-apis-with-python-and-flask
def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d

#Homepage of server
@app.route('/', methods=['GET'])
def home():
    return "<h1>Julia Shan's Stocks API</h1>"

#Function for retrieving stocks names from SQLite database: stock.db
class stocks(Resource):
    def get(self):
        conn = sqlite3.connect('stock.db') 
        conn.row_factory = dict_factory #Convert database format into json type data 
        cur = conn.cursor() 
        stock_codes = cur.execute('SELECT DISTINCT STOCK FROM stocks;').fetchall() #Fetch required columns from database
        return jsonify(stock_codes) #Return JSON object containing stock names

#Custom endpoint for Task 3, Part 2: a graph of volume over time for each stock using matplotlib
class graph(Resource):
    def get(self):
        #Create connection with database
        conn = sqlite3.connect('stock.db')
        cur = conn.cursor()

        #Fetch volume data for Tesla stock
        tesla = cur.execute("SELECT DATE, VOLUME FROM stocks WHERE STOCK='TSLA' ").fetchall()
        dates = []
        values = []
        #Parse the retrieved data into date and values arrays
        for row in tesla:
            dates.append(parser.parse(row[0]))
            values.append(row[1])
        #Add the tesla data to the plot
        plt.plot_date(dates, values, '-', label ='Tesla')
        
        #Fetch volume data for Twitter stock
        twitter = cur.execute("SELECT DATE, VOLUME FROM stocks WHERE STOCK='TWTR' ").fetchall()
        dates = []
        values = []
        #Parse the retrieved data into date and values arrays
        for row in twitter:
            dates.append(parser.parse(row[0]))
            values.append(row[1])
        #Add the twitter data to the plot
        plt.plot_date(dates, values, '-', label = 'Twitter')

        #Fetch vcolume data for Amazon stock
        amazon = cur.execute("SELECT DATE, VOLUME FROM stocks WHERE STOCK='AMZN' ").fetchall()
        dates = []
        values = []
        #Parse the retrieved data into date and values arrya
        for row in amazon:
            dates.append(parser.parse(row[0]))
            values.append(row[1])
        #Add the amazon data to the plot
        plt.plot_date(dates, values, '-', label = 'Amazon')

        #Label the title and axes of the plot
        plt.title('Volume of stocks over time')
        plt.xlabel('Date (yyyy-mm-dd')
        plt.ylabel('Volume (number of stocks)')
        #Save the plot as a PNG
        plt.savefig('volume.png')
        return send_from_directory('','volume.png')

#Add the requests and endpoints to the API
api.add_resource(stocks, '/stocks')
api.add_resource(graph, '/volume')

#Run the api
app.run()