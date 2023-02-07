from django.contrib import admin

from .models import ShoppingSession

# Register your models here.
admin.site.register([
    ShoppingSession
])
