from django.contrib.auth.models import User
from rest_framework import serializers

from .models import Categories, Tasks, UserProfile

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "email"]


class TasksSerializer(serializers.ModelSerializer):
    author = serializers.HiddenField(default=serializers.CurrentUserDefault())
    author_info_display = serializers.SerializerMethodField()
    category_display = serializers.SerializerMethodField()
    repeat_days_display = serializers.SerializerMethodField()

    class Meta:
        model = Tasks
        fields = ["id", "title", "content", "time", "author_info_display", "category_display", "repeat_days_display",
                  "author", "category", "repeat_days",'status']

    def get_author_info_display(self, object):
        serializer = UserSerializer(object.author)
        return serializer.data

    def get_repeat_days_display(self, object):
        return object.repeat_days.split(" ")

    def get_category_display(self, object):
        serializer = CategoriesSerializer(object.category)
        return serializer.data


class CategoriesSerializer(serializers.ModelSerializer):
    created_user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    user_info_display = serializers.SerializerMethodField()

    class Meta:
        model = Categories
        fields = ["id", "category_name", "user_info_display", "created_user"]

    def get_user_info_display(self, object):
        serializer = UserSerializer(object.created_user)
        return serializer.data

class UserProfileSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    display_user = serializers.SerializerMethodField()

    class Meta:
        model = UserProfile
        fields = ['id', 'image', 'display_user','user']

    def get_display_user(self, object):
        serializer = UserSerializer(object.user)
        return serializer.data
