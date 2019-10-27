from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Department, Member, Club

# Register your models here.


admin.site.register(User, UserAdmin)
admin.site.register(Department)
admin.site.register(Member)
admin.site.register(Club)
