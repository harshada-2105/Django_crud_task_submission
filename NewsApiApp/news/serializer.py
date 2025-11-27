from rest_framework import serializers
from .models import *

class CategorySerializer(serializers.ModelSerializer):
    news_count = serializers.SerializerMethodField()
    class Meta:
        model = Category
        fields = ['id', 'name', 'description', 'slug', 'color_code', 'is_active', 'created_at', 'news_count']
        read_only_fields = ['id', 'slug', 'created_at']
    def get_news_count(self, obj):
        return obj.news_articles.count()