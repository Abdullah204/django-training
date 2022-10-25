from django.urls import include, path
from users import views
urlpatterns = [
    path('<int:pk>/', views.UserDetailView.as_view(), name='user_detail'),
]