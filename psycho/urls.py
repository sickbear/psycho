from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from blog_app.views import post_list, post_single
from main_app.views import (main, services, reviews, contacts)

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^$', main, name='main'),
    url(r'^services/$', services, name='services'),
    url(r'^blog/$', post_list, name='post_list'),
    url(r'^reviews/$', reviews, name='reviews'),
    url(r'^contacts/$', contacts, name='contacts'),
    url(r'^post/(?P<pk>\w+)/$', post_single, name='post_single')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)