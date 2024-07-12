# serializers.py
from rest_framework import serializers
from django.contrib.auth.models import Group
from App.AppStatus import AppStatus
from App.AppFileds import AppFileds

class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ['id', 'name']  # Only include the fields you want

class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = AppStatus
        fields = ['id','app_id', 'status']  

class FieldSerializer(serializers.ModelSerializer):
    class Meta:
        model = AppFileds
        fields = ['id','app_id', 'title', 'type', 'required', 'db_filed'] 