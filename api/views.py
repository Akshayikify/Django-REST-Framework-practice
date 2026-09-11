from rest_framework.decorators import api_view
from django.http import JsonResponse,HttpResponse
from .models import Product,Order,OrderItem
from .serializers import ProductSerializer
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework import status

@api_view(['GET'])
def product_lists(request):
    products=Product.objects.all()
    serializer=ProductSerializer(products,many=True)
    return Response(serializer.data) 
@api_view(['GET'])
def product_detial(request,pk):
    product=get_object_or_404(Product,pk=pk)
    serializer=ProductSerializer(product,many=False)
    return Response(serializer.data)
@api_view(['POST'])
def create_product(request):
    serializer=ProductSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data,status=status.HTTP_201_CREATED)
    return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def update_product(request,pk):
    product=get_object_or_404(Product,pk=pk)
    serializer=ProductSerializer(product,data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data,status=status.HTTP_201_CREATED)
        
    return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    


