from datetime import datetime
from django.db import connection
import uuid

def fetch_elections():
    with connection.cursor() as cursor:
        cursor.execute("select election_id, start_date, end_date from election")
        elections = cursor.fetchall()
        return [
            {"id" : row[0], "start_date" : row[1], "end_date" : row[2]}
            for row in elections
        ]


def fetch_priv(user_id):
    with connection.cursor() as cursor:
        cursor.execute("select privilege from users where user_id = %s", user_id)
        result = cursor.fetchone()
        if (result):
            return True 
        else:
            return False


def generate_session_key():
    return str(uuid.uuid4())

def create_session(user_id):
    session_key = generate_session_key() 

    with connection.cursor() as cursor:
        cursor.execute(
            """
            insert into sessions (session_key, user_id) values (%s, %s)
            """, [session_key, user_id]
        )
    return session_key

def is_logged_in(user_id):
    with connection.cursor() as cursor:
        cursor.execute(
            """
            select session_key, user_id from sessions where user_id = %s
            """, [user_id]
        )
        if cursor.fetchone() is not None: 
            return True
        else:
            return False


def delete_session(session_key):
    with connection.cursor() as cursor:
        cursor.execute(
            """
            delete from sessions where session_key = %s
            """, [session_key]
        )

