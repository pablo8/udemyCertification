from nsApp.customer.models import Customer
from rest_framework import serializers
from nsApp.order.serializers import OrderSerializer


class CustomerSerializer(serializers.ModelSerializer):
    orders = OrderSerializer(read_only=True, many=True)

    class Meta:
        model = Customer
        fields = "__all__"
