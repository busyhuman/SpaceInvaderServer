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


class RecordListView(APIView):
    def get(self, request):
        ListCount = 10
        queryset = Record.objects.all()

        mRecordNum = request.GET.get('RecordNum')
        mScore = request.GET.get('Score')
        mStage = request.GET.get('Stage')
        muser = request.GET.get('user')
        mDate = request.GET.get('Date')

        if request.GET.get('RecordNum') is not None:
            queryset = queryset.filter(RecordNum = mRecordNum)

        if request.GET.get('Score') is not None:
            queryset = queryset.filter(Score = mScore)

        if request.GET.get('Stage') is not None:
            queryset = queryset.filter(Stage = mStage)

        if request.GET.get('user') is not None:
            queryset = queryset.filter(user = muser)

        if request.GET.get('Date') is not None:
            queryset = queryset.filter(Date = mDate)

        queryset = queryset.order_by('-Score', 'RecordNum')[:ListCount]

        serializer = RecordSerializer(queryset, many=True)
        return Response(serializer.data);


    def post(self, request):
        print(request.user)
        queryset = Record.objects.create(user=get_object_or_404(User, pk=request.user), Stage=request.data['Stage'], Score=request.data['Score'])

        return Response("Being Added !!")


class RecordDetailView(APIView):
    def get(self, request, rid):
        queryset = Record.objects.filter(RecordNum = rid)
        serializer = RecordSerializer(queryset, many=True)
        return Response(serializer.data);


class Auth(APIView):
    def get(self, request):
        print(request.user)
        print(request.auth)
        return HttpResponse(request.user)

    def post(self, request):
        print("data =", request.data['id'])
        user = authenticate(username=request.data['id'], password=request.data['password'])
        print("user =", user)
        if user is not None:
            token = Token.objects.get(user=user)
            return HttpResponse(token.key)
        else:
            return HttpResponse("shit~")
