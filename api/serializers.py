from rest_framework import serializers
from api.models import Note

# The NoteSerializer
# serializing and deserializering Note instances into representations such as json
class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = ['id','title','content']