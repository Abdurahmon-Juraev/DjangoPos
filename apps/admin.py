from django.contrib import admin
from django.contrib.auth.models import User

from apps.models import Category


@admin.register(Category)
class UserAdmin(admin.ModelAdmin):
    list_display = 'name',



