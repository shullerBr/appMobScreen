from django.urls import path
from django.conf.urls import url
from . import views

app_name = 'challenge'

urlpatterns = [
    path('', views.challenge_list, name='challenge_list'),
    path('create/', views.challenge_create, name='challenge_create'),
    #path('challenge/<int:pk>/', views.challenge_detail, name='challenge_detail'),
    path('challenge/<int:pk>/edit/', views.challenge_edit, name='challenge_edit'),
]


