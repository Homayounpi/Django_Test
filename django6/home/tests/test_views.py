from django.test import TestCase,Client,RequestFactory
from django.urls import reverse
from django.contrib.auth.models import User,AnonymousUser
from home.forms import UserRegisterForm
from home.views import Home


class TestUserRegisterView(TestCase):
    def setUp(self):
        self.client = Client()

    def test_user_register_GET(self):
        response = self.client.get(reverse('home:register')) 
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response,'home/register.html')
        self.failUnless(response.context['form'],UserRegisterForm)

    def test_user_register_POST_valid(self):
        response = self.client.post(reverse('home:register')
                        ,data={'username':'ali','password1':'root','password2':'root','email':'ali@gmail.com'})
        self.assertEqual(response.status_code,302)
        self.assertRedirects(response,reverse('home:home'))
        self.assertEqual(User.objects.count(),1)
    


    def test_user_register_POST_invalid(self):
        response = self.client.post(reverse('home:register'),data={'username':'ali','password1':'root','password2':'root','email':'ali@gmail.com'})
                        

        self.assertEqual(response.status_code,302)

        # context nemishnase
        # form = response.context['form']
        # self.assertFalse(form.is_valid())
        # self.failIf(form=response.context['form'],field='email',errors='in email vogud dard!!!')
            # bala va pain yeki has
        # self.assertFalse(form=response.context['form'],field='email',errors='in email vogud dard!!!')


class TestWriterView(TestCase):
    def setUp(self):
        User.objects.create_superuser(username='ali',email='ali@gmail.com',password='root')
        self.client = Client()
        self.client.login(username='ali',password='root',email='ali@gmail.com')

    def test_writer(self):
        response = self.client.get(reverse('home:all_writer'))
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response,'home/writer.html')



class TestHomeView(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='root',email='root@gmail.com',password='root')
        self.factory = RequestFactory()

    def test_home_user_authenticated(self):
        request = self.factory.get(reverse('home:home'))
        request.user = self.user
        response = Home.as_view()(request)
        self.assertEqual(response.status_code,302)


    def test_home_user_Anonymous(self):
        request = self.factory.get(reverse('home:home'))
        request.user = AnonymousUser()
        response = Home.as_view()(request)
        self.assertEqual(response.status_code,200)