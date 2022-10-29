from rest_framework import viewsets, permissions
from rest_framework.decorators import action

from bookings.models import Service, Review, Appointment
from bookings.serializers import ServiceSerializer, ReviewSerializer, AppointmentSerializer


class ServiceViewSet(viewsets.ModelViewSet):
    http_method_names = ['get', 'post', 'patch']
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class ReviewViewSet(viewsets.ModelViewSet):
    http_method_names = ['get', 'post', 'patch']
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class AppointmentViewSet(viewsets.ModelViewSet):
    http_method_names = ['get', 'post']
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    @action(detail=True, methods=['patch']) # todo
    def request_cancel(self, request, pk=None):
        pass
