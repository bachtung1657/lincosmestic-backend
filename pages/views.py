# pages/views.py

from rest_framework import viewsets, permissions
from .models import Page
from .serializers import PageSerializer

class PageViewSet(viewsets.ReadOnlyModelViewSet):
    """API endpoint để lấy nội dung các trang tĩnh."""
    queryset = Page.objects.filter(is_published=True)
    serializer_class = PageSerializer
    lookup_field = 'slug'
    permission_classes = [permissions.AllowAny]