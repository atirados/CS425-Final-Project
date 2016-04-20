from django.contrib import admin
from login.models import UserProfile


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'address', 'phone')

    fieldsets = [
        ('Main Info', {
         'fields': ['user', 'ccNumber', 'ccType', 'expDate', 'address', 'phone']}),
        ('Membership', {'fields': ['status', 'credits']}),
    ]


# Register your models here.
admin.site.register(UserProfile, UserProfileAdmin)
