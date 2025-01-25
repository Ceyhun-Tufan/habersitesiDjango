from rest_framework import serializers
from .models import Category, News, Tag
from .tasks import categoryAi

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
            'created_at', 'updated_at', 'category',
            'tags', 'image', 'view_count', 'is_featured', 'source'
        ]


class NewsAddSerializer(serializers.ModelSerializer):
    category = CategorySerializer(required=False)
    content = serializers.CharField(required=True)
    
    class Meta:
        model = News
        fields = [
            'title', 'subtitle', 'content', 'author',
            'category', 'tags', 'image', 'is_featured', 'source'
        ]

    def create(self, validated_data):

        content = validated_data.get('content')
        validated_data["category"] = None

        instance = super().create(validated_data)

        categoryAi.delay(content,instance.id)

        return instance



# Paging sırasında az detaylı gösterim için

class NewsUndetailedSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)  # İlişkili model için
    tags = TagSerializer(required=False,many=True, read_only=True)  # Many-to-Many için
    author = serializers.StringRelatedField(read_only=True)  # Yazarın adı gösterilecek.

    class Meta:
        model = News
        fields = [
            'id', 'title', 'subtitle', 'slug', 'author',
            'category','created_at',
            'tags', 'image', 'view_count', 'is_featured'
        ]
