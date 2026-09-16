from rest_framework.decorators import api_view
from django.http import JsonResponse,HttpResponse
from .models import Product,Order,OrderItem
from .serializers import ProductSerializer,OrderSerializer,ProductInfoSerializer
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework import status
from django.db.models import Max
# Creating get and post requests
@api_view(['GET','PUT','DELETE','PATCH'])
def get_or_update_delete(request,pk):
    
    if request.method=='PUT':
        product=get_object_or_404(Product,pk=pk)
        serializer=ProductSerializer(product,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    elif request.method=='GET':
        product=get_object_or_404(Product,pk=pk)
        serializer=ProductSerializer(product)
        return Response(serializer.data,status=status.HTTP_200_OK)
    elif request.method=='GET':
        product=get_object_or_404(Product,pk=pk)
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    elif request.method=='PATCH':
        product=get_object_or_404(Product,pk=pk)
        serializer=ProductSerializer(product,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status.HTTP_404_NOT_FOUND)
        

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
    orders=Order.objects.prefetch_related('items')
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