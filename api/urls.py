from django.urls import path, include
from . import views


urlpatterns = [
    path('customers/', views.customer_list),
    path('signup/', views.customer_signup),
    path('login/', views.customer_login),
    path('logout/', views.customer_logout),
]
