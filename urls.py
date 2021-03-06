from django.conf.urls.defaults import *
from django.conf import settings

urlpatterns = patterns('',
    (r'^r/', include('django.conf.urls.shortcut')),
    (r'^admin/filebrowser/filebrowser/', include('filebrowser.urls')),
    #
    (r'^admin/', include('django.contrib.admin.urls')),
    (r'^events/', include('events.urls')),
    (r'^links/', include('links.urls')),
    (r'^planetauec/', include('feedme.urls')),
    (r'^txts/preview/$', 'txts.views.preview',),
    (r'^nova/', include('txts.urls')),
)


if settings.LOCAL_DEV:
    urlpatterns = patterns('',
    (r'^media/(?P<path>.*)$', 'django.views.static.serve',
      {'document_root': settings.MEDIA_ROOT,
       'show_indexes': True, }),
) + urlpatterns


