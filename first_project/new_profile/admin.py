from django.contrib import admin
from new_profile.models import User_Data , Bill_Data

def disable(modeladmin, request, queryset):
    for member in queryset:
        member.status = '3'
        member.save()
disable.short_description = 'Disable selected User'

def enable(modeladmin, request, queryset):
    for member in queryset:
        member.status = '2'
        member.save()
enable.short_description = 'Enable selected User'

class UserAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'father_name', 'mobile']
    actions = [enable, disable, ]
# Register your models here.

admin.site.register(User_Data, UserAdmin)
admin.site.register(Bill_Data)