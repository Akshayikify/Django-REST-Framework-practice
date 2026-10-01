from rest_framework.decorators import api_view
from django.http import JsonResponse,HttpResponse
from .models import Product,Order,OrderItem
from .serializers import ProductSerializer,OrderSerializer,ProductInfoSerializer
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework import status
from django.db.models import Max
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated,IsAdminUser,AllowAny
from rest_framework.views import APIView
from api.filters import ProductFilter,InStockFilterBackend,OrderFilter
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import mixins
from rest_framework.pagination import PageNumberPagination,LimitOffsetPagination
from rest_framework import viewsets
from api.pagination import CustomProductPagination,OrderPagination
from rest_framework.decorators import action
# Creating get and post requests
class ProductListCreateAPIView(generics.ListCreateAPIView):
    queryset=Product.objects.order_by('pk')
    serializer_class=ProductSerializer
    filterset_class=(ProductFilter)
    filter_backends = [DjangoFilterBackend,filters.SearchFilter,filters.OrderingFilter,InStockFilterBackend]
    search_fields=['name','description']
    ordering_fields=['name','price']
    pagination_class = CustomProductPagination
    def get_permissions(self):
        self.permission_classes=[AllowAny]
        if self.request.method=='POST':
            self.permission_classes=[IsAdminUser]
        return super().get_permissions()
 
class ProductDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset=Product.objects.all()
    serializer_class=ProductSerializer
    lookup_url_kwarg='product_id'
    def get_permissions(self):
        self.permission_classes=[AllowAny]
        if self.request.method in ['PUT','DELETE','PATCH']:
            self.permission_classes=[IsAdminUser]
        return super().get_permissions()
class OrderViewSet(viewsets.ModelViewSet):
    queryset=Order.objects.prefetch_related('items__product')
    serializer_class=OrderSerializer
    permission_classes=[AllowAny]
    pagination_class = OrderPagination
    filterset_class=(OrderFilter)
    
    @action(detail = False,methods = ['get'],permission_classes=[IsAuthenticated])
    def user_orders(self,request):
        orders = self.get_queryset().filter(user=request.user)
        serializer = self.get_serializer(orders,many = True)
        return Response(serializer.data)
        
        
    

# class OrderListAPIView(generics.ListAPIView):
#     queryset=Order.objects.prefetch_related('items__product').all()
#     serializer_class=OrderSerializer

# class UserOrderListAPIView(generics.ListAPIView):
#     queryset=Order.objects.prefetch_related('items__product').all()
#     serializer_class=OrderSerializer
#     permission_classes=[IsAuthenticated]
#     def get_queryset(self):
#         user = self.request.user
#         qs=super().get_queryset()
#         return qs.filter(user=user)
class ProductInfo(APIView):
    permission_classes=[IsAuthenticated]
    def get(self,request):
        products=Product.objects.all()
        serializer=ProductInfoSerializer({
            'products': products,
            'count': len(products),
            'max_price': products.aggregate(max_price=Max('price'))['max_price']
        })
        return Response(serializer.data)


