from django.contrib import admin
from .models import Post, ImagePost

# Register your models here.
#admin.site.register(Post)
#admin.site.register(ImagePost)

class PostImageAdmin(admin.StackedInline):
    model = ImagePost

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    inlines = [PostImageAdmin]

    class Meta:
        model = Post

@admin.register(ImagePost)
class PostImageAdmin(admin.ModelAdmin):
    pass