from django.shortcuts import render
from rest_framework import generics
from nsApp.order.models import Order
from nsApp.order.serializers import OrderSerializer


class ListOrder(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class DetailOrder(generics.RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
