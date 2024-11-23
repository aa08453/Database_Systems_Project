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


@pytest.fixture
def test_create_session():
    user_id = 1
    create_session(user_id)

    with connection.cursor() as cursor:
        cursor.execute(
            """
            select * from sessions
            """
        )
        print("All sessions")
        print(cursor.fetchall())

        print("Required session:")
        cursor.execute(
            """
            select * from sessions where user_id = %s
            """, [user_id]
        )
        print(cursor.fetchone())



