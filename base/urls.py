from django.urls import path,include
from base.views import home,register,gaming_profile
urlpatterns = [
    path('',home),
    path('register',register,name='register_form'),
    path('profiles/<str:pk>/',gaming_profile,name="profiles"),
]

