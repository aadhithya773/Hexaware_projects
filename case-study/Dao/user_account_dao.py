import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import pyodbc
from entity.user import UserAccount
from util.DBConnUtil import DBConnUtil

class UserAccountDAO:

    def addUser(self, user: UserAccount) -> bool:
        try:
            conn = DBConnUtil.get_connection()
            cursor = conn.cursor()
            insert_query = '''
                INSERT INTO user_account (username, password, email, first_name, last_name, date_of_birth, profile_picture)
                VALUES (?, ?, ?, ?, ?, ?, ?)
            '''
            cursor.execute(insert_query, (
                user.get_username(),
                user.get_password(),
                user.get_email(),
                user.get_first_name(),
                user.get_last_name(),
                user.get_date_of_birth(),
                user.get_profile_picture()
            ))
            conn.commit()
            return True
        except Exception as e:
            print(f"Error in adding user account: {e}")
            return False
        finally:
            if conn:
                conn.close()

    def getUserById(self, user_id: int):
        try:
            conn = DBConnUtil.get_connection()
            cursor = conn.cursor()
            select_query = "SELECT * FROM user_account WHERE user_id = ?"
            cursor.execute(select_query, (user_id,))
            row = cursor.fetchone()
            if row:
                return UserAccount(*row)
            else:
                return None
        except Exception as e:
            print(f"Error in fetching user by ID: {e}")
            return None
        finally:
            if conn:
                conn.close()

    def getAllUsers(self):
        try:
            conn = DBConnUtil.get_connection()
            cursor = conn.cursor()
            select_query = "SELECT * FROM user_account"
            cursor.execute(select_query)
            rows = cursor.fetchall()
            users = []
            for row in rows:
                users.append(UserAccount(*row))
            return users
        except Exception as e:
            print(f"Error in fetching all users: {e}")
            return []
        finally:
            if conn:
                conn.close()

    def updateUser(self, user: UserAccount) -> bool:
        try:
            conn = DBConnUtil.get_connection()
            cursor = conn.cursor()
            update_query = '''
                UPDATE user_account
                SET username = ?, password = ?, email = ?, first_name = ?, last_name = ?, date_of_birth = ?, profile_picture = ?
                WHERE user_id = ?
            '''
            cursor.execute(update_query, (
                user.get_username(),
                user.get_password(),
                user.get_email(),
                user.get_first_name(),
                user.get_last_name(),
                user.get_date_of_birth(),
                user.get_profile_picture(),
                user.get_user_id()
            ))
            conn.commit()
            return cursor.rowcount > 0
        except Exception as e:
            print(f"Error in updating user account: {e}")
            return False
        finally:
            if conn:
                conn.close()

    def deleteUser(self, user_id: int) -> bool:
        try:
            conn = DBConnUtil.get_connection()
            cursor = conn.cursor()
            delete_query = "DELETE FROM user_account WHERE user_id = ?"
            cursor.execute(delete_query, (user_id,))
            conn.commit()
            return cursor.rowcount > 0
        except Exception as e:
            print(f"Error in deleting user account: {e}")
            return False
        finally:
            if conn:
                conn.close()
