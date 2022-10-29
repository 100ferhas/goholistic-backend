import datetime
import enum
import uuid

from django.conf import settings
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


class AppointmentStatus(enum.Enum):  # todo translate
    PENDING = "Pending"
    CONFIRMED = "Confirmed"
    CANCELED_BY_CUSTOMER = "Canceled by customer"
    CANCELED_BY_USER = "Canceled by user"

    @classmethod
    def choices(cls):
        return tuple((i.name, i.value) for i in cls)


class ServiceType(enum.Enum):  # todo translate
    ACU_JP = "Japanese acupuncture"
    ACU_SHA = "Non-insertive (Shakuju Therapy) acupuncture"
    ACU_AUR = "Auricular acupuncture"
    STR = "Stretching"
    ESSOIL = "Essential oils"
    MIND = "Mindfulness"
    FITNESS = "Fitness consultations"
    DIETARY = "Dietary consultations"
    MOXI = "Moxibustion"
    TUINA = "Tui na"
    GUASHA = "Gua sha"
    REIKI = "Reiki"
    CUPPING = "Cupping"

    @classmethod
    def choices(cls):
        return tuple((i.name, i.value) for i in cls)


class Service(models.Model):
    id = models.UUIDField(primary_key=True, null=False, blank=False, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255, null=False, blank=False)
    description = models.TextField(max_length=1000, null=False, blank=False)
    duration = models.DurationField(null=False, blank=False)
    price = models.DecimalField(null=False, blank=False, max_digits=6, decimal_places=2)
    type = models.CharField(choices=ServiceType.choices(), max_length=255, null=False, blank=False)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='services', on_delete=models.PROTECT)

    class Meta:
        verbose_name = "Service"
        verbose_name_plural = "Services"
        ordering = ['id']

    def __str__(self):
        return self.name


class Appointment(models.Model):
    id = models.UUIDField(primary_key=True, null=False, blank=False, default=uuid.uuid4, editable=False)
    service_name = models.CharField(max_length=255, null=False, blank=False)
    service_description = models.TextField(max_length=1000, null=False, blank=False)
    service_duration = models.DurationField(null=False, blank=False)
    service_price = models.DecimalField(null=False, blank=False, max_digits=6, decimal_places=2)
    service_type = models.CharField(choices=ServiceType.choices(), max_length=255, null=False, blank=False)
    date = models.DateTimeField(null=False, validators=[MinValueValidator(datetime.datetime.now().astimezone())])
    status = models.CharField(choices=AppointmentStatus.choices(), max_length=255, default=AppointmentStatus.PENDING)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT, related_name='owned_appointments')
    customer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT, related_name='appointments')

    class Meta:
        verbose_name = "Appointment"
        verbose_name_plural = "Appointments"

    def __str__(self):
        return 'Appuntamento per ' + self.service_name + ' del ' + str(self.date)  # todo translate


class Review(models.Model):
    id = models.UUIDField(primary_key=True, null=False, blank=False, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=255, null=False, blank=False)
    comment = models.TextField(null=False, blank=True)
    score = models.IntegerField(validators=[MaxValueValidator(5, "MAX!")])  # todo
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT, related_name='received_reviews')
    customer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT, related_name='given_reviews')

    def __str__(self):
        return 'Review per ' + self.user.username + ' da parte di ' + self.customer.username  # todo translate
