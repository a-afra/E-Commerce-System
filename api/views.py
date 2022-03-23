from rest_framework import viewsets
from accounts.models import Customer
from .serializers import CustomerSerializer


# Create your views here.
class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
