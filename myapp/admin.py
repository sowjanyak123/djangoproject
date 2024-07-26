from django.contrib import admin
from .models import Blog, Event
from ckeditor.widgets import CKEditorWidget # type: ignore
from django.db import models


class BlogAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': CKEditorWidget()},
    }


admin.site.register(Blog, BlogAdmin)
admin.site.register(Event)
