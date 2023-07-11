from django.contrib.auth.models import AbstractUser
from django.db import models

USER = 'user'
OWNER = 'owner'

ROLE_CHOICES = (
    (USER, 'User'),
    (OWNER, 'Owner'),
)


class User(AbstractUser):
    """Custom User model."""
    username = models.CharField(
        max_length=150,
        unique=True,
    )
    email = models.EmailField(
        max_length=250,
        unique=True,
    )
    phone = models.PositiveIntegerField(
        max_length=11,
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

    @property
    def is_user(self):
        """Default user."""
        return self.role == USER

    @property
    def is_owner(self):
        """User is owner playground."""
        return self.role == OWNER

    class Meta:
        ordering = ('username',)
        default_related_name = 'users'

    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name}'
