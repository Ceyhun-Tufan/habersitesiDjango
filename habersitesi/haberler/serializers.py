from rest_framework import serializers
from .models import Category, News, Tag

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'slug']  # İhtiyacınıza göre alanları seçebilirsiniz.

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'name', 'slug']

class NewsSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)  # İlişkili model için
    tags = TagSerializer(many=True, read_only=True)  # Many-to-Many için
    author = serializers.StringRelatedField(read_only=True)  # Yazarın adı gösterilecek.

    class Meta:
        model = News
        fields = [
            'id', 'title', 'subtitle', 'slug', 'content', 'author',
            'published_date', 'created_at', 'updated_at', 'category',
            'tags', 'image', 'view_count', 'is_featured', 'source'
        ]


# Paging sırasında az detaylı gösterim için

class NewsUndetailedSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)  # İlişkili model için
    tags = TagSerializer(many=True, read_only=True)  # Many-to-Many için
    author = serializers.StringRelatedField(read_only=True)  # Yazarın adı gösterilecek.

    class Meta:
        model = News
        fields = [
            'id', 'title', 'subtitle', 'slug', 'author',
            'published_date', 'category',
            'tags', 'image', 'view_count', 'is_featured'
        ]