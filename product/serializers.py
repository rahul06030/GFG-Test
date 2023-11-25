from rest_framework import serializers
from .models import Product, Order, OrderDetails

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
        
class OrderDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderDetails
        fields = '__all__'

class OrderSerializer(serializers.ModelSerializer):
    order_details = OrderDetailsSerializer(many=True, read_only=True)

    class Meta:
        model = Order
        fields = '__all__'
