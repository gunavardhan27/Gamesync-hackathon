from django.urls import path,include
from base.views import home,register,gaming_profile,Login,game
urlpatterns = [
    path('',home),
    path('register',register,name='register_form'),
    path('profiles/<str:pk>/',gaming_profile,name="profiles"),
    path('login/',Login,name='loginpage'),
    path('games/',game,name='games'),
]

