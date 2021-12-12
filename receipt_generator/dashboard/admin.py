from django.contrib import admin
from .models import Tenant, Home, Receipt


admin.site.register(Tenant)
admin.site.register(Home)
admin.site.register(Receipt)


