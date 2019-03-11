from django.contrib import admin

from .models import BlogUser,Blog
# Register your models here.

admin.site.register(BlogUser)
admin.site.register(Blog)