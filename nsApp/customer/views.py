from django.shortcuts import render
from nsApp.customer.models import Customer
from nsApp.customer.serializers import CustomerSerializer
from rest_framework import  generics


class ListCustomer(generics.ListCreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


class DetailCustomer(generics.RetrieveUpdateDestroyAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

