from django.contrib import admin
from .models import Post

class PostAdmin(admin.ModelAdmin):
    model = Post
    list_display = ['title', 'auth', 'created_at', 'updated_at']

admin.site.register(Post, PostAdmin)