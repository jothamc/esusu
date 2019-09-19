from .models import Group
from rest_framework import viewsets,permissions,generics,filters,status
from rest_framework.response import Response
from .serializers import *
from random import choice
from .permissions import *

from members.models import Member
from payments.models import Payment
from payments.serializers import PaymentGroupSerializer
from payments.permissions import IsPayerOrAdmin

def collector_choice(queryset):
	"""
	function for selecting a collector for the monthly contributions

	In a real life situation, a sampling method would be 
		used to prevent a member from being picked more than once
	This function also ensures that a collector is not picked when only
	one member is in the group since the admin could be the first member
	or is that desired?
	"""
	for group in queryset:
		if group.collector is None and group.members.all().count() >= 2:
			members = group.members.all()
			collector = choice(members)
			group.collector = collector
			group.save()


class GroupListView(generics.ListCreateAPIView):
	"""
	Displays a list of all public groups 
	"""
	serializer_class = PartialGroupSerializer
	filter_backends = [filters.SearchFilter]
	search_fields = ['name','description']
	permission_classes = [permissions.IsAuthenticatedOrReadOnly]
	def get_queryset(self):
		"""
		This prevents the private groups from being displayed
		""" 
		queryset = Group.objects.exclude(is_searchable=False)
		collector_choice(queryset)
		self.queryset = queryset
		return queryset
	def perform_create(self,serializer):
		serializer.save(admin=self.request.user)




class GroupDetailView(generics.RetrieveUpdateDestroyAPIView):
	"""
	Group detail view giving different levels of access to admin and members
	"""
	serializer_class = FullGroupSerializer
	queryset = Group.objects.all()
	permission_classes = [permissions.IsAuthenticatedOrReadOnly,IsGroupAdmin]
	def get_queryset(self):
		queryset = Group.objects.all()
		collector_choice(queryset)
		return queryset
	def get_serializer_class(self,*args,**kwargs):
		if self.request.user == self.get_object().admin:
			return FullGroupSerializer
		return PartialGroupSerializer



class GroupPaymentsListView(generics.ListCreateAPIView):
	"""
		View displaying payments linked to current group to payers and admin
	"""
	serializer_class = PaymentGroupSerializer
	permission_classes = [permissions.IsAuthenticatedOrReadOnly,IsPayerOrAdmin]
	def get_queryset(self):
		pk = self.kwargs.get('pk')
		if self.request.user.is_authenticated:
			return Payment.objects.filter(group__pk=pk,payer=self.request.user)
		return Payment.objects.none()
	def perform_create(self,serializer):
		"""
		Sets the payer and group at creation
		"""
		pk = self.kwargs.get('pk')
		queryset = Payment.objects.filter(group__pk=pk,payer=self.request.user)
		if not queryset.exists():
			group = Group.objects.get(pk=pk)
			amount = group.savings_amount
			serializer.save(payer=self.request.user,group=group,amount=amount)


class GroupPaymentsDetailView(generics.RetrieveUpdateDestroyAPIView):
	"""
	API view that updates the current amount paid by logged in user
	The view increments the current amount using the amount set by the admin
	of the relevant group
	"""
	serializer_class = PaymentGroupSerializer
	permission_classes = [permissions.IsAuthenticatedOrReadOnly,IsPayerOrAdmin]
	def get_object(self):
		member_username = self.kwargs.get('member_username')
		group = self.kwargs.get('pk')
		return Payment.objects.get(group__pk=group,payer__username=member_username)
	def patch(self,request,*args,**kwargs):
		obj = self.get_object()
		obj.amount += obj.group.savings_amount
		obj.save()
		self.update(request,*args,**kwargs)





class AddMemberView(generics.RetrieveUpdateAPIView):
	"""
	API view that allows an admin to add a member to his group using member's username
	"""
	queryset = Group.objects.all()
	serializer_class = FullGroupSerializer
	permission_classes = [permissions.IsAuthenticatedOrReadOnly,IsGroupAdmin]

	def patch(self,request,*args,**kwargs):
		member_username = self.kwargs.get('member_username')
		group_pk = self.kwargs.get('group_pk')
		obj = self.get_object()
		member = Member.objects.get(username=member_username)
		if member not in obj.members.all():
			obj.members.add(member)
		obj.save()
		return self.partial_update(request,*args,**kwargs)





class GroupInviteView(generics.RetrieveUpdateAPIView):
	"""
	API View for sending out an invite using group uuid code
	Any logged-in user that visits the url is added to the group
	The view is accessed using a PUT request only
	"""
	queryset = Group.objects.all()
	serializer_class = FullGroupSerializer
	permission_classes = [permissions.IsAuthenticatedOrReadOnly]
	lookup_field = 'uuid'
	def patch(self,request,*args,**kwargs):
		member = request.user
		group_uuid = self.kwargs.get('uuid')
		queryset = Group.objects.filter(uuid=group_uuid)
		if queryset.exists() and queryset.count() == 1:
			queryset[0].members.add(member)
			queryset[0].save
		return self.partial_update(request,*args,**kwargs)
