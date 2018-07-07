from django.urls import path

from .views import EntriesList, EntryDetail

app_name = 'faq'

urlpatterns = [
    path('', EntriesList.as_view()),
    path('<int:pk>', EntryDetail.as_view()),
]
