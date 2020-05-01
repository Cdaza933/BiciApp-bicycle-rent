from django.conf.urls import url

from bicycles.views import BicycleViewSet
from rents.views import RentBicycle

urlpatterns = [
    url(r'^', RentBicycle.as_view(), name='rent'),
]