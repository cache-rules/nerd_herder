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

urlpatterns = [
    path("admin/", admin.site.urls),
    path(
        "pages/code-of-conduct/",
        include("nerd_herder.code_of_conduct.urls", namespace="code_of_conduct"),
    ),
    path("api/v1/talks/", include("nerd_herder.talks.urls", namespace="talks")),
    path(
        "api/v1/talk-proposals/",
        include("nerd_herder.talk_proposals.urls", namespace="talk_proposals"),
    ),
    path("api/v1/slack/", include("nerd_herder.slack.urls", namespace="slack")),
]
