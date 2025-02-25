from rest_framework import serializers
from .models import Category, News
from .tasks import categoryAi,summeryAi

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'slug']  # İhtiyacınıza göre alanları seçebilirsiniz.



class NewsSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)  # İlişkili model için
    author = serializers.StringRelatedField(read_only=True)  # Yazarın adı gösterilecek.

    class Meta:
        model = News
        fields = [
            'id', 'title', 'subtitle', 'slug', 'content', 'author',
            'created_at', 'updated_at', 'category',
              'image', 'view_count', 'is_featured', 'source'
        ]


class NewsAddSerializer(serializers.ModelSerializer):
    category = CategorySerializer(required=False)
    content = serializers.CharField(required=True)
    
    class Meta:
        model = News
        fields = [
            'title', 'content', 'author',
            'category', 'image', 'is_featured', 'source'
        ]

    def create(self, validated_data):

        content = validated_data.get('content')
        validated_data["category"] = None
        validated_data["subtitle"] = None

        instance = super().create(validated_data)
        summeryAi.delay(content,instance.id)
        categoryAi.delay(content,instance.id)

        return instance



# Paging sırasında az detaylı gösterim için

class NewsUndetailedSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)  # İlişkili model için
    author = serializers.StringRelatedField(read_only=True)  # Yazarın adı gösterilecek.

    class Meta:
        model = News
        fields = [
            'id', 'title', 'subtitle', 'slug', 'author',
            'category','created_at',
             'image', 'view_count', 'is_featured'
        ]
