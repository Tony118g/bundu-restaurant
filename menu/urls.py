from . import views
from django.urls import path

urlpatterns = [
    path('menu/', views.menu_page, name='menu_page'),
    path('menu/drafts/', views.menu_drafts, name='menu_drafts'),
    path('menu/add_menu_item/', views.add_menu_item, name='add_menu_item'),
    path(
        'menu/edit_menu_item/<str:pk>',
        views.edit_menu_item,
        name='edit_menu_item'
        ),
    path(
        'menu/delete_item/<str:pk>/',
        views.delete_menu_item,
        name='delete_item'
        )
]
