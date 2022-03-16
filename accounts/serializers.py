from rest_framework import serializers
from .models import Customer


class CustomerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Customer
        fields = ['username', 'email', 'password']
