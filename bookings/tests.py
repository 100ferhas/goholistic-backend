import datetime

from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.db import IntegrityError
from django.test import TestCase
from rest_framework.test import APITestCase

from bookings.models import Service


class ServiceApiTestCase(APITestCase):
    """Tests for APIs integration"""
    base_path = "/services/"
    user = None
    service = None

    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create_user(username='testuser', password='12345')
        cls.service = Service.objects.create(
            name="Test Service",
            description="Test Service description",
            duration=datetime.timedelta(hours=1),
            price=49.99,
            type="ACU_JP",
            user_id=cls.user.id,
        )

    def test_list(self):
        """Test list services"""
        response = self.client.get(self.base_path)

        self.assertEqual(response.status_code, 200, 'Http status_code unexpected %s' % response.status_code)
        self.assertEqual(response.json()['count'], 1, "Results size unexpected")
        self.assertEqual(response.json()['results'][0]['name'], "Test Service")

    def test_get(self):
        """Test get single resource"""
        response = self.client.get(f"{self.base_path}{str(self.service.id)}/")

        self.assertEqual(response.status_code, 200, 'Http status_code unexpected %s' % response.status_code)
        self.assertEqual(response.json()['name'], "Test Service")

    def test_create(self):
        """Test create service"""
        data = {
            "name": "Test Service",
            "description": "Test Service description",
            "duration": "01:00:00",
            "price": 49.99,
            "type": "ACU_JP",
            "user": self.user.id,
        }

        response = self.client.post(self.base_path, data=data)
        self.assertEqual(response.status_code, 403, 'Http status_code unexpected %s' % response.status_code)

        self.client.login(username="testuser", password="12345")
        response = self.client.post(self.base_path, data=data)
        self.assertEqual(response.status_code, 201, 'Http status_code unexpected %s' % response.status_code)
        self.assertEqual(response.json()['name'], "Test Service")

    def test_update(self):
        """Test update service"""
        data = {
            "name": "Test Service",
            "description": "Test Service description updated",
            "user": 999,  # not valid, shoul be ignored!
        }

        response = self.client.patch(f"{self.base_path}{str(self.service.id)}/", data=data)
        self.assertEqual(response.status_code, 403, 'Http status_code unexpected %s' % response.status_code)

        self.client.login(username="testuser", password="12345")
        response = self.client.patch(f"{self.base_path}{str(self.service.id)}/", data=data)
        self.assertEqual(response.status_code, 200, 'Http status_code unexpected %s' % response.status_code)
        self.assertEqual(response.json()['description'], "Test Service description updated")

    def test_delete(self):
        """Test delete service"""
        response = self.client.delete(f"{self.base_path}{str(self.service.id)}/")
        self.assertEqual(response.status_code, 403, 'Http status_code unexpected %s' % response.status_code)

        self.client.login(username="testuser", password="12345")
        response = self.client.delete(f"{self.base_path}{str(self.service.id)}/")
        self.assertEqual(response.status_code, 204, 'Http status_code unexpected %s' % response.status_code)


class ServiceTestCase(TestCase):
    """Tests for model validation"""

    def test_model_validation(self):
        service = Service(
            name="Test Service",
            description="Test Service description",
            duration=datetime.timedelta(hours=1),
            price=None,
            type="ACU_JP",
            user_id=1,
        )
        self.assertRaises(ValidationError, service.full_clean, "Validation failed!")

    # Todo
    # def test_db_constraint(self):
    #     service = Service(
    #         name="Test Service",
    #         description="Test Service description",
    #         duration=datetime.timedelta(hours=1),
    #         price=49.99,
    #         type="ACU_JP",
    #         user_id=1,
    #     )
    #
    #     # with self.assertRaises(IntegrityError):
    #     try:
    #         # service.save()
    #         Service.objects.create(
    #             name="Test Service",
    #             description="Test Service description",
    #             duration=datetime.timedelta(hours=1),
    #             price=49.99,
    #             type="ACU_JP",
    #             user_id=1,
    #         )
    #     except Exception as e:
    #         print(e)
