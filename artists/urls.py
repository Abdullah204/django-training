from django.urls import path
from django.contrib.auth.decorators import login_required
from artists.views import ArtistList, CreateView , ListView
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('', ArtistList.as_view()),
    # path('' , ListView.as_view(),name = 'list'),
    path('create', login_required(CreateView.as_view()), name='create'),
    

]
urlpatterns = format_suffix_patterns(urlpatterns)
