from .models import Payment
from rest_framework import viewsets,permissions,generics
from .serializers import PaymentSerializer
from .permissions import IsPayerOrAdmin
# Create your views here.

class PaymentListView(generics.ListAPIView):
	"""
	Displays payments relevant to admins and logged in members
	Only payers can update their payments using a PUT request
	"""
	queryset = Payment.objects.all()
	serializer_class = PaymentSerializer
	permission_classes = [IsPayerOrAdmin,permissions.IsAuthenticatedOrReadOnly]

	def get_queryset(self):
		"""
		Only logged in users and group admins can see payments
		"""
		if self.request.user.is_authenticated:
			return Payment.objects.filter(payer=self.request.user) | Payment.objects.filter(group__admin=self.request.user)
		return Payment.objects.none()



class PaymentDetailView(generics.RetrieveUpdateDestroyAPIView):
	queryset = Payment.objects.all()
	serializer_class = PaymentSerializer
	permission_classes = [IsPayerOrAdmin,permissions.IsAuthenticatedOrReadOnly]