# -*- coding: utf-8 -*-
import datetime
from django.db import models
from django.contrib.auth.models import User

class Tweet(models.Model):
    """
    Model que representa los tweets.
    """
    user = models.ForeignKey(User)
    message = models.CharField(max_length=140)
    date_posted = models.DateTimeField(default=datetime.datetime.now)
    
    def __unicode__(self):
        return "Tweet from: %s, Txt: %s" % (self.user.username, self.message,)
