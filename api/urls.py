from django.urls import path
from api import views
urlpatterns=[
    path('products/',views.ProductListCreateAPIView.as_view()),
    path('products/<int:pk>/',views.ProductUpdateAPIView.as_view()),
    # path('products/info/',views.ProductInfo.as_view()),
    # path('products/<int:product_id>/',views.ProductDetailAPIView.as_view()),
    # path('orders/',views.OrderListAPIView.as_view()),
    # path('user-orders/',views.UserOrderListAPIView.as_view(),name='user-orders'),
]