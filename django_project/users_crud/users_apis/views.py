from rest_framework import generics
from .models import users
from .serializers import NoteSerializer
class NoteList(generics.ListCreateAPIView):
    queryset = users.objects.all()
    serializer_class = NoteSerializer
class NoteDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = users.objects.all()
    serializer_class = NoteSerializer