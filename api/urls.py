from django.urls import path
from api import views
urlpatterns=[
    path('products/',views.product_lists),
    path('products/<int:pk>/',views.product_detial),
    path('create_product/',views.create_product),
    path('update_product/<int:pk>/',views.update_product),
]