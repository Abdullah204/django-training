from django.urls import path
from django.contrib.auth.decorators import login_required

from artists.views import CreateView , ListView
urlpatterns = [
    path('' , ListView.as_view(),name = 'list'),
    path('create', login_required(CreateView.as_view()), name='create'),
]