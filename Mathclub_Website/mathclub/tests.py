from django.test import TestCase

from django.contrib.auth.models import User
from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from mathclub.models import Product

import time

# Create your tests here.



class CrudTest(LiveServerTestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def tearDown(self):
        self.driver.quit()

    def test_add_product(self):
        self.driver.get(f"{self.live_server_url}/additem")
        self.driver.find_element(By.NAME, 'item_title').send_keys('Item_test')
        self.driver.find_element(By.NAME, 'item_price').send_keys('123')
        self.driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()

        product_exists = Product.objects.filter(product_name='Item_test', price=123).exists()
        assert(product_exists)








