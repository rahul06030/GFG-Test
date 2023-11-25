from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .models import Product, Order, OrderDetails
from .serializers import ProductSerializer, OrderSerializer, OrderDetailsSerializer
from rest_framework.response import Response

class ProductListCreateView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    def perform_destroy(self, instance):
        instance.is_deleted = True
        instance.save()

class OrderListCreateView(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

class OrderRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        order_details_qs = OrderDetails.objects.filter(order_ref=instance)
        order_details_serializer = OrderDetailsSerializer(order_details_qs, many=True)

        data = serializer.data
        data['order_details'] = order_details_serializer.data

        return Response(data)

    def perform_destroy(self, instance):
        instance.is_deleted = True
        instance.save()

class OrderDetailsListCreateView(generics.ListCreateAPIView):
    queryset = OrderDetails.objects.all()
    serializer_class = OrderDetailsSerializer

class OrderDetailsRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = OrderDetails.objects.all()
    serializer_class = OrderDetailsSerializer
    def perform_destroy(self, instance):
        instance.is_deleted = True
        instance.save()

