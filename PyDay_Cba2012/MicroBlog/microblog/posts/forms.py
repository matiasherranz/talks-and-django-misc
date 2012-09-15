# -*- coding: utf-8 *-*
from django.forms import ModelForm

from posts.models import Post


class PostForm(ModelForm):
    class Meta:
        model = Post
        exclude = ['author', ]
