#Import serializers from rest_framework package
from rest_framework import serializers
#Import all model classes from models module
from .models import Product,Order,OrderItem
#Create a Product Serializer --> Json 
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model=Product
        fields=['id','name','price','stock']
        #Define a method that is used for the validation of the price
        def valid_price(self,val):
            if val<=0:
                serializers.ValidationError("The price should not be negative or zero")
            return self.val
#Create a OrderItemSerializer class
class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model=OrderItem
        fields=[
           'product','order','quantity'
        ]
class OrderSerializer(serializers.ModelSerializer):
    items=OrderItemSerializer(many=True,read_only=True)
    class Meta:
        model=Order
        fields=['order_id','user','created_at']
        
        
