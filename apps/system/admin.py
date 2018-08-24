from django.contrib import admin
from django.contrib.auth import get_user_model
from . import models

User = get_user_model()


class UserAdmin(admin.ModelAdmin):
    list_display = ['name', 'username', 'mobile', 'email', 'gender']


admin.site.register(User, UserAdmin)
admin.site.register(models.Structure)
admin.site.register(models.Menu)
admin.site.register(models.Role)
