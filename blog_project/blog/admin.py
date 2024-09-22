from django.contrib import admin
from .models import Post

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_at')  # Displaying in the form of list in admin pannel

admin.site.register(Post, PostAdmin)  
