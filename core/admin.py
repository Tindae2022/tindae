from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin

from .models import Category, Comment, Tag, Post, Message

from .models import Category, Comment, Tag, Post




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



@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email')


@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    summernote_fields = ('body',)
    list_display = ('title', 'category', 'status')

    class Meta:
        model = Post
        fields = '__all__'