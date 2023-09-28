from django.contrib import admin
from .models import Post, Comment, Reply
# Register your models here.

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display=['hashtag', 'description']
    list_filter=['CreatedAt']

@admin.register(Comment)
class CommetnAdmin(admin.ModelAdmin):
    list_display=['related_user', 'content']

@admin.register(Reply)
class ReplyAdmin(admin.ModelAdmin):
    list_display = ['related_comment', 'content']