from django.test import TestCase

from .models import User


class UserModelTests(TestCase):
    def test_new_user_has_default_role_and_hashed_password(self):
        user = User.objects.create_user(username="newtester", password="StrongPass#123")
        self.assertEqual(user.role, User.Role.TESTER)
        self.assertNotEqual(user.password, "StrongPass#123")
        self.assertTrue(user.check_password("StrongPass#123"))