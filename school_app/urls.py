from django.urls import path
from . import views


urlpatterns = [
    path('', views.welcome, name='welcome'),

    path('add/', views.add, name='add'),

    path('login/', views.login, name='login'),

    path('signup/', views.signup, name='signup'),

    path('table/', views.table, name='table'),
    
]
