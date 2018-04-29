from django.urls import path
from . import views

urlpatterns = [
    path('hello/', views.hello),
    path('coin/', views.coin_flip),
    path('hello2/', views.hello_form),


    ##### CHARACTER VIEWS #####
    # path('', views.character_page),
    # path('<character_id>/', views.character_page),
    ##### END CHARACTER VIEWS #####
]
