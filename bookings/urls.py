from django.urls import path, include
from rest_framework import routers

from bookings import views

router = routers.DefaultRouter()
router.register(r'services', views.ServiceViewSet)
router.register(r'appointments', views.AppointmentViewSet)
router.register(r'reviews', views.ReviewViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

