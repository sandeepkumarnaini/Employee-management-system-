from django.contrib.auth.models import User
from dbapp.models import Employee
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

class empserializer(serializers.ModelSerializer):
    class Meta:
        model=Employee
        fields=['empno','empname','empsal','bonus']

class customserializer(serializers.Serializer):
    empno=serializers.IntegerField()
    empname=serializers.CharField()
    empsal=serializers.IntegerField()
    bonus=serializers.IntegerField()
    def validate_empsal(self,sal):
        if sal<0:
            raise ValidationError('negative values are not allowed')
        else:
            return sal
    def create(self,validated_data):
        return Employee.objects.create(**validated_data)

class userserializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['username','password','email']