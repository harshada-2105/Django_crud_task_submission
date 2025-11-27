from rest_framework import serializers
from .models import Movie

class MovieSerializers(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = "__all__"
        read_only_fields = ["created_as", "updated_as"]