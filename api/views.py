from rest_framework.decorators import api_view
from django.http import JsonResponse,HttpResponse
from .models import Product,Order,OrderItem
from .serializers import ProductSerializer
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework import status

# Creating get and post requests
@api_view(['GET','PUT','DELETE'])
def get_or_update_delete(request,pk):
    
    if request.method=='PUT':
        serializer=ProductSerializer(Product,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    elif request.method=='GET':
        product=get_object_or_404(Product,pk=pk)
        serializer=ProductSerializer(product)
        return Response(serializer.data,status=status.HTTP_200_OK)
    else:
        product=get_object_or_404(Product,pk=pk)
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

        

        
        
@api_view(['GET','POST'])
def product_lists(request):
    if request.method=='POST':
        serializer=ProductSerializer(Product,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    else:
        products=Product.objects.all()
        serializer=ProductSerializer(products,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)


