from django.contrib import admin
from .models import Page
from django_summernote.admin import SummernoteModelAdmin

@admin.register(Page)
class PageAdmin(SummernoteModelAdmin):
    summernote_fields = ('content',)
    list_display = ('title', 'slug', 'is_published')
    list_filter = ('is_published',)
    search_fields = ('title', 'content')