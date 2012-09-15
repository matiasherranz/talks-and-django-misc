from django.conf.urls import patterns, include, url
from django.views.generic.simple import direct_to_template

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',

    url(r'^accounts/login/$', 'django.contrib.auth.views.login'),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    # My urls:
    url(r'^$', direct_to_template,
                   {'template': 'posts/index.html'}, "home"),
    url(r'^home$', direct_to_template,
                   {'template': 'posts/index.html'}, "home"),
    url(r'^write_post/$', 'posts.views.write_post', name='write_new_post'),
    url(r'^read_posts/$', 'posts.views.show_timeline', name="read_posts"),
)
