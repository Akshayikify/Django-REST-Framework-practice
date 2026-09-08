from django.urls import path
from api import views
urlpatterns=[
    path('products/',views.ProductListAPIView.as_view()),
    path('products/<int:product_id>/',views.ProductDetailAPIView.as_view()),
    path('orders/',views.OrderListAPIView.as_view()),
    path('product/info/',views.ProductInfoAPIView.as_view()),
    path('update_product/<int:pk>/',views.UpdateDeleteAPIView.as_view()),
    path('create_product/',views.CreateProductAPIView.as_view()),
    path('user/orders/',views.UserOrderListAPIView.as_view()),
]