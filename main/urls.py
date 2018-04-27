from django.urls import path
from . import views

urlpatterns = [
    path('', views.root, name='root'),
    path('<character_id>/', views.root, name='character'),
    path('sayings/', views.post_saying, name='post_saying'),
]
