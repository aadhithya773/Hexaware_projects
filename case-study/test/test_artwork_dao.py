import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import unittest
from dao.artwork_dao import ArtworkDAO
from entity.artwork import Artwork
from exception.custom_exceptions import ArtworkNotFoundException

class TestArtworkDAO(unittest.TestCase):

    def setUp(self):
        self.dao = ArtworkDAO()

    def test_add_artwork(self):
        artwork = Artwork(None, "Test Art", "Test Description", "Oil", 1500.0, "2025-04-29", 1)
        print(f"Inserting artwork: {artwork.get_title()}")
        result = self.dao.addArtwork(artwork)
        self.assertTrue(result)

    def test_update_artwork(self):
    # First insert a test record
        artwork = Artwork(None, "Temp Art", "Temp Desc", "Watercolor", 1200.0, "2025-04-29", 1)
        self.dao.addArtwork(artwork)

        # Retrieve last inserted ID (e.g., SELECT MAX(artwork_id) FROM Artwork)
        last_artwork = self.dao.getAllArtworks()[-1]
        artwork_id = last_artwork.get_artwork_id()

        # Now update the inserted artwork
        updated_artwork = Artwork(artwork_id, "Updated Art", "Updated Desc", "Acrylic", 2000.0, "2025-04-29", 1)
        result = self.dao.updateArtwork(updated_artwork)
        self.assertTrue(result)

    def test_delete_artwork(self):
        result = self.dao.deleteArtwork(1)
        self.assertTrue(result)

    def test_get_artwork_by_id(self):
        artwork = self.dao.getArtworkById(2)
        self.assertIsNotNone(artwork)
        self.assertEqual(artwork.get_artwork_id(), 2)

    def test_get_nonexistent_artwork(self):
        artwork = self.dao.getArtworkById(9999)
        self.assertIsNone(artwork)

if __name__ == "__main__":
    unittest.main()
