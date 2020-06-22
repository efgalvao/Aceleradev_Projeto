from django.test import TestCase

# Create your tests here.

from django.test import TestCase
from .models import Event


class EventTestCase(TestCase):
    def test_should_return_attributes(self):
        self.assertTrue(hasattr(Event, 'level'))
        self.assertTrue(hasattr(Event, 'title'))
        self.assertTrue(hasattr(Event, 'details'))
        self.assertTrue(hasattr(Event, 'date'))
        self.assertTrue(hasattr(Event, 'name'))
        self.assertTrue(hasattr(Event, 'address'))
        self.assertTrue(hasattr(Event, 'user'))

    def test_should_create_item(self):
        person = Event.objects.create(level='CRITICAL', title='Blah', details='blah blah blah')
        self.assertIsNotNone(event)