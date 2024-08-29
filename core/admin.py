from django.contrib import admin
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


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    pass
