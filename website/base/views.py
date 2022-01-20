import geocoder
import folium
import random

from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

from .models import (
	Operator, 
	Assignment, 
	LatLong)


def home_view(request):
	# location = geocoder.osm("UK")
	if request.user.is_authenticated:
		map_obj = ""
		operator = ''

		try:
			operator = Operator.objects.filter(unique_name=request.user.username)[0].name
		except:
			pass
		# location = geocoder.ip('144.48.116.171')
		lat_lng = LatLong.objects.filter(assignment__operator__unique_name=request.user.username).order_by('-timestamp')
		if lat_lng.exists():
			lat = lat_lng[0].lat
			lng = lat_lng[0].lng
			map_obj = folium.Map([lat, lng], zoom_start=2)
			folium.Marker(
				[lat, lng], 
				tooltip = 'click here',
				popup = f'{lat} {lng} {operator}').add_to(map_obj)
			map_obj = map_obj._repr_html_()
		context = {
			'operator':operator,
			"map":map_obj
		}
		return render(request,'base/home.html', context)
	else:
		return redirect('account:login')

@login_required
def cars_view(request):
	if request.user.is_superuser:
		if request.is_ajax():
			print("ajax")
		context = {
			
		}
		return render(request, 'base/cars.html', context)
	else:
		return redirect('base:home')

@login_required
def user_view(request):
	if request.user.is_superuser:
		pass
		return render(request, 'base/user.html')
	else:
		return redirect('base:home')

@login_required
def city_view(request):
	if request.user.is_superuser:
		pass
		return render(request, 'base/city.html')
	else:
		return redirect('base:home')

@login_required
def reports_view(request):
	if request.user.is_superuser:

		return render(request, 'base/reports.html')
	else:
		return redirect('base:home')

@login_required
def tracking_view(request):
	if request.user.is_superuser:

		return render(request, 'base/tracking.html')
	else:
		return redirect('base:home')
