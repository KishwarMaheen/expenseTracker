from django.urls import path
from . import views


# app urls
urlpatterns = [
    path('', views.index, name='index'),
    path('add_category/', views.add_category, name='add_category'),
    path('add_category/add_category_process/', views.add_category_process, name='add_category_process'),
    path('category_detail/<category_id>', views.category_detail, name='category_detail'),
    path('category_detail/<category_id>/add_item/', views.add_item, name='add_item'),
    path('category_detail/<category_id>/add_item/add_item_process', views.add_item_process, name='add_item_process'),
    path('category_detail/<category_id>/item_detail/<item_id>', views.item_detail, name='item_detail'),
    path('category_detail/<category_id>/item_detail/<item_id>/edit_item/', views.edit_item, name='edit_item'),
    path('category_detail/<category_id>/item_detail/<item_id>/edit_item/edit_item_process',
         views.edit_item_process, name='edit_item_process'),
]
