from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    class Role(models.TextChoices):
        TESTER = "TESTER", "Security tester"
        ANALYST = "ANALYST", "Security analyst"
        ADMIN = "ADMIN", "Administrator"

    role = models.CharField(max_length=10, choices=Role.choices, default=Role.TESTER)

    def __str__(self):
        return f"{self.username} ({self.get_role_display()})"