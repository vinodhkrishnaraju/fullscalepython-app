# project/server/tests/test_main.py


import unittest

from base import BaseTestCase


class TestMainBlueprint(BaseTestCase):

    def test_index(self):
        # Ensure Flask is setup.
        response = self.client.get('/', follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Map', response.data)
        self.assertIn(b'<h2>Bathrooms</h2>', response.data)
        self.assertIn(b'<li\n            data-address="NYC"\n            data-rating="0"\n            data-rating-count="0"\n          >test bathroom</li>', response.data)


if __name__ == '__main__':
    unittest.main()
