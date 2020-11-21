from django_filters import rest_framework, NumberFilter
import django
from .models import *
from rest_framework import viewsets, generics
from .serializers import *
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import HttpResponse

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filter_backends = (rest_framework.DjangoFilterBackend, )
    filter_fields = ('ID',)

class RecordViewSet(viewsets.ModelViewSet):
    queryset = Record.objects.all().order_by('-Score', 'RecordNum')[:10]
    serializer_class = RecordSerializer
    filter_backends = (rest_framework.DjangoFilterBackend, )
    filter_fields = ('RecordNum', 'user', 'Date', 'Score', 'Stage', )


class LoginedViewSet(viewsets.ModelViewSet):
    queryset = Logined.objects.all()
    serializer_class = LoginedSerializer
    filter_backends = (rest_framework.DjangoFilterBackend, )
    filter_fields = ('user', )

class wow(APIView):
    def get(self, request):
        print(request.user)
        print(request.auth)
        return HttpResponse(request.user)
