from django.urls import path, include
from . import views


urlpatterns = [
    path('customers/', views.customer_info),
    path('orders/<int:pk>/', views.order_detail, name='order-detail'),
    path('signup/', views.customer_signup),
    path('login/', views.customer_login),
    path('logout/', views.customer_logout),
    #path('orders/', views.order_detail),
]
