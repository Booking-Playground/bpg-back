from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser, PermissionsMixin
from django.db import models

USER = "user"
OWNER = "owner"

ROLE_CHOICES = (
    (USER, "User"),
    (OWNER, "Owner"),
)


class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        """
        Создает и сохраняет пользователя с указанным email и паролем.
        """
        if not email:
            raise ValueError("The Email field must be set")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        """
        Создает и сохраняет суперпользователя с указанным email и паролем.
        """
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        return self.create_user(email, password, **extra_fields)


class User(AbstractUser):
    """Custom User model."""

    username = None
    email = models.EmailField(
        max_length=250,
        unique=True,
    )
    phone = models.PositiveIntegerField(
        unique=True,
    )
    first_name = models.CharField(
        max_length=150,
    )
    last_name = models.CharField(
        max_length=150,
    )
    role = models.CharField(
        max_length=max(len(role) for role, _ in ROLE_CHOICES),
        choices=ROLE_CHOICES,
        default=USER,
        blank=True,
    )
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = (
        "phone",
        "first_name",
        "last_name",
    )
    objects = CustomUserManager()

    @property
    def is_user(self):
        """Default user."""
        return self.role == USER

    @property
    def is_owner(self):
        """User is owner playground."""
        return self.role == OWNER

    class Meta:
        ordering = ("email",)
        default_related_name = "users"

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name} ({self.email})"
