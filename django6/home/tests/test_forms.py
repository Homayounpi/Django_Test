from django.test import TestCase
from home.forms import UserRegisterForm
from django.contrib.auth.models import User


class TestRegisterForm(TestCase):
    """
    The code snippet provided defines a test case class in Python using the Django testing
    framework.
    """

    @classmethod
    def setUpTestData(cls):
        
        User.objects.create_user(username='a',email='a@gmail.com',password='aaaa')
        return super().setUpTestData()

    def test_valid_data(self):
        form = UserRegisterForm(
            data={'username':'ali','password1':'root','password2':'root','email':'mmad@gmqil.com'})
        self.assertTrue(form.is_valid())

    def test_empty_data(self):
        form = UserRegisterForm(data={})
        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors),4)
    def test_exist_email(self):
        form = UserRegisterForm(            
            data={'username':'b','password1':'bbbb','password2':'bbbb','email':'a@gmail.com'}
            )
        self.assertEqual(len(form.errors),1)
        self.assertTrue(form.has_error('email'))
    def test_unmatched_passwords(self):
        form = UserRegisterForm(
               data={'username':'ali','password1':'root','password2':'root2','email':'mm313ad@gmqil.com'})
        self.assertEqual(len(form.errors),1)
        self.assertTrue(form.has_error)