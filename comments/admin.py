from django.contrib import admin
from .models import Comment


class CommentAdmin(admin.ModelAdmin):
    list_display=['post','name','text','created_time',]

admin.site.register(Comment, CommentAdmin)