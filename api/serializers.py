from rest_framework import serializers
from .models import Product,Order,OrderItem
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model=Product
        fields=[
            'name',
            'price',
            'stock'
        ]
    def validate_price(self,val):
        if val<=0:
            """
            This is used to validate the price of the product
            """
            raise serializers.ValidationError("The price should be greater than 0")
        return val
    
class OrderItemSerializer(serializers.ModelSerializer):
    product_name=serializers.CharField(max_length=200,source='product.name')
    product_price=serializers.DecimalField(max_digits=10,decimal_places=2,source='product.price')
    class Meta:
        model=OrderItem
        fields=[
            'product_name',
            'product_price',
            'quantity'
        ]
class OrderSerializer(serializers.ModelSerializer):
    items=OrderItemSerializer(many=True,read_only=True)
    total_price=serializers.SerializerMethodField()
    def get_total_price(self,obj):
        price=[item.item_subtotal for item in obj.items.all()]
        return sum(price)
    class Meta:
        model=Order
        fields=[
            'order_id',
            'user',
            'created_at',
            'status',
            'items',
            'total_price'
        ]
class ProductInfoSerializer(serializers.Serializer):
    products=ProductSerializer(many=True)
    count=serializers.IntegerField()
    max_price=serializers.FloatField()