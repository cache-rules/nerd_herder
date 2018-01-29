from django.shortcuts import render, redirect
from django.urls import reverse


def index(request):
    if request.user.is_authenticated:
        return redirect(reverse('dashboard'), permanent=False)

    return render(request, 'index.html')
