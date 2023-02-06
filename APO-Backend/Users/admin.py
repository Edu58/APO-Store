from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import AccountCreationForm, AccountUpdateForm
from .models import Account, CustomerAddress, CustomerPayment


# Register your models here.
class AccountAdmin(UserAdmin):
    add_form = AccountCreationForm
    form = AccountUpdateForm
    model = Account
    list_display = ("email", "role", "is_staff", "is_active",)
    list_filter = ("email", "role", "is_staff", "is_active",)

    fieldsets = [
        (None, {
            "fields": ("email", "password")
        }),
        ("Permissions", {
            "fields": ("groups", "user_permissions", "role", "is_staff", "is_active")
        })
    ]

    add_fieldsets = [
        (None, {
            "classes": ("wide",),
            "fields": (
                "email", "password1", "password2", "groups", "user_permissions", "role", "is_staff", "is_active"
            )
        })
    ]

    search_fields = ("email", "role",)
    ordering = ("email",)


admin.site.register(Account, AccountAdmin)
admin.site.register([
    CustomerAddress,
    CustomerPayment
])
