from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomerCreationForm, CustomerUpdateForm
from .models import Customer


# Register your models here.
class CustomerAdmin(UserAdmin):
    add_form = CustomerCreationForm
    form = CustomerUpdateForm
    model = Customer
    list_display = ("email", "is_staff", "is_active",)
    list_filter = ("email", "is_staff", "is_active",)

    fieldsets = [
        (None, {
            "fields": ("email", "password")
        }),
        ("Permissions", {
            "fields": ("groups", "user_permissions", "is_staff", "is_active")
        })
    ]

    add_fieldsets = [
        (None, {
            "classes": ("wide",),
            "fields": (
                "email", "password1", "password2", "groups", "user_permissions", "is_staff", "is_active"
            )
        })
    ]

    search_fields = ("email",)
    ordering = ("email",)


admin.site.register(Customer, CustomerAdmin)
