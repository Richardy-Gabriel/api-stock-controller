from django.urls import path
from stock import views

urlpatterns = [
    path('products/', views.product_list_create, name="product-list-create"),
]
