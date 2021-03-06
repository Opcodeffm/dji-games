# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.views.generic import TemplateView

urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name='pages/home.html'), name="home"),
    url(r'^games/$', TemplateView.as_view(template_name='pages/home.html'), name="home"),
    url(r'^games/de/$', TemplateView.as_view(template_name='pages/de/home.html'), name="home-de"),
    url(r'^games/travel/$', TemplateView.as_view(template_name='pages/travel.html'), name="travel"),
    url(r'^games/travel/de/$', TemplateView.as_view(template_name='pages/de/travel.html'), name="travel-de"),
    url(r'^games/press/$', TemplateView.as_view(template_name='pages/press.html'), name="press"),
    url(r'^games/press/de/$', TemplateView.as_view(template_name='pages/de/press.html'), name="press-de"),
    url(r'^games/social/$', TemplateView.as_view(template_name='pages/social.html'), name="social"),
    url(r'^games/social/de/$', TemplateView.as_view(template_name='pages/de/social.html'), name="social-de"),

    # Django Admin
    url(r'^games/admin/', include(admin.site.urls)),

    # User management
    url(r'^games/users/', include("dji-games.users.urls", namespace="users")),
    url(r'^games/accounts/', include('allauth.urls')),

    # Your stuff: custom urls includes go here
    url(r'^games/pages/', include("nupages.urls", namespace="nupages")),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    # This allows the error pages to be debugged during development, just visit
    # these url in browser to see how these error pages look like.
    urlpatterns += [
        url(r'^400/$', 'django.views.defaults.bad_request'),
        url(r'^403/$', 'django.views.defaults.permission_denied'),
        url(r'^404/$', 'django.views.defaults.page_not_found'),
        url(r'^500/$', 'django.views.defaults.server_error'),
    ]
