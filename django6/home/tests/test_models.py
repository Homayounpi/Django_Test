from django.test import TestCase
from home.models import Writer
from model_bakery import baker


class TestWriterModel(TestCase):

    def setUp(self):
        write = baker.make(Writer,f_name='ali',l_name='mmadii')

    def test_model_str(self):
        # write = Writer.objects.create(f_name='ali',l_name='mmadii',email='ali@gmail.com',country='Iran')
        write = baker.make(Writer,f_name='ali',l_name='mmadii')
        self.assertEqual(str(write),'ali mmadii')
