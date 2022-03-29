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
        fields = ['id', 'title', 'items', 'detail']


class CustomerSerializer(serializers.ModelSerializer):
    orders = OrderSerializer(many=True, required=False)

    class Meta:
        model = Customer
        fields = ['id', 'username', 'email', 'password', 'street_name', 'detail', 'orders']
        # password field will not appear in response to GET requests
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        customer = super().create(validated_data)
        customer.set_password(validated_data['password'])
        customer.save()
        return customer

    def update(self, instance, validated_data):
        instance.username = validated_data.get('username', instance.username)
        instance.email = validated_data.get('email', instance.email)
        instance.street_name = validated_data.get('street_name', instance.street_name)
        instance.detail = validated_data.get('detail', instance.detail)
        instance.save()
        return instance
