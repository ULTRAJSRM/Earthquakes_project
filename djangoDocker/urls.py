from django.contrib import admin
from django.urls import path
from rest_framework.routers import DefaultRouter
from earthquakes_app.views import EarthquakeViewSet

router = DefaultRouter()

router.register(r'earthquakes', EarthquakeViewSet)

urlpatterns = router.urls

urlpatterns += [
    path('admin/', admin.site.urls),
]
