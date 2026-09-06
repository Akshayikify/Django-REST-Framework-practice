from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from .models import Product,Order,OrderItem
from .serializers import ProductSerializer,OrderSerializer,ProductInfoSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.db.models import Max
from rest_framework import status
from rest_framework import generics
from rest_framework.views import APIView

class ProductListAPIView(generics.ListAPIView):
    queryset=Product.objects.exclude(price__gt=67)
    serializer_class=ProductSerializer

class ProductDetailAPIView(generics.RetrieveAPIView):
    queryset=Product.objects.all()
    serializer_class=ProductSerializer
    lookup_url_kwarg='product_id'

class OrderListAPIView(generics.ListAPIView):
    queryset=Order.objects.prefetch_related('items__product')
    serializer_class=OrderSerializer
class UserOrderListAPIView(generics.ListAPIView):
    queryset=Order.objects.prefetch_related('items__product')
    serializer_class=OrderSerializer
    def get_queryset(self):
        user = self.request.user
        query=super().get_queryset()
        return query.filter(user=user)

class ProductInfoAPIView(APIView):
    def get(self,request):
        products=Product.objects.all()
        serializer=ProductInfoSerializer({
            'products': products,
            'count': len(products),
            'max_price': products.aggregate(max_price=Max('price'))['max_price']
        })
        return Response(serializer.data)
    

@api_view(['PUT', 'DELETE'])
def update_product(request, pk):

    product = get_object_or_404(Product, pk=pk)

    if request.method == 'PUT':

        serializer = ProductSerializer(
            product,
            data=request.data
        )

        if serializer.is_valid():
            serializer.save()

            return Response(
                serializer.data,
                status=status.HTTP_200_OK
            )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

    elif request.method == 'DELETE':

        product.delete()

        return Response(
            {"message": "Product deleted successfully"},
            status=status.HTTP_204_NO_CONTENT
        )
        