from django.test import TestCase
from .models import Animals
# import library
import unittest
# Create your tests here.

# create a class
class TestXXXXX(unittest.TestCase):

    def setUp(self):
        Animals.objects.all().delete()
        Animals.objects.create(name="Cow", sound="Mua")
        Animals.objects.create(name="Dog", sound="Bhow")

    def test_animals_can_speak(self):
        """Animals that can speak are correctly identified"""
        lion = Animals.objects.get(name="Cow")
        cat = Animals.objects.get(name="Dog")
        self.assertEqual(lion.animal_sounds(), 'Cow says Mua')
        self.assertEqual(cat.animal_sounds(), 'Dog says Bhow')

   

# driver code
if __name__ == '__main__':

	unittest.main()
