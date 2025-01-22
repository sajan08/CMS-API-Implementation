from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.validators import MinLengthValidator, RegexValidator
from django.contrib.auth.models import User

class CustomUser(AbstractUser):
    ROLE_CHOICES = (('admin', 'Admin'), ('author', 'Author'))
    
    email = models.EmailField(unique=True)
    phone = models.CharField(
        max_length=10,
        validators=[RegexValidator(r'^\d{10}$', message="Phone number must be 10 digits")]
    )
    address = models.TextField(blank=True, null=True)
    city = models.CharField(max_length=50, blank=True, null=True)
    state = models.CharField(max_length=50, blank=True, null=True)
    country = models.CharField(max_length=50, blank=True, null=True)
    pincode = models.CharField(
        max_length=6,
        validators=[RegexValidator(r'^\d{6}$', message="Pincode must be 6 digits")]
    )
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='author')
    groups = models.ManyToManyField(
        "auth.Group",
        related_name="customuser_groups",  # 👈 Add this to avoid clash
        blank=True
    )
    user_permissions = models.ManyToManyField(
        "auth.Permission",
        related_name="customuser_permissions",  # 👈 Add this to avoid clash
        blank=True
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'phone', 'role']

    def __str__(self):
        return self.email


class Content(models.Model):
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    title = models.CharField(max_length=30)
    body = models.TextField(max_length=300)
    summary = models.CharField(max_length=60)
    document = models.FileField(upload_to='documents/', blank=True, null=True)
    categories = models.CharField(max_length=100)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
