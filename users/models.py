from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    username = models.CharField(unique=True)
    email = models.EmailField(verbose_name="email", unique=True)
    tg_id = models.CharField(null=True, blank=True, max_length=100)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    class Meta:
        verbose_name = "пользователь"
        verbose_name_plural = "пользователи"

    groups = models.ManyToManyField(
        "auth.Group",
        related_name="customuser_set",
        blank=True,
        help_text="Группы, к которым принадлежит пользователь..",
        verbose_name="группы",
    )

    user_permissions = models.ManyToManyField(
        "auth.Permission",
        related_name="customuser_set",
        blank=True,
        help_text="Специфические разрешения для пользователя.",
        verbose_name="права пользователя",
    )

    def __str__(self):
        return self.username
