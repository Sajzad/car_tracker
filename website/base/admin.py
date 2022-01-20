from django.contrib import admin

from .models import (
	Car,
	Operator,
	Assignment,
	LatLong,
	City
)



admin.site.register(Car)
admin.site.register(Operator)
admin.site.register(City)
admin.site.register(Assignment)
admin.site.register(LatLong)