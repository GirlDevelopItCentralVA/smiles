from django.urls import path
from . import views

urlpatterns = [
    path('', views.root, name='root'),
    path('sayings/', views.post_saying, name='post_saying'),
    path('<character_id>/', views.root, name='character'),
]
