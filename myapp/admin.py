from django.contrib import admin
from .models import Post
from .models import Media

# Register your models here.
admin.site.register(Post)
admin.site.register(Media)

