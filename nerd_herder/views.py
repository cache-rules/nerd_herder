from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.urls import reverse


def home(request):
    if request.user.is_authenticated:
        return redirect(reverse('dashboard'), permanent=False)

    return render(request, 'home.html')

# def signup(request):
#     if request.method == 'POST':
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             username = form.cleaned_data.get('username')
#             raw_password = form.cleaned_data.get('password1')
#             user = authenticate(username=username, password=raw_password)
#             login(request, user)
#             return redirect('home')
#         else:
#             form = UserCreationForm()
#         return render(request, 'signup.html', {'form', form})
