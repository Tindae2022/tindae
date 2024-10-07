from django.contrib import admin

from .models import Category, Comment, Tag, Post, Message
from tinymce.widgets import TinyMCE
from tinymce import models as tinymce_models

from .models import Category, Comment, Tag, Post
from django_summernote.admin import SummernoteModelAdmin

# Apply summernote to all TextField in model.
from django_summernote.admin import SummernoteModelAdmin
from .models import Post


# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    pass


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass


class PostAdmin(admin.ModelAdmin):
    formfield_overrides = {
        tinymce_models.HTMLField: {'widget': TinyMCE(attrs={'width': '100%', 'height': 400})},
    }


admin.site.register(Post, PostAdmin)


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email')


