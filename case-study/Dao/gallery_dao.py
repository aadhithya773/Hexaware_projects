import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import pyodbc
from entity.gallery import Gallery
from util.DBConnUtil import DBConnUtil

class GalleryDAO:

    def addGallery(self, gallery: Gallery) -> bool:
        try:
            conn = DBConnUtil.get_connection()
            cursor = conn.cursor()
            insert_query = '''
                INSERT INTO gallery (name, description, location, curator_id, opening_hours)
                VALUES (?, ?, ?, ?, ?)
            '''
            cursor.execute(insert_query, (
                gallery.get_name(),
                gallery.get_description(),
                gallery.get_location(),
                gallery.get_curator_id(),
                gallery.get_opening_hours()
            ))
            conn.commit()
            return True
        except Exception as e:
            print(f"Error in adding gallery: {e}")
            return False
        finally:
            if conn:
                conn.close()

    def getGalleryById(self, gallery_id: int):
        try:
            conn = DBConnUtil.get_connection()
            cursor = conn.cursor()
            select_query = "SELECT * FROM gallery WHERE gallery_id = ?"
            cursor.execute(select_query, (gallery_id,))
            row = cursor.fetchone()
            if row:
                return Gallery(*row)
            else:
                return None
        except Exception as e:
            print(f"Error in fetching gallery by ID: {e}")
            return None
        finally:
            if conn:
                conn.close()

    def getAllGalleries(self):
        try:
            conn = DBConnUtil.get_connection()
            cursor = conn.cursor()
            select_query = "SELECT * FROM gallery"
            cursor.execute(select_query)
            rows = cursor.fetchall()
            galleries = []
            for row in rows:
                galleries.append(Gallery(*row))
            return galleries
        except Exception as e:
            print(f"Error in fetching all galleries: {e}")
            return []
        finally:
            if conn:
                conn.close()

    def updateGallery(self, gallery: Gallery) -> bool:
        try:
            conn = DBConnUtil.get_connection()
            cursor = conn.cursor()
            update_query = '''
                UPDATE gallery
                SET name = ?, description = ?, location = ?, curator_id = ?, opening_hours = ?
                WHERE gallery_id = ?
            '''
            cursor.execute(update_query, (
                gallery.get_name(),
                gallery.get_description(),
                gallery.get_location(),
                gallery.get_curator_id(),
                gallery.get_opening_hours(),
                gallery.get_gallery_id()
            ))
            conn.commit()
            return cursor.rowcount > 0
        except Exception as e:
            print(f"Error in updating gallery: {e}")
            return False
        finally:
            if conn:
                conn.close()

    def deleteGallery(self, gallery_id: int) -> bool:
        try:
            conn = DBConnUtil.get_connection()
            cursor = conn.cursor()
            delete_query = "DELETE FROM gallery WHERE gallery_id = ?"
            cursor.execute(delete_query, (gallery_id,))
            conn.commit()
            return cursor.rowcount > 0
        except Exception as e:
            print(f"Error in deleting gallery: {e}")
            return False
        finally:
            if conn:
                conn.close()
