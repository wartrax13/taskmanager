from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import unittest

class NewVisitorTest(LiveServerTestCase):

    def setUp(self) -> None:
        self.browser = webdriver.Chrome()

    def tearDown(self) -> None:
        self.browser.quit()
        
    def test_can_start_a_list_and_retrieve_it_later(self):    
        self.browser.get(self.live_server_url)
        self.assertIn('Task Manager', self.browser.title)
        self.fail('Finish the test!')

if __name__ == '__main__':
    unittest.main(warnings='ignore')
