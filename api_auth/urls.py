from . import views
from django.urls import path

urlpatterns  = [
    path('', views.SignUp.as_view()),
]