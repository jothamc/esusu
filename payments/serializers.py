# from django.contrib.auth.models import 
from rest_framework import serializers

from .models import Payment

class PaymentSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Payment
		fields = ['payer','group','datetime','amount','url']
		read_only_fields = fields


class PaymentGroupSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Payment
		fields = ['payer','group','datetime','amount','url']
		read_only_fields = ['payer','group']

