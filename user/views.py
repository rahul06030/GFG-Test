from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate, login, logout
from .models import Customer
from .serializers import CustomerSerializer

from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework import status
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from product.models import Order

class CustomerOrderInfoView(generics.ListAPIView):
    serializer_class = CustomerSerializer

    def get_queryset(self):
        ordered_param = self.request.query_params.get('ordered', None)
        if ordered_param is not None:
            if ordered_param == '1': # for customer with order
                return Customer.objects.filter(customer_id__in=Order.objects.values('customer_ref')).distinct()
            elif ordered_param == '0': # for customer without oerder
                return Customer.objects.exclude(customer_id__in=Order.objects.values('customer_ref')).distinct()
        return Customer.objects.all() #list of all the customers

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class CustomerLoginView(generics.CreateAPIView):
    serializer_class = CustomerSerializer

    def create(self, request, *args, **kwargs):
        username = request.data.get('username', None)
        password = request.data.get('password', None)
        if username and password:
            user = authenticate(username=username, password=password)
            login(request, user)
            if user:
                return Response({'message': "successfully logged in"}, status=status.HTTP_200_OK)
        return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

class CustomerLogoutView(generics.DestroyAPIView):
    def destroy(self, request, *args, **kwargs):
        logout(request)
        return Response({'message': 'Successfully logged out'}, status=status.HTTP_200_OK)


class CustomerRegistrationView(generics.CreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        customer = serializer.save()
        return Response({'message': 'Customer registered successfully' }, status=status.HTTP_201_CREATED)