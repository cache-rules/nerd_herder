from django.shortcuts import render

from nerd_herder.utils import get_asset_urls


def app(request, **_):
    js_url, css_url = get_asset_urls(request)
    context = {'js_url': js_url, 'css_url': css_url}
    return render(request, 'app.html', context)
