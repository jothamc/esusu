from rest_framework import permissions

class IsGroupAdmin(permissions.BasePermission):
	def has_object_permission(self,request,view,obj):
		return request.user == obj.admin

class IsPaymentGroupAdmin(permissions.BasePermission):
	def has_object_permission(self,request,view,obj):
		return request.user == obj.group.admin