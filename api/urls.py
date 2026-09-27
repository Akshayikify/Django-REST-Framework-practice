from django.urls import path
from api import views
from rest_framework.routers import DefaultRouter
urlpatterns=[
    path('products/',views.ProductListCreateAPIView.as_view()),
    path('products/<int:product_id>/',views.ProductDetailAPIView.as_view()),
    path('products/info/',views.ProductInfo.as_view()),
    path('products/<int:product_id>/',views.ProductDetailAPIView.as_view()),
]

router = DefaultRouter()
router.register('oreders',views.OrderViewSet)
urlpatterns += router.urls