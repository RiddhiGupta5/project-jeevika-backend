from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User
from .forms import CustomUserCreationForm, CustomUserChangeForm


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = User
    list_display = ('email', 'username', 'phone_no', 'is_staff', 'is_active',)
    list_filter = ('email', 'username', 'phone_no', 'is_staff', 'is_active',)
    fieldsets = (
        (None, {'fields': ('email', 'username', 'phone_no', 'password')}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'username', 'phone_no', 'password1', 'password2', 'is_staff', 'is_active')}
        ),
    )
    search_fields = ('email', 'username', 'phone_no')
    ordering = ('email', 'username', 'phone_no')

admin.site.register(User, CustomUserAdmin)