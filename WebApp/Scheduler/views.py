from django.shortcuts import render
from .models import ScheduleObject
import requests

def index(request):
	return render(request, 'Scheduler/index.html')

def schedule(request):
	r = request.POST
	requests.post("http://192.241.177.248:3000/server", data={"start_time":r['start_time']})
	return render(request, 'Scheduler/index.html')
	