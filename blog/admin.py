from django.contrib import admin

# Register your models here.
from .models import Post

class PostAdmin(admin.ModelAdmin):
	list_display = ("title", "slug", "status", "created_on")
	list_filter = ("status", "author")
	search_fileds = ["title", "content"]
	prepopulated_fields = {"slug": ("title",)} 

admin.site.register(Post, PostAdmin)