from django.urls import path
from . import views

urlpatterns = [
    path('', views.loginaccount, name="login"),
    path('signup/', views.signupaccount, name="signup"),
    path('logout/', views.logoutaccount, name="logout"),
]