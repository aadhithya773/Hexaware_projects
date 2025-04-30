import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import unittest
from dao.gallery_dao import GalleryDAO
from entity.gallery import Gallery

class TestGalleryDAO(unittest.TestCase):

    def setUp(self):
        self.dao = GalleryDAO()

    def test_add_gallery(self):
        gallery = Gallery(None, "Nature Collection", "Nature-themed artworks", 1)
        result = self.dao.addGallery(gallery)
        self.assertTrue(result)

    def test_update_gallery(self):
        gallery = Gallery(1, "Updated Gallery", "Updated Desc", 1)
        result = self.dao.updateGallery(gallery)
        self.assertTrue(result)

    def test_delete_gallery(self):
        result = self.dao.deleteGallery(1)
        self.assertTrue(result)

    def test_get_gallery_by_id(self):
        gallery = self.dao.getGalleryById(2)
        self.assertIsNotNone(gallery)
        self.assertEqual(gallery.get_gallery_id(), 2)

    def test_get_nonexistent_gallery(self):
        gallery = self.dao.getGalleryById(9999)
        self.assertIsNone(gallery)

if __name__ == "__main__":
    unittest.main()
