from api.models import Note
from api.serializers import NoteSerializer
from rest_framework import generics

# https://www.django-rest-framework.org/api-guide/generic-views/#concrete-view-classes
# API methods without a id in the URL
class NotesList(generics.ListCreateAPIView):
    """
    Notes List \n
    - Create a Note (POST) \n
    - Read all Notes (GET) \n
    Add a id to the url to access Notes Detail.
    """
    serializer_class=NoteSerializer
    queryset=Note.objects.all()

# API methods with a id in the URL
class NotesDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Notes Detail \n
    - Update a Note (PUT) \n
    - Read a Note (GET) \n
    - Delete a Note (DELETE) \n
    Remove the id from the url to access Notes List. 
    """
    serializer_class=NoteSerializer
    queryset=Note.objects.all()



# An example of how to do it without generics
# https://www.django-rest-framework.org/tutorial/3-class-based-views/
# class Note_API(APIView):
#     """
#     Notes API
#     - Create a Note (POST)
#     - Read a Note (GET)
#      - Either with ID input or no input for all
#     - Update a Note (PUT)
#     - Delete a Note (DELETE)
    
#     """
    
#     # Helper function to grab a single Note
#     def get_single(self, pk):
#         try:
#             return Note.objects.get(pk=pk)
#         except Note.DoesNotExist:
#             raise Http404('Note does not exist')
    
#     # Get all Notes or a single by ID
#     def get(self, request, pk=None, format=None):
#         """
#         Get all Notes or a Single by ID
#         """
#         if pk is None:
#             # get all Notes
#             notes  = Note.objects.all()
#             serializer = NoteSerializer(notes,many=True)
#         else:
#             # get single Note
#             note = self.get_single(pk)
#             serializer = NoteSerializer(note)
#         return Response(serializer.data)
    
#     # Create new Note
#     def post(self, request, format=None):
#         """
#         Create a new Note, with a 'title' and 'content'
#         """
#         serializer = NoteSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     # Update existing Note
#     def put(self, request, pk, format=None):
#         """
#         Update an existing Note, with a 'id' and a 'title' or 'content'
#         """
#         note = self.get_single(pk)
#         serializer = NoteSerializer(note,data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     # Delete existing Note
#     def delete(self, request, pk, format=None):
#         """
#         Delete an existing note with an ID
#         """
#         note = self.get_single(pk)
#         note.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)