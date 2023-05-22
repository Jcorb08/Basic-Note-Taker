from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from api.models import Note

# Create your tests here.
class api_app_test_note_api(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.note1 = Note.objects.create(title='note1',content='note1 content')
        cls.note2 = Note.objects.create(title='note1',content='note1 content') 
        cls.note3 = Note.objects.create(title='note1',content='note1 content')  

    def test_get_all(self):
        response = self.client.get('')
        self.assertEqual(response.status_code,status.HTTP_200_OK)
        self.assertEqual(len(response.data),Note.objects.count())

    def test_create(self):
        response = self.client.post('',{"title":"createTest","content":"createTestContent"},format='json')
        self.assertEqual(response.status_code,status.HTTP_200_OK)
        #self.assertEqual()