import unittest
from addons.od_product.models.extended_product_template import ExtendedProductTemplate

'''
    Contains the test cases for ExtendedProductTemplate class.
'''
class TestExtendedProductTemplate(unittest.TestCase):

    '''
        Test Case for when the slug field is re-computed as a result of a change event.
    '''
    def test_compute_slug(self):
        actual = [{ "name": "Drawer"}, { "name": "Window Hanger/Section"}]
        expected = [{ "name": "Drawer", "slug": "drawer" }, { "name": "Window Hanger/Section", "slug" : "window-hanger/section"}]
        
        ExtendedProductTemplate._compute_slug(actual)
        self.assertEqual(actual, expected)

if __name__ == "__main__":
    unittest.main()