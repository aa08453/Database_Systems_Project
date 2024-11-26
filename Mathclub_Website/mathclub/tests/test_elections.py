import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service  
from webdriver_manager.chrome import ChromeDriverManager  
from selenium.webdriver.common.keys import Keys
from django.db import connection
import os
from datetime import datetime

live_server_url = "http://localhost:8000"

#install selenium and wherever it is add it to python path

@pytest.fixture
def setup_driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

@pytest.mark.django_db
def test_election_create(setup_driver):
    driver = setup_driver
    driver.get(f"{live_server_url}/election/create")

    with connection.cursor() as cursor:
        print("Before")
        cursor.execute("select * from election")
        print(cursor.fetchall())

    start_date = "01-12-2024 10:10 AM"
    end_date = "01-12-2024 12:13 AM"


    input_format = "%d-%m-%Y %I:%M %p"
    output_format = "%Y-%d-%m %H:%M"

    # Convert start_date and end_date to the database format
    start_date_db = datetime.strptime(start_date, input_format).strftime(output_format)
    end_date_db = datetime.strptime(end_date, input_format).strftime(output_format)

    print("Start:", start_date_db)
    print("End:", end_date_db)

    start_splitted = start_date.split(" ")

    start_date_elem = driver.find_element(By.NAME, "start_date")
    start_date_elem.send_keys(start_splitted[0], Keys.TAB,
                              start_splitted[1], start_splitted[2]
                              )

    end_date_elemn = driver.find_element(By.NAME, "end_date")
    end_splitted = end_date.split(" ")

    end_date_elem = driver.find_element(By.NAME, "end_date")

    end_date_elem.send_keys(end_splitted[0], Keys.TAB,
                              end_splitted[1], end_splitted[2]
                              )

    print(start_splitted)
    print(end_splitted)


    driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()

    with connection.cursor() as cursor:
        print("After")
        cursor.execute("select * from election")
        print(cursor.fetchall())

        query = f"SELECT * FROM election WHERE start_date = %s AND end_date = %s"
        print(query)
        cursor.execute(query, [start_date_db, end_date_db])

        assert cursor.fetchone()
