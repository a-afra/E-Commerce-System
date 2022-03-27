from rest_framework import serializers
from accounts.models import Customer


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['username', 'email', 'password']
        # password field will not appear in GET requests
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        customer = super().create(validated_data)
        customer.set_password(validated_data['password'])
        customer.save()
        return customer
