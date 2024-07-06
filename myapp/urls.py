from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index, name='index'),
    path('', views.home, name='home'),
    path('create/', views.create, name='create'),
    path('view/', views.view, name='view'),
    path('<int:id>', views.list, name='list'),
    path('logout/', views.logout_user, name='logout'),
]