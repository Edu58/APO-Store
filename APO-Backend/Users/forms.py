from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import Customer


class CustomerCreationForm(UserCreationForm):
    class Meta:
        model = Customer
        fields = ("email",)


class CustomerUpdateForm(UserChangeForm):
    class Meta:
        model = Customer
        fields = ("email",)
