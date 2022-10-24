from django.urls import path, include
from authentication import views

urlpatterns = [
    path('register/',views.RegisterView.as_view(), name='register'),
]
