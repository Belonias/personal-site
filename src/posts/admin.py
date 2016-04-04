from django.contrib import admin

# Register your models here.

from .models import Post
from .forms import PostModelForm

class PostAdmin(admin.ModelAdmin):
    form = PostModelForm

    list_display = ["title", "updated", "timestamp"]
    list_display_links = ["updated", "timestamp"]
    list_filter = ["updated", "timestamp"]
    search_fields = ["title", "content"]
    list_editable = ["title"]
    class Meta:
        model = Post

admin.site.register(Post, PostAdmin)
