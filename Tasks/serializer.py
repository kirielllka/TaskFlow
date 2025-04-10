from django.contrib.auth.models import User
from rest_framework import serializers

from .models import Tasks,Categories

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','username','email']

class TasksSerializer(serializers.ModelSerializer):
    author = serializers.HiddenField(default=serializers.CurrentUserDefault())
    category = serializers.HiddenField(default=serializers.CurrentUserDefault())
    repeat_days = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class