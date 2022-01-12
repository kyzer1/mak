from django.contrib import admin
from .forms import CustomUserChangeForm, CustomUserCreationForm
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
User = get_user_model()
from salesman_profile.models import SalesmanAddress, SalesmanProfile, User

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = User
    list_display = ('email', 'is_staff', 'is_active', 'is_superuser')
    list_filter = ('email', 'is_staff', 'is_active',)
    fieldsets = (
        ('اطلاعات اصلی', {'fields': ('email', 'password', 'first_name')}),
        ('Permissions', {
         'fields': ('is_staff', 'is_active', 'user_permissions')}),
    )
    add_fieldsets = (
        ("اطلاعات کاربری", {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2',)
        },
        ), (
            "سطح دسترسی", {
                'fields': ('is_staff', 'is_active', 'user_permissions')
            }

        )
    )
    search_fields = ('is_staff',)
    ordering = ('email',)



admin.site.register(SalesmanProfile)
admin.site.register(SalesmanAddress)
admin.site.register(User, CustomUserAdmin)