from . import views
from django.urls import path

urlpatterns = [
    path('menu/', views.menu_page, name='menu_page'),
    path('menu/add_menu_item/', views.add_menu_item, name='add_menu_item'),
]
