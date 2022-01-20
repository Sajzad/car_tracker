from rest_framework import serializers
from django.contrib.auth.models import User

from base.models import(
	Car,
	Operator,
	City,
	LatLong,
	Assignment
)


class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = ('username',)


class CarSerializer(serializers.ModelSerializer):
	class Meta:
		model = Car
		fields = '__all__'


class OperatorSerializer(serializers.ModelSerializer):
	class Meta:
		model = Operator
		fields = '__all__'

class CitySerializer(serializers.ModelSerializer):
	class Meta:
		model = City
		fields = '__all__'

class AssignmentSerializer(serializers.ModelSerializer):
	class Meta:
		model = City
		fields = '__all__'

class ReportsSerializer(serializers.ModelSerializer):
	class Meta:
		model = Assignment
		depth = 1
		fields = '__all__'
class LatLongsSerializer(serializers.ModelSerializer):
	class Meta:
		model = LatLong
		exclude = ('assignment','id')

class TrackingSerializer(serializers.ModelSerializer):
	class Meta:
		model = Assignment
		depth = 2
		fields = ('assignment_items', 'car', 'operator', 'city')

