from django.urls import path
from api import views
urlpatterns=[
    path('products/',views.ProductList.as_view()),
    path('products/info/',views.product_info),
    path('orders/',views.order_list),
]