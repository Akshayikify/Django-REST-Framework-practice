from django.urls import path
from api import views
urlpatterns=[
    path('products/<int:pk>/',views.get_or_update_delete),
    path('products/',views.product_lists),
    path('products/info/',views.product_info),
    path('orders/',views.order_list),
]