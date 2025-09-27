from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PageViewSet

# 1. Khởi tạo router
router = DefaultRouter()

# 2. Đăng ký PageViewSet với router
#    'pages' là tiền tố của URL (ví dụ: /api/v1/pages/)
#    'page' là basename để Django tự tạo tên cho các URL
router.register(r'pages', PageViewSet, basename='page')

# 3. urlpatterns phải bao gồm router.urls
urlpatterns = [
    path('', include(router.urls)),
]