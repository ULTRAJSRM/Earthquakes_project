from django.shortcuts import render
from rest_framework import viewsets
from .models import Earthquake
from .serializers import EarthquakeSerializer

class EarthquakeViewSet(viewsets.ModelViewSet):
    serializer_class = EarthquakeSerializer
    queryset = Earthquake.objects.all()

