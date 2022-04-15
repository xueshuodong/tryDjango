from django.urls import path
from .views import (
    product_detail_view, 
    product_create_view, 
    product_form_view, 
    render_initial_data, 
    product_delete_view,
    product_list_view,
    product_update_view,
    dynamic_lookup_view,
    )

app_name = 'products'

urlpatterns = [
    # path('product/', product_detail_view),
    # path('create/', product_create_view),
    # path('form/', product_form_view),
    # path('initial/', render_initial_data),
    path('', product_list_view, name='product-list'),
    path('create/', product_create_view, name='product-list'),
    path('<int:id>/', dynamic_lookup_view, name='product-detail'),#<int:id> / <slug:slug>
    path('<int:id>/update/', product_update_view, name='product-update'),#<int:id> / <slug:slug>
    path('<int:id>/delete/', product_delete_view, name='product-delete'),
    
]