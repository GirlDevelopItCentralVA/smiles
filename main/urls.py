from django.urls import path
from . import views

urlpatterns = [
    # Lesson 1 and 2
    # path('hello/', views.hello),

    # Lesson 3
    path('hello/', views.hello),

    # Let's develop it
    path('coin/', views.coin_flip),
    path('hello2/', views.hello_form),

    # Lesson 4
    path('hello_form/', views.hello_form),

    # Lesson 5
    path('hello_path/', views.hello_path),
    path('hello_path/<name>/', views.hello_path),

    ##### CHARACTER VIEWS #####
    # path('', views.character_page),
    # path('<character_id>/', views.character_page),
    ##### END CHARACTER VIEWS #####
]
