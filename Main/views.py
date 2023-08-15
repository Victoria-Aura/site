from django.shortcuts import render
from rest_framework import viewsets

from .serializers import UserSerializer
from MainModels.models import User

# Create your views here.
def index(request):
    return render(request,'main/index.html')

class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()