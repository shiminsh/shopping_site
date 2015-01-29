from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.conf import settings

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'app.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', 'global.views.home'),
    url(r'^item/$', 'global.views.item'),
    url(r'^feedback/$', 'global.views.feedback'),
    url(r'^main/', include('global.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/', include('allauth.urls')),				
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
