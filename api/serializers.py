from rest_framework import serializers
from .models import Product,Order,OrderItem

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model=Product
        fields=[
            'id',
            'name',
            # 'description',
            'price',
            'stock'
        ]
    def validate_price(self,value):
        """
            The price should be greater than 1 and should not be less than 0
        """
        if value<=0:
            raise serializers.ValidationError("The price should be greater than 0")
        return value
class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model=Order
        fields=[
            'order_id',
            'user',
            'created_at',
            'status'
        ]

class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model=OrderItem
        fields=[
            'order',
            'product',
            'quantity'
        ]