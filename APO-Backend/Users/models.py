from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils.translation import gettext_lazy as _


# Create your models here.
class AccountManager(BaseUserManager):
    def create_user(self, email, password, **extra_fields):
        """
        Creates a new Customer. Emails and Phone Numbers are unique identifiers. Email and Password are used to log
        in customers
        """
        if not email:
            raise ValueError(_("A valid email is required"))

        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)  # extra fields caters for fields like is_active
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        """
        Creates a superuser who basically have all rights and permissions to do anything and access everything in the
        system
        """
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError(_("Superuser must have is_staff option as True"))
        elif extra_fields.get("is_superuser") is not True:
            raise ValueError(_("Superuser must have is_superuser option as True"))

        return self.create_user(email, password, **extra_fields)


class Account(AbstractBaseUser, PermissionsMixin):
    """
    This model is used to create a new customer. In this model, we also specify that the email is to be used as the
    email field, and we should use the CustomUserManager created above instead
    """

    class UserRoles(models.TextChoices):
        CUSTOMER = "Customer", "Customer"
        ADMIN = "Admin", "Admin",

    email = models.EmailField(_("email address"), unique=True, null=False, blank=False)
    role = models.CharField(max_length=8, choices=UserRoles.choices, default=UserRoles.CUSTOMER)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = AccountManager()

    def __str__(self):
        return self.email

    def roles(self):
        return self.UserRoles.values


class Profile(models.Model):
    account = models.OneToOneField(Account, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50, null=False, blank=False)
    middle_name = models.CharField(max_length=50, null=True, blank=True)
    last_name = models.CharField(max_length=50, null=False, blank=False)

    def __str__(self):
        return self.account.email


class CustomerAddress(models.Model):
    account_id = models.ForeignKey(Account, on_delete=models.CASCADE)
    country = models.CharField(max_length=100, null=False, blank=False)
    city = models.CharField(max_length=100, null=False, blank=False)
    postal_code = models.CharField(max_length=100, null=False, blank=False)
    address_line1 = models.CharField(max_length=100, null=False, blank=False)
    address_line2 = models.CharField(max_length=100, null=False, blank=True)
    telephone = models.CharField(max_length=100, null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-created_at',)

    def __str__(self):
        return self.address_line1


class CustomerPayment(models.Model):
    class PaymentTypes(models.TextChoices):
        CASH = "Cash", "Cash"
        MOBILE_PAYMENTS = "Mobile Payment", "Mobile Payment"
        CREDIT_CARD = "Credit Card", "Credit Card"

    class PaymentProviders(models.TextChoices):
        STRIPE = "Stripe", "Stripe"
        PAYPAL = "PayPal", "PayPal"
        MPESA = "M-Pesa", "M-Pesa"

    account_id = models.ForeignKey(Account, on_delete=models.CASCADE)
    payment_type = models.CharField(max_length=15, choices=PaymentTypes.choices, default=PaymentTypes.MOBILE_PAYMENTS)
    provider = models.CharField(max_length=6, choices=PaymentProviders.choices, default=PaymentProviders.STRIPE)
    account_no = models.CharField(max_length=100, null=False, blank=True)
    expiry = models.CharField(max_length=100, null=False, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-created_at',)

    def __str__(self):
        return self.payment_type
