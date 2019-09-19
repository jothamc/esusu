from django.urls import path,include
from .views import *

urlpatterns = [
	path('',GroupListView.as_view(),name='group-list'),
	path('<int:pk>/',GroupDetailView.as_view(),name='group-detail'),
	path('<int:pk>/payments/',GroupPaymentsListView.as_view(),name='payment-list'),
	path('<int:pk>/payments/<str:member_username>/',GroupPaymentsDetailView.as_view(),name='payment-detail'),
	path('<int:pk>/add-<str:member_username>/',AddMemberView.as_view(),name='member-add'),
	path('invite-<uuid:uuid>/',GroupInviteView.as_view(),name='group-invite'),
]