from rest_framework import serializers
from .models import Group

# class GroupSerializer(serializers.HyperlinkedModelSerializer):
# 	admin = serializers.ReadOnlyField(source='admin.username')
# 	class Meta:
# 		model = Group
# 		fields = ['admin','name','description','max_capacity',
# 		'is_searchable','savings_amount','started','url']
# 		read_only_fields = ['name','description','max_capacity','started','savings_amount','is_searchable']

class FullGroupSerializer(serializers.HyperlinkedModelSerializer):
	admin = serializers.ReadOnlyField(source='admin.username')
	class Meta:
		model = Group
		fields = ['admin','members','name','description','max_capacity',
		'is_searchable','savings_amount','started','url','collector','uuid',]
		read_only_fields = ['collector']


class PartialGroupSerializer(serializers.HyperlinkedModelSerializer):
	admin = serializers.ReadOnlyField(source='admin.username')
	class Meta:
		model = Group
		fields = ['admin','name','description','max_capacity',
		'is_searchable','savings_amount','started','url','uuid']
		read_only_fields = fields

	