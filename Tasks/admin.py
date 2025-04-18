from django.contrib import admin

from .models import Categories, Tasks, UserProfile,Group

admin.site.register(Tasks)
admin.site.register(Categories)
admin.site.register(UserProfile)
admin.site.register(Group)
