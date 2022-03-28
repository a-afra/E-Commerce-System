from rest_framework import serializers
from accounts.models import Customer, Order


class OrderSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Order
        fields = ['id', 'url']
        extra_kwargs = {'url': {'view_name': 'order-detail'}}


class OrderDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['id', 'title', 'detail']


class CustomerSerializer(serializers.ModelSerializer):
    orders = OrderSerializer(many=True)

    class Meta:
        model = Customer
        fields = ['id', 'username', 'email', 'password', 'orders']
        # password field will not appear in response to GET requests
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        customer = super().create(validated_data)
        customer.set_password(validated_data['password'])
        customer.save()
        return customer
