import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service  
from webdriver_manager.chrome import ChromeDriverManager  
from django.db import connection
import os

#install selenium and wherever it is add it to python path

@pytest.fixture
def setup_driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()



@pytest.fixture
def setup_database():
    cursor = connection.cursor()
    cursor.execute(open('/home/hak/Desktop/synced/work/sem5/dbms/Database_django_project/Mathclub_Website/mathclub/tests/create_db.sql'.read()))
    yield connection  # This makes the connection available to the test
    connection.commit()
    connection.close()




@pytest.mark.django_db
def test_create_item(setup_driver):

    driver = setup_driver
    driver.get("http://localhost:8000/additem")
    driver.find_element(By.NAME, 'item_title').send_keys('Item_test')
    driver.find_element(By.NAME, 'item_price').send_keys('123')
    driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()

    # Verify item in database
    with connection.cursor() as cursor:


        query = """ SELECT * FROM Products """

        cursor.execute(query)

        assert cursor.fetchone()
    
