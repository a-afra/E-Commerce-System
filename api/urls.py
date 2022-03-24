from django.urls import path, include
from rest_framework import routers
from . import views

"""router = routers.DefaultRouter()
router.register(r'customers', views.CustomerViewSet)"""

urlpatterns = [
    path('customers/', views.customer_list),
    path('add/', views.add_customer),
    path('auth/', include('rest_framework.urls', namespace='rest_framework'))  # endpoint for authentication
]
