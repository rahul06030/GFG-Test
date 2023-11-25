from django.urls import path
from .views import CustomerLoginView, CustomerOrderInfoView, CustomerLogoutView, CustomerRegistrationView

urlpatterns = [
    path('customer/register/', CustomerRegistrationView.as_view(), name='customer-register'),
    path('customer/login/', CustomerLoginView.as_view(), name='customer-login'),
    path('customer/logout/', CustomerLogoutView.as_view(), name='customer-logout'),
    path('customer/', CustomerOrderInfoView.as_view(), name='customer-order-info'),
]
