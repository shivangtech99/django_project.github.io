from rest_framework import serializers
from .models import users

class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = users
        fields = ('id','name','email','password')