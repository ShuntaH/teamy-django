from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth import get_user_model

from teamy.forms import SearchForm
from .models import User, Department, Club

# Register your models here.

admin.site.register(User, UserAdmin)
admin.site.register(Department)
admin.site.register(Club)


class SearchFormAdmin(admin.ModelAdmin):
    form = SearchForm
