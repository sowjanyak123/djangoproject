from django.contrib import admin
from .models import Blog
from ckeditor.widgets import CKEditorWidget
from django.db import models


class BlogAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': CKEditorWidget()},
    }

admin.site.register(Blog, BlogAdmin)
