from rest_framework import serializers
from .models import *

class LibrarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Library
        fields = "__all__"
        read_only_fields = ["created_at", "updated_at"]