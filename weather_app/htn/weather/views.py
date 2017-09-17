# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render
from .models import Weather
import requests, time, math

# Create your views here.
def index(request):
	var = 'index.html'
	return render(request, var, )


def result(request):
	#creating the API request
	city = request.POST['city']
	country = request.POST['country']
	r = requests.get("http://api.openweathermap.org/data/2.5/forecast/daily?q="+city+","+country+"ca&cnt=16&units=metric&APPID=48a8c111df81fd58c7240c8f432660e7")
	data = r.json()

	#getting supplied date to UNIX
	date_time = request.POST['date']
	pattern = '%Y-%m-%d'
	epoch = int(time.mktime(time.strptime(date_time, pattern)))
	#getting days away
	day = int(math.floor(((epoch - math.floor(time.time()))/86400))+1)

	#condition for if rain or clear
	cond = data["list"][day]["weather"][0]["main"]
	if cond == "Rain":
		precipitation = True
	else:
		precipitation = False

	#create variables for database (city is created above, date = epoch)
	event = request.POST['event']
	conditions = precipitation
	morn_temp = data["list"][day]["temp"]["morn"]
	day_temp = data["list"][day]["temp"]["day"]
	night_temp = data["list"][day]["temp"]["night"]

	#creating instance 
	q = Weather(event=event, location=city, conditions=conditions, morn_temp=morn_temp, day_temp=day_temp, night_temp=night_temp, date=epoch)
	q.save()

	if conditions == True:
		var = 'result.html'
		con = 'Precipitation'
	else:
		var = 'result1.html'
		con = 'Clear Skies'

	context = {
		'event': event,
		'morn_temp': int(morn_temp),
		'day_temp': int(day_temp),
		'night_temp': int(night_temp),
		'conditions': con,
	}

	return render(request, var, context)




