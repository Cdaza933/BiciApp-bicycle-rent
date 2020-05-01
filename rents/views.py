from datetime import datetime, timezone

from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from bicycles.models import Bicycle
from rents.models import Rent


class RentBicycle(APIView):
    def post(self, request, format=None):
        data = request.data
        bicycle = Bicycle.objects.get(pk=data.pop('bicycle_id'))
        data['bicycles'] = bicycle
        rent = Rent.objects.create(**data)
        return Response(rent.pk, status=status.HTTP_201_CREATED)

    def put(self, request, *args, **kwargs):
        data = request.data
        rent_ended_at = datetime.now(timezone.utc)
        rent = Rent.objects.get(pk=data['id'])
        rent.rented_ended_at = rent_ended_at
        rent.save()
        total_time = rent.rented_ended_at - rent.rented_at
        total_minutes = total_time.total_seconds()/60
        total_value = rent.bicycle.price * total_minutes
        response_data = dict(price=rent.bicycle.price,total_minutes=total_minutes,total_value=total_value)
        return Response(data=response_data, status=status.HTTP_200_OK)


