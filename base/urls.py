from django.urls import path
from . import views

urlpatterns = [
    path('products/get/<int:user_id>', views.get_products, name= 'get_products'),
    path('product/get/<int:pk>', views.get_product, name= 'product'),
    path('products/add/<int:user_id>', views.add_products, name= 'add_products'),
    path('product/update/<int:pk>', views.update_product, name= 'update_product'),
    path('product/delete/<int:pk>', views.delete_product, name= 'delete_product')
]