"""nerd_herder URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.contrib import admin
from django.urls import path
from django.conf.urls import include, url

from nerd_herder.views import index
from nerd_herder.speakers import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('talk_detail', views.talk_form, name='talk_detail'),
    path('talk_confirmation/<uuid:talk_id>/', views.talk_confirmation, name='talk_confirmation')
    #path('', index, name='index'),
    #path('new_speaker', views.talk_form, name='new_speaker'),
    #path('new_talk', views.new_talk, name='new_talk'),
    #path('success', views.success, name='success'),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls, namespace='debug_toolbar')),
    ] + urlpatterns
