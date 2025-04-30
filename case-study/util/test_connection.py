# test_connection.py
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from util.DBConnUtil import DBConnUtil

conn = DBConnUtil.get_connection()
if conn:
    print("You're good to go! 🎉")
