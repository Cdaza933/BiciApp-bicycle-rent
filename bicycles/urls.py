from django.conf.urls import url

from bicycles.views import BicycleViewSet

urlpatterns = [
    url(r'^', BicycleViewSet.as_view(), name='bicycle'),
]