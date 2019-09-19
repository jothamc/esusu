from django.urls import path,include
from .views import *


urlpatterns = [
	path('',MemberListView.as_view(),name='member-list'),
	path('<int:pk>/',MemberDetailView.as_view(),name='member-detail'),
	path('login/',login,name='member-login'),
]