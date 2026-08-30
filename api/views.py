from django.http import JsonResponse
from .serializers import ProductSerializer
from django.shortcuts import get_object_or_404
from .models import Product
from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['GET'])
def product_lists(request):
    products=Product.objects.all()
    serializer=ProductSerializer(products,many=True)
    return Response(serializer.data)
    
@api_view(['GET'])
def product_detail(request,product_id):
    product=get_object_or_404(Product,id=product_id)
    serializer=ProductSerializer(product,many=False)
    return Response(serializer.data)
    