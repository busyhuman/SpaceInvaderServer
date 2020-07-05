from django_filters import rest_framework, NumberFilter
import django
from .models import User, Record
from rest_framework import viewsets, generics
from .serializers import UserSerializer, RecordSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filter_backends = (rest_framework.DjangoFilterBackend, )
    filter_fields = ('ID', 'PW',)

class RecordViewSet(viewsets.ModelViewSet):
    queryset = Record.objects.all()
    serializer_class = RecordSerializer
    filter_backends = (rest_framework.DjangoFilterBackend, )
    filter_fields = ('RecordNum', 'user', 'Date', 'Score',)