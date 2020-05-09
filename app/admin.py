from django.contrib import admin
from .models import CustomUser, CustomToken

admin.site.register(CustomUser)
admin.site.register(CustomToken)