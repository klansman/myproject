from django.shortcuts import render
from django.http import HttpResponse
import urllib.request, json



# Create your views here.
def index(request):
    #get the inputed city from the html file
    if request.method =='POST':
        city = request.POST['city']
        #get the conditions of the city from the openweathermap using the api key and save the values in the variable res 
        res = urllib.request.urlopen('https://api.openweathermap.org/data/2.5/forecast?q='+city+'&APPID=cf646e05484370594fd5227c09d31542').read()
        #load the weather data from res to var jason_data whch saves the weather data as a json file
        json_data = json.loads(res)
        #Now we have to convert the weather data to a dictionary so that django can read it
        data={
           "country_code":str(json_data['sys']['country']),
           "coordinates":str(json_data['coord']['lon']+''+['coord']['lat']),
           "temp":str(json_data['main']['temp']),
           "pressure":str(json_data['main']['pressure']),
           "humidity":str(json_data['main']['humidity']),
        }
    else:
     data={}
    return render(request, 'index.html', {'data':data}, {'city':city})
