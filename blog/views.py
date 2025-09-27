from rest_framework import viewsets, permissions
from .models import Post, Category
from .serializers import PostSerializer, CategorySerializer

class PostViewSet(viewsets.ReadOnlyModelViewSet):
    """API endpoint để xem danh sách bài viết và chi tiết bài viết."""
    queryset = Post.objects.filter(status=Post.Status.PUBLISHED)
    serializer_class = PostSerializer
    lookup_field = 'slug'
    permission_classes = [permissions.AllowAny]

class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    """API endpoint để xem các danh mục bài viết."""
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    lookup_field = 'slug'
    permission_classes = [permissions.AllowAny]