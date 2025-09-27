from rest_framework import serializers
from .models import Post, Category

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['name', 'slug']

class PostSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    author = serializers.StringRelatedField(read_only=True)
    
    # Đảm bảo URL ảnh là URL đầy đủ
    cover_image = serializers.ImageField(use_url=True)

    class Meta:
        model = Post
        fields = [
            'id', 'title', 'slug', 'author', 'excerpt', 'content', 
            'cover_image', 'category', 'created_at'
        ]
        lookup_field = 'slug'