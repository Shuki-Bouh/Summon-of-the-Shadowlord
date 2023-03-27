from partie import Partie
import unittest

class TestPartie(unittest.TestCase):

    def test_shape(self):
        map = Partie(10, 10)
        self.assertEqual(map.l, 12)
        self.assertEqual(map.h, 12)
        with self.assertRaises(AttributeError):
            map.h = 11
        with self.assertRaises(AttributeError):
            map.l = 11

if __name__ == '__main__':
    unittest.main()