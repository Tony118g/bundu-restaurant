from . import views
from .forms import SignUpForm
from django.urls import path
from allauth.account import views as auth_views

urlpatterns = [
    path('', views.home_page, name='home'),
    path('accounts/signup/', auth_views.SignupView.as_view(form_class=SignUpForm)),
]