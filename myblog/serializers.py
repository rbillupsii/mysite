from .models import Post, Category
from rest_framework import serializers

class post_serializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('title', 'text', 'author', 'created_date', 'modified_date', 'published_date')

class category_serializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('name', 'description', 'posts')