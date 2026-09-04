from django.urls import path
from api import views
urlpatterns=[
    path('products/',views.ProductListAPIView.as_view()),
    path('products/<int:product_id>/',views.ProductDetailAPIView.as_view()),
    path('orders/',views.OrderListAPIView.as_view()),
    path('product/info/',views.product_info),
    path('update_product/<int:pk>/',views.update_product)
]