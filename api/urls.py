from django.urls import path, include
from . import views


urlpatterns = [
    path('customer-info/', views.customer_info, name='customer-info'),
    path('customer-update/', views.customer_update, name='customer-update'),
    path('orders/<int:pk>/', views.order_detail, name='order-detail'),
    path('signup/', views.customer_signup, name='signup'),
    path('login/', views.customer_login, name='login'),
    path('logout/', views.customer_logout, name='logout'),
]
