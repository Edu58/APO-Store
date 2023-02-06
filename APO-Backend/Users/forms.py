from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import Account


class AccountCreationForm(UserCreationForm):
    class Meta:
        model = Account
        fields = ("email",)


class AccountUpdateForm(UserChangeForm):
    class Meta:
        model = Account
        fields = ("email",)
