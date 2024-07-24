# serializers.py
from rest_framework import serializers
from django.contrib.auth.models import Group
from App.AppStatus import AppStatus
from App.AppFileds import AppFileds
from App.AppFlow import AppFlow
from App.AppAccess import AppAccess
from App.AppView import AppView

class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ['id', 'name']  # Only include the fields you want

class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = AppStatus
        fields = ['id','app_id', 'status','order']  

class FieldSerializer(serializers.ModelSerializer):
    class Meta:
        model = AppFileds
        fields = [
                    'id',
                    'app_id', 
                    'title', 
                    'type', 
                    'required', 
                    'access',
                    'db_field',                    
                    'order'
                 ]

class AppFlowSerializer(serializers.ModelSerializer):
    class Meta:
        model = AppFlow
        fields = [
                    'id',
                    'app_id', 
                    'from_status', 
                    'action_by_type', 
                    'action_by_filed', 
                    'action_by_grp', 
                    'action', 
                    'to_status', 
                    'custom_action',
                    'order'
                 ] 

class AppAccessSerializer(serializers.ModelSerializer):
    class Meta:
        model = AppAccess
        fields = [
                    'id',
                    'app_id', 
                    'order',
                    'name', 
                    'status', 
                    'type', 
                    'group', 
                    'action_by_filed', 
                    'field', 
                    'access' 
                 ] 

class AppViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = AppView
        fields = [
                    'id',
                    'app_id', 
                    'order',
                    'title', 
                    'html', 
                    'js'                    
                 ] 