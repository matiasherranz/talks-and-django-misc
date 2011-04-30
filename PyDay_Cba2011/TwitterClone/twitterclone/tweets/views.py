# -*- coding: utf-8 -*-
from models import Tweet
from django.shortcuts import render_to_response

def show_timeline(request):
    return render_to_response('tweets/timeline.html',
                    {'tweets': Tweet.objects.order_by('-date_posted')},
           )