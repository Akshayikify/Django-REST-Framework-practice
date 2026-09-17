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
class ProductList(generics.ListAPIView):
    queryset=Product.objects.all()
    serializer_class=ProductSerializer
        

@api_view(['GET','POST'])
def product_lists(request):
    if request.method=='POST':
        serializer=ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    else:
        products=Product.objects.all()
        serializer=ProductSerializer(products,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)

@api_view(['GET'])
def order_list(request):
    orders=Order.objects.prefetch_related('items__product').all()
    serializer=OrderSerializer(orders,many=True)
    return Response(serializer.data,status=status.HTTP_200_OK)

@api_view(['GET'])
def product_info(request):
    products=Product.objects.all()
    serializer=ProductInfoSerializer({
        'products': products,
        'count': len(products),
        'max_price': products.aggregate(max_price=Max('price'))['max_price']
    })
    return Response(serializer.data)