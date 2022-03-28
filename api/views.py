import json
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.serializers import ValidationError
from django.contrib.auth import login, logout
from accounts.models import Customer, Order
from .serializers import CustomerSerializer, OrderDetailSerializer


# Create your views here.
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def customer_info(request):
    customer = Customer.objects.filter(username=request.user.username)
    serializer = CustomerSerializer(customer, many=True, context={'request': request})
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([AllowAny])
def customer_signup(request):
    serializer = CustomerSerializer(data=request.data)

    if serializer.is_valid():
        data = {}
        customer = serializer.save()
        customer.save()
        token = Token.objects.get_or_create(user=customer)[0].key
        data['message'] = 'Customer signed up successfully'
        data['email'] = customer.email
        data['username'] = customer.username
        data['token'] = token
        return Response(data, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@permission_classes([AllowAny])
def customer_login(request):
    data = {}
    # Requests must be sent in json format.
    body = json.loads(request.body)
    # logging customers in with their username
    # alternatively we can use email for credentials
    # email = body['email]
    username = body['username']
    password = body['password']
    try:
        customer = Customer.objects.get(username=username)
    except BaseException as e:
        raise ValidationError(str(e))

    token = Token.objects.get_or_create(user=customer)[0].key
    if not customer.check_password(raw_password=password):
        raise ValidationError('Login credentials is invalid.')

    if customer:
        login(request, customer)
        data['message'] = f'{customer.username} Logged in.'
        data['email'] = customer.email
        data['token'] = token
        return Response(data, status=status.HTTP_200_OK)
    else:
        raise ValidationError('customer not found.')


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def customer_logout(request):
    username = request.user.username
    request.user.auth_token.delete()
    logout(request)
    return Response(f'User: {username} logged out.', status=status.HTTP_200_OK)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def order_detail(request, pk):
    order = Order.objects.filter(id=pk)
    serializer = OrderDetailSerializer(order, many=True)
    return Response(serializer.data)
