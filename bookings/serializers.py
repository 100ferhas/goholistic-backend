from rest_framework import serializers

from bookings.models import Service, Appointment, Review


class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        exclude = ['user']
        read_only_fields = ['id']


class AppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        exclude = ['user', 'customer']
        read_only_fields = [
            'id',
            'service_name',
            'service_description',
            'service_duration',
            'service_price',
            'service_type',
            'date',
            'status',
        ]


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        exclude = ['user', 'customer']
        read_only_fields = ['id']
