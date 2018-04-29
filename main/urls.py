from django.urls import path
from . import views

urlpatterns = [
    path('', views.root),
    path('<character_id>/', views.root),
]
