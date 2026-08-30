from django.urls import path
from api import views
urlpatterns=[
    path('products/',views.product_lists,name='products'),
    path('products/<int:product_id>/',views.product_detail),
]