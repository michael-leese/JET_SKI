from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    role = models.CharField(max_length=20, default="admin")
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=True)
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

class Experience(models.Model):
    slug = models.SlugField(unique=True)
    name = models.CharField(max_length=120)
    description = models.TextField(blank=True)
    duration_min = models.PositiveIntegerField(default=60)
    base_price = models.IntegerField(help_text="cents")
    active = models.BooleanField(default=True)

class Booking(models.Model):
    PENDING = "pending"; PAID = "paid"; CANCELLED = "cancelled"; EXPIRED="expired"
    STATUS = [(PENDING,PENDING),(PAID,PAID),(CANCELLED,CANCELLED),(EXPIRED,EXPIRED)]
    name = models.CharField(max_length=120)
    email = models.EmailField()
    experience = models.ForeignKey(Experience, on_delete=models.PROTECT)
    start_time = models.DateTimeField()
    status = models.CharField(max_length=10, choices=STATUS, default=PENDING)
    stripe_session_id = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

class Payment(models.Model):
    booking = models.OneToOneField(Booking, on_delete=models.CASCADE)
    amount = models.IntegerField()
    currency = models.CharField(max_length=10, default="EUR")
    status = models.CharField(max_length=20, default="pending")
    stripe_payment_intent = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

class GalleryImage(models.Model):
    url = models.CharField(max_length=255)
    category = models.CharField(max_length=50, default="general")
    created_at = models.DateTimeField(auto_now_add=True)

class ContactMessage(models.Model):
    name = models.CharField(max_length=120)
    email = models.EmailField()
    message = models.TextField()
    status = models.CharField(max_length=20, default="new")
    created_at = models.DateTimeField(auto_now_add=True)
