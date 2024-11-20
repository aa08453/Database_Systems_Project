from django.test import TestCase

from django.contrib.auth.models import User
from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Create your tests here.

options = webdriver.ChromeOptions()
service = Service(ChromeDriverManager().install())


class CrudTest(LiveServerTestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(service=service, options=options)

    def tearDown(self):
        self.driver.quit()

    def test_add_product:
        self.driver.get(f"{self.live_server_url}/login/")
        self.driver.find_element(By.NAME, "item_title").send_keys('testitem')
        self.driver.find_element(By.NAME, "item_price").send_keys('123', Keys.RETURN)




