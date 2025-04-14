from django.contrib import admin

from .models import Categories, Tasks

admin.site.register(Tasks)
admin.site.register(Categories)
