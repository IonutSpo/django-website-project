from django.urls import path
from . import views



urlpatterns = [
    path('signup/', views.signup_request, name='signup'),
    path('login/', views.login_request, name='login'),
    path('logout/', views.logout_request, name='logout'),
    path('profile/', views.profile_details, name='profile'),
    path('update/profile', views.update_profile, name='update_profile'),
    path('delete/profile', views.delete_user, name='delete_user')
]
