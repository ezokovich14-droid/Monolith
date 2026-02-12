from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('products/', views.products, name='products'),
    path('orders/', views.orders, name='orders'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('test-api/', views.test_api, name='test_api'),
    
    # 🚨 DÉMONSTRATIONS POUR LA CLASSE
    path('demo/crash-total/', views.crash_everything, name='crash_demo'),
    path('demo/resilient/', views.resilient_feature, name='resilient_demo'),
]
