# -*- coding: utf-8 -*-
import datetime
from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    """
    Model to represent the blog posts.
    """
    author = models.ForeignKey(User, blank=True, null=True)
    message = models.TextField(max_length=140)
    date_posted = models.DateTimeField(default=datetime.datetime.now)

    def __unicode__(self):
        return "Post from: %s, Txt: %s" % (self.author.username, self.message,)
