import pytest
from django.db import connection
import os

path = os.getcwd()

cwd = os.getcwd() 
population_path = os.path.join(cwd, 'mathclub', 'tests', 'create_db.sql')

@pytest.fixture(scope='session')
def django_db_setup(django_db_blocker):
    with django_db_blocker.unblock():
        with connection.cursor() as c:
            c.execute(open(population_path).read())

