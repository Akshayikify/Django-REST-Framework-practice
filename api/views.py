from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from .models import Product,Order,OrderItem
from .serializers import ProductSerializer,OrderSerializer,ProductInfoSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.db.models import Max
@api_view(['GET'])
def product_lists(request):
    products=Product.objects.all()
    serializer=ProductSerializer(products,many=True)
    return Response(serializer.data)

@api_view(['GET'])
def product_detail(reqeust,product_id):
    product=get_object_or_404(Product,id=product_id)
    serializer=ProductSerializer(product,many=False)
    return Response(serializer.data)

@api_view(['GET'])
def order_lists(request):
    orders=Order.objects.prefetch_related('items__product')
    serializer=OrderSerializer(orders,many=True)
    return Response(serializer.data)
@api_view(['GET'])
def product_info(request):
    products=Product.objects.all()
    serializer=ProductInfoSerializer({
        'products': products,
        'count': len(products),
        'max_price': products.aggregate(max_price=Max('price'))['max_price']
    })
    return Response(serializer.data)
