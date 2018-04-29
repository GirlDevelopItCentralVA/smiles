from django.urls import path
from . import views

urlpatterns = [
    # Lessons 1-3
    path('hello/', views.hello),

    # Let's develop it
    path('coin/', views.coin_flip),

    # Lesson 4
    path('hello2/', views.hello_form),

    # Lesson 5
    path('hello_path/', views.hello_path),
    path('hello_path/<name>/', views.hello_path),

    # Lesson 6
    path('', views.character_page),
    path('<character_id>/', views.character_page),
]
