from django.urls import path
from . import views

urlpatterns = [
    # Lesson 1
    # path('hello/', views.hello),

    # Lesson 2
    # path('hello/', views.hello_with_query_param),

    # Lesson 3
    # path('hello/', views.hello_with_template),

    # Lesson 4
    # path('hello/', views.hello_with_param),
    # path('hello/<name>/', views.hello_with_param),

    # Lesson 5
    path('hello/', views.hello_with_post),

    # Lesson 6
    path('', views.character_page),
    path('<character_id>/', views.character_page),
]
