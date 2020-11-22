from django_filters import rest_framework, NumberFilter
import django
from .models import *
from rest_framework import viewsets, generics
from .serializers import *
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import HttpResponse

from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from django.shortcuts import get_object_or_404


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filter_backends = (rest_framework.DjangoFilterBackend, )
    filter_fields = ('ID',)


class RecordViewSet(APIView):
    def get(self, request):
        queryset = Record.objects.all().order_by('-Score', 'RecordNum')[:10]
        serializer = RecordSerializer(queryset, many=True)
        return Response(serializer.data);
      #  serializer_class = RecordSerializer
      #  filter_backends = (rest_framework.DjangoFilterBackend, )
      #  filter_fields = ('RecordNum', 'user', 'Date', 'Score', 'Stage', )

    def post(self, request):
        queryset = Record.objects.create(user=get_object_or_404(User, pk=request.user), Stage=request.data['Stage'], Score=request.data['Score'])

        return Response("Being Added !!")
