from django.test import TestCase
from django.contrib.auth.models import User
from myapp.models import Greenhouse, Plant, InGreenhouse, Compatibility, Temperature, PlantCare

class GreenhouseModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        User.objects.create_user(username='testuser', password='12345')
        test_user = User.objects.get(username='testuser')
        Greenhouse.objects.create(user=test_user, rows=5, row_length=10)

    def test_greenhouse_content(self):
        greenhouse = Greenhouse.objects.get(id=1)
        expected_user = f'{greenhouse.user}'
        expected_rows = f'{greenhouse.rows}'
        expected_row_length = f'{greenhouse.row_length}'
        self.assertEqual(expected_user, 'testuser')
        self.assertEqual(expected_rows, '5')
        self.assertEqual(expected_row_length, '10.0')

