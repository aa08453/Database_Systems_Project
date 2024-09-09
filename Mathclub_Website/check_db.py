import os
import django
from django.conf import settings
from django.db import connections
from django.db.utils import OperationalError

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Mathclub_Website.settings')
django.setup()


def check_database_connection():
    db_conn = connections['default']
    try:
        db_conn.cursor()
        print('Database connection is successful!')
    except OperationalError:
        print('Database connection failed!')
        
if __name__ == "__main__":
    check_database_connection()