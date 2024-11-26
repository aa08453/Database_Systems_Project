import pytest
from django.db import connection
import os
import sys
from datetime import datetime

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from myutils import *

live_server_url = "http://localhost:8000"


@pytest.mark.django_db
def test_create_session():
    user_id = 1
    create_session(user_id)

    with connection.cursor() as cursor:
        cursor.execute(
            """
            select * from sessions where user_id = %s
            """, [user_id]
        )
        result = cursor.fetchone()

        assert result is not None
        assert result[1] == user_id
        session_key = result[0] 

    delete_session(session_key)

    with connection.cursor() as cursor:
        cursor.execute(
            """
            select * from sessions where session_key = %s
            """, [session_key]
        )
        result = cursor.fetchone()
        assert result is None


