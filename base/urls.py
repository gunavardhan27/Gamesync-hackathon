from django.urls import path,include
from base.views import home,register
urlpatterns = [
    path('',home),
    path('register',register,name='register_form'),
]