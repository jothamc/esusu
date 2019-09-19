from .models import Member
from django.contrib.auth import login,authenticate
from django.http import HttpResponse
from rest_framework import generics,permissions,decorators
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from .serializers import MemberSerializer

class MemberListView(generics.ListCreateAPIView):
	"""
	API endpoint that allows members to be viewed or edited
	"""
	queryset = Member.objects.all()
	serializer_class = MemberSerializer



class MemberDetailView(generics.RetrieveUpdateDestroyAPIView):
	"""
	API endpoint that allows members to be viewed or edited
	"""
	queryset = Member.objects.all()
	serializer_class = MemberSerializer
	permission_classes = [permissions.IsAuthenticatedOrReadOnly]



@api_view(['GET','POST'])
def login(request):
	if request.method == "POST":
		username = request.data['username']
		password = request.data['password']
		user = authenticate(request,username=username,password=password)
		if user is not None:
			try:
				login(request,user)
				return Response({"username":request.data['username']})
			except:
				return Response({"username":request.data['username']})
		return Response(status=status.HTTP_403_FORBIDDEN)
		
	elif request.method == "GET":
		return Response('Please send data via POST')

