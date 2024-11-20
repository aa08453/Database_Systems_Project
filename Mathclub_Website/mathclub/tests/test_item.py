import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service  
from webdriver_manager.chrome import ChromeDriverManager  
import os


cache_path = os.path.expanduser("~/.wdm/drivers//")

binary_path = os.path.exists(os.path.join(cache_path, "chromedriver"));

if binary_path:
    driver_path = binary_path
else:
    driver_path = ChromeDriverManager().install()


service = Service(binary_path)
options = webdriver.ChromeOptions()

@pytest.fixture
def setup_driver():
    self.driver = webdriver.Chrome(service=service, options=options)
    yield self.driver
    self.driver.quit()

@pytest.mark.django_db
def test_create_item(setup_driver):
    self.driver = setup_driver
    self.driver.get("http://localhost:8000/create/")
    self.driver.find_element(By.NAME, 'item_name').send_keys('Item_test')
    self.driver.find_element(By.NAME, 'item_price').send_keys('123')
    self.driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()

    # Verify item in database
    with connection.cursor() as cursor:
        query = """
        SELECT TOP 1 * 
        FROM ITEMS
        WHERE Product_Name = %s AND Price = %s
        """

        cursor.execute(query, ['Item_test', 123])

        assert cursor.fetchone()
    
