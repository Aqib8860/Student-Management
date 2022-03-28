from rest_framework import serializers
from .models import User
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


# Login Serializer
class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    
    def validate(self, attrs):
        data = super(CustomTokenObtainPairSerializer, self).validate(attrs)
        
        data.update({'id': self.user.id})
        data.update({'user': self.user.email})
        data.update({'name': self.user.name})
        data.update({'is_teacher': self.user.is_teacher})
    
        return data


# User Register Serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', 'password', 'name', 'is_teacher', 'is_student']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        refresh = RefreshToken.for_user(instance)

        return instance


# List Students Serializer
class StudentSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['id', 'email', 'password', 'name']


# List All Users Serializer
class AllUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['id', 'email', 'password', 'name', 'is_teacher', 'is_student']

