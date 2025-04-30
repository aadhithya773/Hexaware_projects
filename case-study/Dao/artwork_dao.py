
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import pyodbc
from entity.artwork import Artwork
from util.DBConnUtil import DBConnUtil

class ArtworkDAO:

    def addArtwork(self, artwork: Artwork) -> bool:
        try:
            conn = DBConnUtil.get_connection()
            cursor = conn.cursor()
            insert_query = '''
                INSERT INTO artwork (title, description, creation_date, medium, image_url, artist_id)
                VALUES (?, ?, ?, ?, ?, ?)
            '''
            cursor.execute(insert_query, (
                artwork.get_title(),
                artwork.get_description(),
                artwork.get_creation_date(),
                artwork.get_medium(),
                artwork.get_image_url(),
                artwork.get_artist_id()
            ))
            conn.commit()
            return True
        except Exception as e:
            print(f"Error in adding artwork: {e}")
            return False
        finally:
            if conn:
                conn.close()

    def getArtworkById(self, artwork_id: int):
        try:
            conn = DBConnUtil.get_connection()
            cursor = conn.cursor()
            select_query = "SELECT * FROM artwork WHERE artwork_id = ?"
            cursor.execute(select_query, (artwork_id,))
            row = cursor.fetchone()
            if row:
                return Artwork(*row)
            else:
                return None
        except Exception as e:
            print(f"Error in fetching artwork by ID: {e}")
            return None
        finally:
            if conn:
                conn.close()

    def getAllArtworks(self):
        try:
            conn = DBConnUtil.get_connection()
            cursor = conn.cursor()
            select_query = "SELECT * FROM artwork"
            cursor.execute(select_query)
            rows = cursor.fetchall()
            artworks = []
            for row in rows:
                artworks.append(Artwork(*row))
            return artworks
        except Exception as e:
            print(f"Error in fetching all artworks: {e}")
            return []
        finally:
            if conn:
                conn.close()

    def updateArtwork(self, artwork: Artwork) -> bool:
        try:
            conn = DBConnUtil.get_connection()
            cursor = conn.cursor()
            update_query = '''
                UPDATE artwork
                SET title = ?, description = ?, creation_date = ?, medium = ?, image_url = ?, artist_id = ?
                WHERE artwork_id = ?
            '''
            cursor.execute(update_query, (
                artwork.get_title(),
                artwork.get_description(),
                artwork.get_creation_date(),
                artwork.get_medium(),
                artwork.get_image_url(),
                artwork.get_artist_id(),
                artwork.get_artwork_id()
            ))
            conn.commit()
            return cursor.rowcount > 0
        except Exception as e:
            print(f"Error in updating artwork: {e}")
            return False
        finally:
            if conn:
                conn.close()

    def deleteArtwork(self, artwork_id: int) -> bool:
        try:
            conn = DBConnUtil.get_connection()
            cursor = conn.cursor()
            delete_query = "DELETE FROM artwork WHERE artwork_id = ?"
            cursor.execute(delete_query, (artwork_id,))
            conn.commit()
            return cursor.rowcount > 0
        except Exception as e:
            print(f"Error in deleting artwork: {e}")
            return False
        finally:
            if conn:
                conn.close()
