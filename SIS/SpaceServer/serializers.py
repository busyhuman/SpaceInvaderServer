from rest_framework import serializers
from .models import *
from django import forms

class UserSerializer(serializers.ModelSerializer):
    PW = forms.CharField(widget=forms.PasswordInput)
    class Meta :
        model = User
        fields = '__all__'

class RecordSerializer(serializers.ModelSerializer):
    class Meta :
        model = Record
        fields = '__all__'


class LoginedSerializer(serializers.ModelSerializer):
    class Meta :
        model = Logined
        fields = '__all__'
