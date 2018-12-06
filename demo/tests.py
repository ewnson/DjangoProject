from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework.views import status
from .models import Contacts
from .serializers import ContactsSerializer

# tests for views


class BaseViewTest(APITestCase):
    client = APIClient()

    @staticmethod
    def create_contact(name="", number=""):
        if name != "" and number != "":
            Contacts.objects.create(name=name, number=number)

    def setUp(self):
        # add test data
        self.create_contact("Eric", "0703302903")
        self.create_song("User", "0711111111")
        self.create_song("Safcom", "0700000000")
        self.create_song("Person", "0799999999")


class GetAllContactsTest(BaseViewTest):

    def test_get_all_contacts(self):
        """
        This test ensures that all songs added in the setUp method
        exist when we make a GET request to the songs/ endpoint
        """
        # hit the API endpoint
        response = self.client.get(
            reverse("contacts-all", kwargs={"version": "v1"})
        )
        # fetch the data from db
        expected = Songs.objects.all()
        serialized = ContactsSerializer(expected, many=True)
        self.assertEqual(response.data, serialized.data)
self.assertEqual(response.status_code, status.HTTP_200_OK)