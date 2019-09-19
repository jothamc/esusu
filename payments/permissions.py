from rest_framework import permissions


class IsPayerOrAdmin(permissions.BasePermission):
	def has_object_permission(self,request,view,obj):
		if request.user == obj.payer or request.user == obj.group.admin:
			return True
		return False
