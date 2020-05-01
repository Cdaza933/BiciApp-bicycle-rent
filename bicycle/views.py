from django.shortcuts import render

# Create your views here.
from rest_framework.generics import CreateAPIView, ListAPIView

from bicycles.models import Bicycle
from bicycles.serializers import BicycleSerializer


class BicycleViewSet(CreateAPIView, ListAPIView):
    serializer_class = BicycleSerializer
    queryset = Bicycle.objects.all()

