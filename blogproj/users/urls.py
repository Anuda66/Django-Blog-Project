from django.urls import path
from .import views
from django.contrib.auth import views as auth_viwe
from django.contrib.auth.views import LogoutView

class CustomLogoutView(LogoutView):
    # Override the http_method_names attribute to allow GET requests
    http_method_names = ['get', 'post']


urlpatterns = [
    path('sign_up/', views.sign_up, name='users-sign-up'),
    path('profile/', views.profile, name='users-profile'),
    path('', auth_viwe.LoginView.as_view(template_name='users/login.html'), name='users-login'),
    path('logout/', CustomLogoutView.as_view(template_name='users/logout.html'), name='users-logout'),

]


