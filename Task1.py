import requests

#Set the time and date range to 1pm, 2nd July, 2000
startdate = "2000-07-02T13:00:00"
enddate = "2000-07-02T13:59:59"

#Values below retrieved from data tool https://www.ncdc.noaa.gov/cdo-web/datatools
datasetID = 'PRECIP_HLY' #dataset ID for 15 minute precipitation is 'PRECIP_15' which also returns no results
datatypeID = 'HPCP'   #datatype ID - precipitation in inches  
locationID = 'FIPS:15' #locationID for Hawaii
token = {'token' : 'aPztadhIyezpvJutqLeJSxTFazwTkDPI'}
PARAMS = {'datasetid': datasetID, 'locationid' : locationID, 'units':'metric', 'startdate': startdate, 'enddate' : enddate, 'limit' : 1000, 'includemetadata' : 'false'}

#Find dataset ID of hourly precipitation
URL = "https://www.ncdc.noaa.gov/cdo-web/api/v2/data"
response = requests.get(url = URL, headers = token, params=PARAMS)

#Convert request data to json
data = response.json()
print(data)

#No data for 1pm 02/07/2000

