from rest_framework.decorators import api_view
from django.http import JsonResponse,HttpResponse
from .models import Product,Order,OrderItem
from .serializers import ProductSerializer,OrderSerializer,ProductInfoSerializer
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework import status
from django.db.models import Max
from rest_framework import generics
# Creating get and post requests
class ProductListAPIView(generics.ListAPIView):
    queryset=Product.objects.filter(stock__gte=0)
    serializer_class=ProductSerializer
        
class ProductDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset=Product.objects.all()
    serializer_class=ProductSerializer
    lookup_url_kwarg='product_id'

# class OrderListAPIView(generics.ListAPIView):
#     queryset=Order.objects.prefetch_related('items__product').all()
#     serializer_class=OrderSerializer

class UserOrderListAPIView(generics.ListAPIView):
    queryset=Order.objects.prefetch_related('items__product').all()
    serializer_class=OrderSerializer
    def get_queryset(self):
        user = self.request.user
        qs=super().get_queryset()
        return qs.filter(user=user)

# @api_view(['GET'])
# def order_list(request):
#     orders=Order.objects.prefetch_related('items__product').all()
#     serializer=OrderSerializer(orders,many=True)
#     return Response(serializer.data,status=status.HTTP_200_OK)

@api_view(['GET'])
def product_info(request):
    products=Product.objects.all()
    serializer=ProductInfoSerializer({
        'products': products,
        'count': len(products),
        'max_price': products.aggregate(max_price=Max('price'))['max_price']
    })
    return Response(serializer.data)