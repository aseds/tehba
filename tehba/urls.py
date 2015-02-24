from django.conf.urls import patterns, include, url
from django.contrib import admin
import views 

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'tehraner.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', views.home, name='home'),

    url(r'^events/', include('events.urls', namespace="events")),

    url(r'^admin/', include(admin.site.urls)),
)
