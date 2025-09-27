from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User
from core.models import TimeStampedModel, ImageProcessingModel
from ckeditor.fields import RichTextField 

class Category(TimeStampedModel):
    name = models.CharField(max_length=100, unique=True, verbose_name="Tên danh mục")
    slug = models.SlugField(max_length=120, unique=True, blank=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)
        
    class Meta:
        verbose_name = "Danh mục"
        verbose_name_plural = "Các danh mục"

class Post(TimeStampedModel, ImageProcessingModel):
    class Status(models.TextChoices):
        DRAFT = 'DF', 'Bản nháp'
        PUBLISHED = 'PB', 'Đã xuất bản'

    title = models.CharField(max_length=200, verbose_name="Tiêu đề")
    slug = models.SlugField(max_length=220, unique=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts', verbose_name="Tác giả")
    # content = models.TextField(verbose_name="Nội dung")
    content = RichTextField(verbose_name="Nội dung")
    excerpt = models.TextField(blank=True, verbose_name="Đoạn trích ngắn")
    
    # Kế thừa ImageProcessingModel sẽ tự động xử lý ảnh này
    cover_image = models.ImageField(upload_to='blog_covers/', verbose_name="Ảnh bìa")
    
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name='posts', verbose_name="Danh mục")
    status = models.CharField(max_length=2, choices=Status.choices, default=Status.DRAFT, verbose_name="Trạng thái")
    
    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)
        
    class Meta:
        verbose_name = "Bài viết"
        verbose_name_plural = "Các bài viết"
        ordering = ['-created_at']