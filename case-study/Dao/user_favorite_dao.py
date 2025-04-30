import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import pyodbc
from util.DBConnUtil import DBConnUtil

class UserFavoriteArtworkDAO:

    def addFavorite(self, user_id: int, artwork_id: int) -> bool:
        try:
            conn = DBConnUtil.get_connection()
            cursor = conn.cursor()
            insert_query = '''
                INSERT INTO user_favorite_artwork (user_id, artwork_id)
                VALUES (?, ?)
            '''
            cursor.execute(insert_query, (user_id, artwork_id))
            conn.commit()
            return True
        except Exception as e:
            print(f"Error in adding favorite artwork: {e}")
            return False
        finally:
            if conn:
                conn.close()

    def removeFavorite(self, user_id: int, artwork_id: int) -> bool:
        try:
            conn = DBConnUtil.get_connection()
            cursor = conn.cursor()
            delete_query = '''
                DELETE FROM user_favorite_artwork
                WHERE user_id = ? AND artwork_id = ?
            '''
            cursor.execute(delete_query, (user_id, artwork_id))
            conn.commit()
            return cursor.rowcount > 0
        except Exception as e:
            print(f"Error in removing favorite artwork: {e}")
            return False
        finally:
            if conn:
                conn.close()

    def getFavoritesByUser(self, user_id: int):
        try:
            conn = DBConnUtil.get_connection()
            cursor = conn.cursor()
            select_query = '''
                SELECT artwork_id FROM user_favorite_artwork WHERE user_id = ?
            '''
            cursor.execute(select_query, (user_id,))
            rows = cursor.fetchall()
            return [row.artwork_id for row in rows]
        except Exception as e:
            print(f"Error in fetching favorites by user: {e}")
            return []
        finally:
            if conn:
                conn.close()
