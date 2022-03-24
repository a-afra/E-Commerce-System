from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from accounts.models import Customer
from .serializers import CustomerSerializer


# Create your views here.
@api_view(['GET'])
def customer_list(request):
    customers = Customer.objects.all()
    serializer = CustomerSerializer(customers, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def add_customer(request):
    serializer = CustomerSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
