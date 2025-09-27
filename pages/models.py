from django.db import models
from core.models import TimeStampedModel
# from ckeditor.fields import RichTextField

class Page(TimeStampedModel):
    """Model cho các trang tĩnh như Giới thiệu, Liên hệ..."""
    title = models.CharField(max_length=200, verbose_name="Tiêu đề trang")
    slug = models.SlugField(max_length=100, unique=True, help_text="Đường dẫn tĩnh, ví dụ: 'about-us', 'contact'")
    content = models.TextField(verbose_name="Nội dung trang")
    # content = RichTextField(verbose_name="Nội dung trang")
    is_published = models.BooleanField(default=True, verbose_name="Hiển thị trang?")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Trang tĩnh"
        verbose_name_plural = "Các trang tĩnh"