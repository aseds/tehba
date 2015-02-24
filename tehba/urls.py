from django.conf.urls import patterns, include, url
from django.conf import settings 
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
import views 

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'tehraner.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', views.home, name='home'),

    url(r'^events/', include('events.urls', namespace="events")),

    url(r'^admin/', include(admin.site.urls)),
)

if settings.DEBUG:
	# static files (images, css, javascript, etc.)
	# this is used when we are on local computer. 
	# when we go to production, the web server configuration would
	# serve static media (DEBUG = False)

	urlpatterns += patterns('',
		(r'^media/(?P<path>.*)$', 'django.views.static.serve', 
			{
				'document_root': settings.MEDIA_ROOT
			})
	)

	urlpatterns += staticfiles_urlpatterns()