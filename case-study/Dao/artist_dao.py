import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import pyodbc
from entity.artist import Artist
from util.DBConnUtil import DBConnUtil

class ArtistDAO:

    def addArtist(self, artist: Artist) -> bool:
        try:
            conn = DBConnUtil.get_connection()
            cursor = conn.cursor()
            insert_query = '''
                INSERT INTO artist (name, biography, birth_date, nationality, website, contact_info)
                VALUES (?, ?, ?, ?, ?, ?)
            '''
            cursor.execute(insert_query, (
                artist.get_name(),
                artist.get_biography(),
                artist.get_birth_date(),
                artist.get_nationality(),
                artist.get_website(),
                artist.get_contact_info()
            ))
            conn.commit()
            return True
        except Exception as e:
            print(f"Error in adding artist: {e}")
            return False
        finally:
            if conn:
                conn.close()

    def getArtistById(self, artist_id: int):
        try:
            conn = DBConnUtil.get_connection()
            cursor = conn.cursor()
            select_query = "SELECT * FROM artist WHERE artist_id = ?"
            cursor.execute(select_query, (artist_id,))
            row = cursor.fetchone()
            if row:
                return Artist(*row)
            else:
                return None
        except Exception as e:
            print(f"Error in fetching artist by ID: {e}")
            return None
        finally:
            if conn:
                conn.close()

    def getAllArtists(self):
        try:
            conn = DBConnUtil.get_connection()
            cursor = conn.cursor()
            select_query = "SELECT * FROM artist"
            cursor.execute(select_query)
            rows = cursor.fetchall()
            artists = []
            for row in rows:
                artists.append(Artist(*row))
            return artists
        except Exception as e:
            print(f"Error in fetching all artists: {e}")
            return []
        finally:
            if conn:
                conn.close()

    def updateArtist(self, artist: Artist) -> bool:
        try:
            conn = DBConnUtil.get_connection()
            cursor = conn.cursor()
            update_query = '''
                UPDATE artist
                SET name = ?, biography = ?, birth_date = ?, nationality = ?, website = ?, contact_info = ?
                WHERE artist_id = ?
            '''
            cursor.execute(update_query, (
                artist.get_name(),
                artist.get_biography(),
                artist.get_birth_date(),
                artist.get_nationality(),
                artist.get_website(),
                artist.get_contact_info(),
                artist.get_artist_id()
            ))
            conn.commit()
            return cursor.rowcount > 0
        except Exception as e:
            print(f"Error in updating artist: {e}")
            return False
        finally:
            if conn:
                conn.close()

    def deleteArtist(self, artist_id: int) -> bool:
        try:
            conn = DBConnUtil.get_connection()
            cursor = conn.cursor()
            delete_query = "DELETE FROM artist WHERE artist_id = ?"
            cursor.execute(delete_query, (artist_id,))
            conn.commit()
            return cursor.rowcount > 0
        except Exception as e:
            print(f"Error in deleting artist: {e}")
            return False
        finally:
            if conn:
                conn.close()
