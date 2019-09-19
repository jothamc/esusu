from django.urls import path,include
from .views import *

urlpatterns = [
	path('',PaymentListView.as_view(),name='payment-list'),
	path('<int:pk>/',PaymentDetailView.as_view(),name='payment-detail'),
]