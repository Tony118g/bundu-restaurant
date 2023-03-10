from . import views
from .forms import SignUpForm
from django.urls import path
from allauth.account import views as auth_views

urlpatterns = [
    path('', views.home_page, name='home'),
    path('accounts/profile/', views.profile_page, name='profile_page'),
    path('accounts/edit_account/<str:pk>/', views.edit_account, name='edit_account'),
    path('accounts/signup/', auth_views.SignupView.as_view(form_class=SignUpForm)),
]
