from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework import permissions

from django.contrib.auth.models import User
from rest_framework.parsers import MultiPartParser, FormParser
from django.contrib.auth.base_user import BaseUserManager

from .serializers import (
    CarSerializer,
    OperatorSerializer,
    CitySerializer,
    AssignmentSerializer,
    LatLongsSerializer,
    TrackingSerializer,
    UserSerializer,
    ReportsSerializer
)
from base.models import(
    Car,
    Operator,
    City,
    LatLong,
    Assignment
)


class ManagerListApiView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def get(self, request):
        try:
            managers = User.objects.filter(is_superuser=True)
            serializer = UserSerializer(managers, many=True)
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            res = {"msg": str(e), "data": None, "success": False}
            return Response(data=res, status=status.HTTP_400_BAD_REQUEST) 


class CarListApiView(APIView):
    # add permission to check if user is authenticated
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        data = request.data
        serializer = CarSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            cars = Car.objects.all()
            serializer = CarSerializer(cars, many=True)
            data = {
                'cars': serializer.data
            }

            return Response(data, status=status.HTTP_201_CREATED)

    def get(self, request):
        """
        List all the car items
        """
        cars = Car.objects.all()
        serializer = CarSerializer(cars, many=True)

        data = {
            'cars':serializer.data
        }
        return Response(data, status=status.HTTP_200_OK)


class CarCRUDView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, car_id):
        try:
            car_info = Car.objects.get(id=car_id)
            serializer = CarSerializer(car_info)
            data = {
                "car":serializer.data
            }
            return Response(data=data, status=status.HTTP_200_OK)
        except Exception as e:
            # print(serializer.errors)
            res = {"msg": str(serializer.errors), "data": None, "success": False}
            return Response(data=res, status=status.HTTP_400_BAD_REQUEST)
    def put(self, request, car_id):
        car_info = {
            "id":car_id,
            "car":request.data.get('car')
        }
        car_obj = Car.objects.get(id=car_id)
        serializer = CarSerializer(instance=car_obj, data=car_info)
        if serializer.is_valid():
            serializer.save()
            res = {"msg": 'Car name updated successfully', "data": None, "success": True}
            return Response(data=res, status=status.HTTP_200_OK)
        res = {"msg": str(serializer.errors), "data": None, "success": False}
        return Response(data=res, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, car_id):
        print(car_id)
        try:
            car_obj = Car.objects.filter(id=car_id)
            car_obj.delete()

            res = {"msg": 'Car deleted successfully', "data": None, "success": True}
            return Response(data=res, status=status.HTTP_200_OK)
        except Exception as e:
            res = {"msg": str(e), "data": None, "success": False}
            return Response(data=res, status=status.HTTP_400_BAD_REQUEST) 

class UsersListApiView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        operators = Operator.objects.all()
        serializer = OperatorSerializer(operators, many=True)
        
        data = {
            "users" : serializer.data
        }
        return Response(data=data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = OperatorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            
            res = {"msg": 'Operator created successfully', "data": None, "success": True}
            return Response(data=res, status=status.HTTP_200_OK)
        res = {"msg": str(serializer.errors), "data": None, "success": False}
        return Response(data=res, status=status.HTTP_400_BAD_REQUEST)

class UserCRUDView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, user_id):
        user_info = Operator.objects.get(id=user_id)
        serializer = OperatorSerializer(user_info)
        data = {
            "user":serializer.data
        }
        return Response(data=data, status=status.HTTP_200_OK)

    def put(self, request, user_id):
        user_info = {
            "id":user_id,
            "name":request.data.get('user')
        }
        user_obj = Operator.objects.get(id=user_id)
        serializer = OperatorSerializer(instance=user_obj, data=user_info)
        if serializer.is_valid():
            serializer.save()
            res = {"msg": 'Operator updated successfully', "data": None, "success": True}
            return Response(data=res, status=status.HTTP_200_OK)

        print(serializer.errors)
        res = {"msg": str(serializer.errors), "data": None, "success": False}
        return Response(data=res, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, user_id):
        print(user_id)
        try:
            user_obj = Operator.objects.filter(id=user_id)
            user_obj.delete()

            res = {"msg": 'Car deleted successfully', "data": None, "success": True}
            return Response(data=res, status=status.HTTP_200_OK)
        except Exception as e:
            res = {"msg": str(e), "data": None, "success": False}
            return Response(data=res, status=status.HTTP_400_BAD_REQUEST) 


