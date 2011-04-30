from django.contrib import admin
from models import Tweet

class TweetAdmin(admin.ModelAdmin):
    list_display = ('user', 'message', 'date_posted',)
    search_fields = ('user__username', 'message', 'date_posted',) 
    
admin.site.register(Tweet, TweetAdmin)