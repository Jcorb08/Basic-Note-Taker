from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from api.models import Note

# Create your tests here.
class api_app_test_note_api(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.note1 = Note.objects.create(title="note1",content="note1 content")
        cls.note2 = Note.objects.create(title="note2",content="note2 content") 
        cls.note3 = Note.objects.create(title="note3",content="note3 content")  

    def test_get_all(self):
        response = self.client.get("")
        self.assertEqual(response.status_code,status.HTTP_200_OK)
        self.assertEqual(len(response.data),Note.objects.count())

    def test_create(self):
        response = self.client.post("",{"title":"createTest","content":"createTestContent"},format="json")
        self.assertEqual(response.status_code,status.HTTP_201_CREATED) 
        self.assertEqual(Note.objects.get(pk=4).title, "createTest")

    def test_get_single(self):
        response = self.client.get("/1")
        self.assertEqual(response.status_code,status.HTTP_200_OK) 
        self.assertEqual(response.data['title'], "note1")
    
    def test_get_single_fail(self):
        response = self.client.get("/test")
        self.assertEqual(response.status_code,status.HTTP_404_NOT_FOUND) 

    def test_update_single(self):
        response = self.client.put("/1",{"title":"createTest","content":"createTestContent"},format="json")
        self.assertEqual(response.status_code,status.HTTP_200_OK) 
        self.assertEqual(response.data['title'], "createTest")
    
    def test_delete_single(self):
        response = self.client.delete("/1")
        self.assertEqual(response.status_code,status.HTTP_204_NO_CONTENT) 
        self.assertFalse(Note.objects.filter(pk=1).exists())