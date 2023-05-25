from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.viewsets import ModelViewSet
from django.contrib.auth.models import User
from .serializers import UserSerializer

# Create your views here.

@api_view(['POST'])
def logout(request):
    request.user.auth_token.delete(    )
    return Response({'message': 'User Logout: Token deleted.'})

class UserView(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    