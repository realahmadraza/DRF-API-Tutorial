from django.contrib.auth.models import User, Group
from .serializers import Userserializer, Groupserializer
from rest_framework import viewsets, permissions


class Userviewset(viewsets.ModelViewSet):
    serializer_class = Userserializer
    queryset = User.objects.all().order_by('-date_joined')
    permission_classes = [permissions.IsAuthenticated]


class Groupviewset(viewsets.ModelViewSet):
    serializer_class = Groupserializer
    queryset = Group.objects.all().order_by('name')
    permission_classes = [permissions.IsAuthenticated]