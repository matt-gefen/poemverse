from django.urls import path
from . import views

urlpatterns = [
  path('', views.Home.as_view(), name='home'),
  path('poems/', views.poems_index, name='poems_index'),
  path('poems/myverse', views.user_index, name='user_index'),
  path('accounts/signup/', views.signup, name='signup'),
  path('poems/create/', views.PoemCreate.as_view(), name='poems_create'),
  path('poems/add', views.poems_add, name='poems_add'),
]