class CityListApiView(APIView):

    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        cities = City.objects.all()
        serializer = CitySerializer(cities, many=True)
        
        data = {
            "cities" : serializer.data
        }
        return Response(data=data, status=status.HTTP_200_OK)

    def post(self, request):

        serializer = CitySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()

            res = {"msg": 'City created successfully', "data": None, "success": True}
            return Response(data=res, status=status.HTTP_200_OK)
        print(serializer.errors)
        res = {"msg": str(serializer.errors), "data": None, "success": False}
        return Response(data=res, status=status.HTTP_400_BAD_REQUEST)

class CityCRUDView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, city_id):
        city_info = City.objects.get(id=city_id)
        serializer = OperatorSerializer(city_info)
        data = {
            "city":serializer.data
        }
        return Response(data=data, status=status.HTTP_200_OK)

    def put(self, request, city_id):
        city_info = {
            "id":city_id,
            "name":request.data.get('city')
        }
        print(city_info)
        city_obj = City.objects.get(id=city_id)
        serializer = CitySerializer(instance=city_obj, data=city_info)
        if serializer.is_valid():
            serializer.save()
            res = {"msg": 'City updated successfully', "data": None, "success": True}
            return Response(data=res, status=status.HTTP_200_OK)

        print(serializer.errors)
        res = {"msg": str(serializer.errors), "data": None, "success": False}
        return Response(data=res, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, city_id):
        print(city_id)
        try:
            city_obj = City.objects.filter(id=city_id)
            city_obj.delete()

            res = {"msg": 'City deleted successfully', "data": None, "success": True}
            return Response(data=res, status=status.HTTP_200_OK)
        except Exception as e:
            res = {"msg": str(e), "data": None, "success": False}
            return Response(data=res, status=status.HTTP_400_BAD_REQUEST) 


class AssignmentView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        try:
            user_id = request.data.get('operator_id')
            car_id = request.data.get('car_id')
            city_id = request.data.get('city_id')
            Assignment.objects.create(

                operator_id = user_id,
                car_id = car_id,
                city_id = city_id
            )
            op_obj = Operator.objects.get(id=user_id)
            if not User.objects.filter(username=op_obj.unique_name).exists():
                User.objects.create_user(username=op_obj.unique_name, password=str(op_obj.code))           
            res = {"msg": f'Login code for {op_obj.unique_name} is {op_obj.code}', "data": None, "success": True}
            return Response(data=res, status=status.HTTP_200_OK)
        except Exception as e:
            print(e)
            res = {"msg": str(e), "data": None, "success": False}
            return Response(data=res, status=status.HTTP_400_BAD_REQUEST)

class ReportsApiView(APIView):
    
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        reports = Assignment.objects.all()
        serializer = ReportsSerializer(reports, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        assignment_id = request.data.get('assignment_id')

        try:
            lat_lng_obj = LatLong.objects.filter(assignment_id=assignment_id).order_by('-timestamp')
            serializer = LatLongsSerializer(lat_lng_obj, many=True)

            return Response(data=serializer.data[:20], status=status.HTTP_200_OK)
        except Exception as e:
            print(e)
            res = {"msg": str(e), "data": None, "success": False}
            return Response(data=res, status=status.HTTP_400_BAD_REQUEST)

class TrackingApiView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        print("get")
        try:
            trackings = Assignment.objects.all()
            serializer = TrackingSerializer(trackings, many=True)
            print(serializer.data)
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            print(e)
            res = {"msg": str(e), "data": None, "success": False}
            return Response(data=res, status=status.HTTP_400_BAD_REQUEST)

    def post(self, request):
        assignment_id = request.data.get('assignment_id')

        try:
            lat_lng_obj = LatLong.objects.filter(assignment_id=assignment_id).order_by('-timestamp')
            serializer = LatLongsSerializer(lat_lng_obj, many=True)
            data = serializer.data[0]
            return Response(data=data, status=status.HTTP_200_OK)
        except Exception as e:
            print(e)
            res = {"msg": str(e), "data": None, "success": False}
            return Response(data=res, status=status.HTTP_400_BAD_REQUEST)

