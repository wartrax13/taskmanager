from django.http import HttpRequest
from django.test import TestCase
from django.urls import resolve
from taskmanager.item.models import Item
from taskmanager.item.views import home_page

# Create your tests here.
class HomePageTest(TestCase):
    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)
       
    def test_uses_home_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'home.html')
    
    def test_can_save_a_POST_request(self):
        response = self.client.post('/', data={'item_text': 'BLABLABLA'})
        self.assertIn('BLABLABLA', response.content.decode())
    
    def test_only_saves_items_when_necesssary(self):
        self.client.get('/')
        self.assertEqual(Item.objects.count(), 0)

class ItemModelTest(TestCase):
    def test_saving_and_retrieving_items(self):
        first_item = Item()
        first_item.description = 'O primeiro'
        first_item.save()

        second_item = Item()
        second_item.description = 'O segundo'
        second_item.save()

        saved_items = Item.objects.all()
        self.assertEqual(saved_items.count(), 2)