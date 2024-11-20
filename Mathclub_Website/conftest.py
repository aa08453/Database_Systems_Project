import pytest
from django.db import connection


@pytest.fixture(scope='session')
def django_db_setup(django_db_blocker):
    with django_db_blocker.unblock():
        with connection.cursor() as c:
            c.execute(open('/home/hak/Desktop/synced/work/sem5/dbms/Database_django_project/Mathclub_Website/mathclub/tests/create_db.sql').read())

