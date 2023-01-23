from django.contrib import admin
from .models import Post, Perfil

class PostAdmin(admin.ModelAdmin):
    model = Post
    list_display = ['title', 'auth', 'created_at', 'updated_at']

class PerfilAdmin(admin.ModelAdmin):
    model = Perfil
    list_display = ['user', 'updated_at']

admin.site.register(Post, PostAdmin)
admin.site.register(Perfil, PerfilAdmin)