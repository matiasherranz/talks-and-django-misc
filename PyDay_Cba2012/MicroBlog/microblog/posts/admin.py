# -*- coding: utf-8 *-*
from django.contrib import admin
from posts.models import Post


class PostAdmin(admin.ModelAdmin):
    list_display = ('author', 'message', 'date_posted',)
    search_fields = ('author__username', 'message', 'date_posted',)

admin.site.register(Post, PostAdmin)
