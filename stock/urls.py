from django.urls import path
from stock import views

urlpatterns = [
    path('products/', views.product_list_create, name="product-list-create"),
    path('products/<int:pk>/', views.product_detail, name="product-detail"),
]
