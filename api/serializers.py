#Import serializers from rest_framework package
from rest_framework import serializers
#Import all model classes from models module
from .models import Product,Order,OrderItem
#Create a Product Serializer --> Json 
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model=Product
        fields=['description','name','price','stock']
        #Define a method that is used for the validation of the price
        def valid_price(self,val):
            if val<=0:
                serializers.ValidationError("The price should not be negative or zero")
            return self.val
#Create a OrderItemSerializer class
class OrderItemSerializer(serializers.ModelSerializer):
    product_name=serializers.CharField(source='product.name',max_length=200)
    product_price=serializers.DecimalField(source='product.price',max_digits=10,decimal_places=2)
    class Meta:
        model=OrderItem
        fields=[
            'product_name',
            'product_price',
            'quantity',
            'item_subtotal'
        ]
class OrderSerializer(serializers.ModelSerializer):
    items=OrderItemSerializer(many=True,read_only=True)
    total_price=serializers.SerializerMethodField(method_name='total')
    def total(self,obj):
            order_items=obj.items.all()
            total=[item.item_subtotal for item in order_items]
            return sum(total)
    class Meta:
        model=Order
        fields=['order_id','user','created_at','status','items','total_price']

class ProductInfoSerializer(serializers.Serializer):
    products=ProductSerializer(many=True)
    count=serializers.IntegerField()
    max_price=serializers.FloatField()
    
        
        
