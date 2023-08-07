from django.contrib import admin
from django.contrib.auth import get_user_model

from Plattypus.account.models import PlattypusUser

UserModel = get_user_model()


class UserModelAdmin(admin.ModelAdmin):

    list_display = ("username", "first_name", "last_name", "email", "date_of_birth", "last_login")
    search_fields = ("first_name", "last_name", "email")
    list_filter = ("username", "first_name", "last_name", "email", "date_of_birth")
    ordering = ["username"]
    readonly_fields = ['last_login']


admin.site.register(UserModel, UserModelAdmin)
