from django.contrib import admin
from .models import Post,Tag,Category

class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_time', 'modified_time', 'category','author']
    class Media:
        js = [
            '/static/blog/js/tinymce/js/jquery.min.js',   # 必须首先加载的jquery，手动添加文件
            '/static/blog/js/tinymce/js/tinymce/tinymce.min.js',   # tinymce自带文件
            '/static/blog/js/tinymce/js/tinymce/plugins/jquery.form.js',    # 手动添加文件
            '/static/blog/js/tinymce/js/tinymce/textarea.js',   # 手动添加文件，用户初始化参数
        ]


admin.site.register(Post, PostAdmin)
admin.site.register(Category)
admin.site.register(Tag)

