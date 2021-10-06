from django.urls import reverse_lazy
from rest_framework import status
from rest_framework.test import APITestCase

from tests.factories.user import UserFactory


class UserViewSetTest(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = UserFactory()
        cls.detail_url = reverse_lazy('user-detail', kwargs={'pk': cls.user.id})

    def test_retrieve_user(self):
        response = self.client.get(self.detail_url)

        assert response.status_code == status.HTTP_200_OK
        assert response.data['email'] == self.user.email
