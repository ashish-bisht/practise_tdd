from django.test import TestCase
from django.contrib.auth import get_user_model


class ModeTests(TestCase):
    def test_create_user_with_email_success(self):
        """ Positive test case to create test user with email """
        email = 'test@test.com'
        password = "password"
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))



    def test_new_user_email_normalised(self):
        """ Test email for new user is normalised """
        email = 'test@TEST.COM'
        user = get_user_model().objects.create_user(email, 'test123')
        self.assertEqual(user.email, email.lower())


    def test_new_user_invalid_email(self):
        """ create user without email"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user("", "heythere")


    def test_create_new_superuser(self):
        user = get_user_model().objects.create_superuser(
            'test@test.com',
            'password'
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)