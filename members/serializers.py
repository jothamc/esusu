# from django.contrib.auth.models import 
from rest_framework import serializers, permissions
from .models import Member


class MemberSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Member
		fields = ['first_name','last_name','email','username','uuid','date_joined','password']
		extra_kwargs = {'password':{'write_only':True}}
		read_only_fields = ['date_joined']

	def create(self,validated_data):
		"""
		Method to set and hash password using Django's auth system on creation of instance
		"""
		member = Member(
			email = validated_data['email'],
			username = validated_data['username'],
			first_name = validated_data['first_name'],
			last_name = validated_data['last_name'],
		)
		member.set_password(validated_data['password'])
		member.save()
		return member