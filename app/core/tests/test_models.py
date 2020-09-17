from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):

    def test_create_with_email_successful(self):
        """Test creating a new user with an email is successful"""
        email = 'test@mail.com'
        username = 'UsernameTest'
        password = "TestPass123"
        user = get_user_model().objects.create_user(
            email=email,
            username=username,
            password=password,
        )

        self.assertEqual(user.email, email)
        self.assertEqual(user.username,  username)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """Test the email for a new user is normalized"""
        username = "testusername"
        email = 'test@MAIL.COM'
        user = get_user_model().objects.create_user(
            username=username,
            email=email,
            password='test123'
        )

        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        """Test creating user with no email raise error"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(
                email=None,
                username='UsernameTest',
                password='1234Test'
            )

    def test_new_user_invalid_username(self):
        """Test creating user with no email raise error"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(
                email='test@mail.com',
                username=None,
                password='1234Test'
            )

    def test_create_new_superuser(self):
        """Test creating a new superuser"""
        user = get_user_model().objects.create_superuser(
            username='test',
            email='test@mail.com',
            password='1234test'
        )

        self.assertTrue(user.is_staff)
        self.assertTrue(user.is_superuser)
