from django.contrib import admin

# Register your models here.

from django.contrib import admin
from .models import Blog , Comment


# class CommentInline(admin.TabularInline): 
#     model = Comment
    

# class BlogAdmin(admin.ModelAdmin): 
#     inlines = [
#         CommentInline,
#     ]



admin.site.register(Blog)
admin.site.register(Comment)