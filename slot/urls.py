from django.urls import path
from . import views

urlpatterns = [
    path('', views.home,name = 'slot-home'),
    path('about/', views.about,name = 'slot-about'),
]