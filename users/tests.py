from django.test import TestCase
from django.db import IntegrityError
from users.models import CustomUser


class CustomUserModelTest(TestCase):
    """Тесты для кастомной модели пользователя CustomUser."""

    def setUp(self):
        """Создаём базового пользователя для тестов."""
        self.user_data = {
            "email": "test@example.com",
            "username": "testuser",
            "password": "securepassword123",
        }
        self.user = CustomUser.objects.create_user(**self.user_data)

    def test_create_user(self):
        """Проверка создания обычного пользователя."""
        self.assertEqual(self.user.email, "test@example.com")
        self.assertEqual(self.user.username, "testuser")
        self.assertTrue(self.user.check_password("securepassword123"))
        self.assertFalse(self.user.is_staff)
        self.assertFalse(self.user.is_superuser)

    def test_create_superuser(self):
        """Проверка создания суперпользователя."""
        superuser = CustomUser.objects.create_superuser(
            email="admin@example.com", username="admin", password="adminpass123"
        )
        self.assertTrue(superuser.is_staff)
        self.assertTrue(superuser.is_superuser)
        self.assertEqual(superuser.email, "admin@example.com")

    def test_email_unique(self):
        """Проверка уникальности email."""
        with self.assertRaises(IntegrityError):
            CustomUser.objects.create_user(
                email="test@example.com", username="anotheruser", password="pass123"  # тот же email
            )

    def test_username_unique(self):
        """Проверка уникальности username."""
        with self.assertRaises(IntegrityError):
            CustomUser.objects.create_user(
                email="another@example.com", username="testuser", password="pass123"  # тот же username
            )

    def test_str_method(self):
        """Проверка метода __str__."""
        self.assertEqual(str(self.user), "testuser")

    def test_username_field_is_email(self):
        """Проверка, что USERNAME_FIELD установлен как 'email'."""
        self.assertEqual(CustomUser.USERNAME_FIELD, "email")

    def test_required_fields_include_username(self):
        """Проверка, что username в REQUIRED_FIELDS."""
        self.assertIn("username", CustomUser.REQUIRED_FIELDS)

    def test_email_field_is_emailfield(self):
        """Проверка, что поле email — это EmailField (опционально, но полезно)."""
        email_field = CustomUser._meta.get_field("email")
        self.assertEqual(email_field.__class__.__name__, "EmailField")

    def test_tg_id_can_be_null(self):
        """Проверка, что tg_id может быть пустым."""
        user = CustomUser.objects.create_user(email="tguser@example.com", username="tguser", password="pass123")
        self.assertIsNone(user.tg_id)
