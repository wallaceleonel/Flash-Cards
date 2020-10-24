from django.contrib import admin
from .models import Post
# Register your models here.

@admin.register(Post)
class PostAdemin(admin.ModelAdmin):
    list_display =("title","slug","author","created","updated")
    prepopulated_fields = {"slug":("title",)}