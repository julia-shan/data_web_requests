import requests

startdate = "2000-07-02T13:00:00"
enddate = "2000-07-02T13:59:59"
#Values below retrieved from data tool https://www.ncdc.noaa.gov/cdo-web/datatools
datasetID = 'PRECIP_HLY' 
datatypeID = 'HPCP'
locationID = 'FIPS:15' #locationID for Hawaii
PARAMS = {'datasetid': datasetID, 'datatypeid' : datatypeID, 'locationid' : locationID, 'startdate': startdate, 'enddate' : enddate, 'limit' : 1000, 'includemetadata' : 'false'}

#Find dataset ID of hourly precipitation
URL = "https://www.ncdc.noaa.gov/cdo-web/api/v2/data"
token = {'token' : 'aPztadhIyezpvJutqLeJSxTFazwTkDPI'}

response = requests.get(url = URL, headers = token, params=PARAMS)
data = response.json()
print(data)

