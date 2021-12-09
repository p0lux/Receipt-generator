from django.contrib import admin
from .models import User, Tenant, Home, Receipt


class UserList(admin.ModelAdmin):
    list_display = ['name', 'email', 'sudo']
    search_fields = ['name']
    list_filter = ['sudo']
    readonly_fields = ['id']


admin.site.register(User, UserList)
admin.site.register(Tenant)
admin.site.register(Home)
admin.site.register(Receipt)


