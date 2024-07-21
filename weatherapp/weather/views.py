from django.shortcuts import render
from django.http import HttpResponse
import urllib.request, json



# Create your views here.
def index(request):
    #initializing the city and data variables to empty strings and an empty dictionary respectively
    city = ''
    data = {}   
    #get the inputed city from the html file
    if request.method =='POST':
        city = request.POST['city']
        #get the conditions of the city from the openweathermap using the api key and save the values in the variable res 
        res = urllib.request.urlopen('https://api.openweathermap.org/data/2.5/forecast?q='+city+'&APPID=cf646e05484370594fd5227c09d31542').read()
        #load the weather data from res to var jason_data whch saves the weather data as a json file
        json_data = json.loads(res)
        #get the weather data for today (0 index) from the list of forecasts and save it in f
        f = json_data['list'][0]
        #Now we have to convert the weather data to a dictionary so that django can read it
        data = {
           "country_code":str(json_data['city']['country']),
           "coordinates":str(json_data['city']['coord']),
           "temp":str(f['main']['temp']),
           "pressure":str(f['main']['pressure']),
           "humidity":str(f['main']['humidity'])
        }
    else:
        data={}
    return render(request, 'index.html', {'city':city, 'data':data })
