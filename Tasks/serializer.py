from django.contrib.auth.models import User
from rest_framework import serializers

from .models import Tasks,Categories

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','username','email']

class TasksSerializer(serializers.ModelSerializer):
    author = serializers.HiddenField(default=serializers.CurrentUserDefault())
    category = serializers.HiddenField(default=None)
    repeat_days = serializers.HiddenField(default=None)
    author_info_display = serializers.SerializerMethodField()
    category_display = serializers.SerializerMethodField()
    repeat_days_display = serializers.SerializerMethodField()
    class Meta:
        model = Tasks
        fields = ['title','content','time','author_info_display','category_display','repeat_days_display','author','category','repeat_days']

    def get_author_info_display(self):
        serializer = UserSerializer(self.author)
        return serializer.data

    def get_repeat_days_display(self):
        return self.repeat_days.split(' ')

    def get_category_display(self):
        serializer = CategoriesSerializer(self.category)
        return serializer.data

class CategoriesSerializer(serializers.ModelSerializer):
    created_user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    user_info_display = serializers.SerializerMethodField()
    class Meta:
        model = Categories
        fields = ['category_name','user_info_display','created_user']

    def get_user_info_display(self):
        serializer = UserSerializer(self.created_user)
        return serializer.data