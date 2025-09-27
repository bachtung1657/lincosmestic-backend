import sys
from io import BytesIO
from PIL import Image
from django.db import models
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.utils.text import slugify

class TimeStampedModel(models.Model):
    """Một model trừu tượng cung cấp 2 trường created_at và updated_at."""
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class ImageProcessingModel(models.Model):
    """
    Model trừu tượng để xử lý ảnh:
    1. Nén ảnh để giảm dung lượng.
    2. Chuyển đổi sang định dạng WebP để tối ưu cho web.
    """
    def save(self, *args, **kwargs):
        # Duyệt qua tất cả các trường của model
        for field_name in self._meta.get_fields():
            # Chỉ xử lý các trường ImageField
            if isinstance(field_name, models.ImageField):
                img_field = getattr(self, field_name.name)
                if not img_field:
                    continue

                # Mở ảnh từ bộ nhớ
                img = Image.open(img_field)
                
                # Loại bỏ metadata không cần thiết (EXIF) để giảm dung lượng
                img_data = list(img.getdata())
                img_without_exif = Image.new(img.mode, img.size)
                img_without_exif.putdata(img_data)

                # Nén và chuyển đổi sang WebP
                output = BytesIO()
                # Chất lượng 85 là một sự cân bằng tốt giữa chất lượng và dung lượng
                img_without_exif.save(output, format='WEBP', quality=85)
                output.seek(0)
                
                # Tạo một file mới trong bộ nhớ để lưu lại
                file_name = f"{slugify(img_field.name.split('.')[0])}.webp"
                setattr(self, field_name.name, InMemoryUploadedFile(
                    output,
                    'ImageField',
                    file_name,
                    'image/webp',
                    sys.getsizeof(output),
                    None
                ))
        
        super().save(*args, **kwargs)

    class Meta:
        abstract = True