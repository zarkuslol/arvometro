import sys
sys.path.append('.')

from utils.db import DataBase

db = DataBase()

db.test_connection()
