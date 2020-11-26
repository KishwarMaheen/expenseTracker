from django.urls import path
from . import views


# app urls
urlpatterns = [
    path('', views.index, name='index'),
    path('add_category', views.add_category, name='add_category'),
    path('<category_id>', views.category_detail, name='category_detail'),
    path('<category_id>/add_item', views.add_item, name='add_item'),
    path('<category_id>/<item_id>', views.item_detail, name='item_detail'),
    path('<category_id>/<item_id>/edit_item', views.edit_item, name='edit_item'),
]
