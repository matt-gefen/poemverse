from django.urls import path
from . import views

urlpatterns = [
  path('', views.Home.as_view(), name='home'),
  path('poems/', views.poems_index, name='poems_index'),
  path('accounts/signup/', views.signup, name='signup'),
]