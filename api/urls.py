from django.urls import path, include
from . import views


urlpatterns = [
    path('customer-info/', views.customer_info),
    path('customer-update/', views.customer_update),
    path('orders/<int:pk>/', views.order_detail, name='order-detail'),
    path('signup/', views.customer_signup),
    path('login/', views.customer_login),
    path('logout/', views.customer_logout),
    #path('orders/', views.order_detail),
]
