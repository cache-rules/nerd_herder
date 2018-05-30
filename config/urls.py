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
from django.contrib import admin
from django.urls import path, include

from nerd_herder.talks import urls as talks_urls
from nerd_herder.views import index, code_of_conduct, code_of_conduct_reporting_guide,\
    code_of_conduct_response_playbook

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('code-of-conduct', code_of_conduct),
    path('code-of-conduct/reporting-guide', code_of_conduct_reporting_guide),
    path('code-of-conduct/response-playbook', code_of_conduct_response_playbook),
    path('api/talks', include(talks_urls, namespace='talks')),
]
