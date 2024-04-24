from django.shortcuts import render 
import json 
import urllib.request 
'''by swati'''
def index(request): 
	if request.method == 'POST': 
		city = request.POST['city'] 

		source = urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather?q=' + city + '&units=metric&appid=a379789c8bd6009543e88586fda4692a').read()
		
		list_of_data = json.loads(source) 

		data = { 
			"city" : city,
			"country_code": str(list_of_data['sys']['country']), 
			"coordinate": str(list_of_data['coord']['lon']) + ' '
						+ str(list_of_data['coord']['lat']), 
			"temp": str(list_of_data['main']['temp']) + ' °C', 
			"pressure": str(list_of_data['main']['pressure']), 
			"humidity": str(list_of_data['main']['humidity']), 
		} 
		print(data) 
	else: 
		data ={} 
	return render(request, "main/index.html", data) 
