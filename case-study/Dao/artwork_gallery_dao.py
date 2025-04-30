import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pyodbc
from util.DBConnUtil import DBConnUtil
from entity.artwork import Artwork

class ArtworkGalleryDAO:

    def addArtworkToGallery(self, artwork_id: int, gallery_id: int) -> bool:
        conn = None
        try:
            conn = DBConnUtil.get_connection()
            cursor = conn.cursor()
            insert_query = '''
                INSERT INTO artwork_gallery (artwork_id, gallery_id)
                VALUES (?, ?)
            '''
            cursor.execute(insert_query, (artwork_id, gallery_id))
            conn.commit()
            return True
        except Exception as e:
            print(f"Error in adding artwork to gallery: {e}")
            return False
        finally:
            if conn:
                conn.close()

    def removeArtworkFromGallery(self, artwork_id: int, gallery_id: int) -> bool:
        conn = None
        try:
            conn = DBConnUtil.get_connection()
            cursor = conn.cursor()
            delete_query = '''
                DELETE FROM artwork_gallery
                WHERE artwork_id = ? AND gallery_id = ?
            '''
            cursor.execute(delete_query, (artwork_id, gallery_id))
            conn.commit()
            return cursor.rowcount > 0
        except Exception as e:
            print(f"Error in removing artwork from gallery: {e}")
            return False
        finally:
            if conn:
                conn.close()

    def getGalleriesForArtwork(self, artwork_id: int):
        conn = None
        try:
            conn = DBConnUtil.get_connection()
            cursor = conn.cursor()
            select_query = '''
                SELECT gallery_id FROM artwork_gallery WHERE artwork_id = ?
            '''
            cursor.execute(select_query, (artwork_id,))
            rows = cursor.fetchall()
            return [row.gallery_id for row in rows]
        except Exception as e:
            print(f"Error in fetching galleries for artwork: {e}")
            return []
        finally:
            if conn:
                conn.close()


    def getArtworksByGallery(self, gallery_id: int):
        conn = None
        try:
            conn = DBConnUtil.get_connection()
            cursor = conn.cursor()
            select_query = '''
                SELECT a.artwork_id, a.title, a.description, a.creation_date, a.medium, a.image_url, a.artist_id
                FROM artwork a
                INNER JOIN artwork_gallery ag ON a.artwork_id = ag.artwork_id
                WHERE ag.gallery_id = ?
            '''
            cursor.execute(select_query, (gallery_id,))
            rows = cursor.fetchall()
            artworks = []
            for row in rows:
                artwork = Artwork(
                    artwork_id=row[0],
                    title=row[1],
                    description=row[2],
                    creation_date=row[3],
                    medium=row[4],
                    image_url=row[5],
                    artist_id=row[6]
                )
                artworks.append(artwork)
            return artworks
        except Exception as e:
            print(f"Error in fetching artworks by gallery: {e}")
            return []
        finally:
            if conn:
                conn.close()
