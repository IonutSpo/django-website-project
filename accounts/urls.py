from django.urls import path
from . import views


urlpatterns = [
    path('signup/', views.signup_request, name='signup'),
    path('login', views.login_request, name='login'),
    path('logout', views.logout_request, name='logout')
]
