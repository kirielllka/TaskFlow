from django.contrib.auth.models import User
from rest_framework import serializers

from .models import Tasks,Categories

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','username','email']

class TasksSerializer(serializers.ModelSerializer):
    author = serializers.HiddenField(default=serializers.CurrentUserDefault())
    author_info_display = serializers.SerializerMethodField()
    category_display = serializers.SerializerMethodField()
    repeat_days_display = serializers.SerializerMethodField()
    class Meta:
        model = Tasks
        fields = ['id','title','content','time','author_info_display','category_display','repeat_days_display','author','category','repeat_days']

    def get_author_info_display(self, object):
        serializer = UserSerializer(object.author)
        return serializer.data

    def get_repeat_days_display(self, object):
        return object.repeat_days.split(' ')

    def get_category_display(self, object):
        serializer = CategoriesSerializer(object.category)
        return serializer.data

class CategoriesSerializer(serializers.ModelSerializer):
    created_user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    user_info_display = serializers.SerializerMethodField()
    class Meta:
        model = Categories
        fields = ['id','category_name','user_info_display','created_user']

    def get_user_info_display(self, object):
        serializer = UserSerializer(object.created_user)
        return serializer.data