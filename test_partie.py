from partie import Partie
from personnage import Epeiste
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

    def test_rien_autour_position(self):
        map = Partie(10, 10)
        self.assertTrue(map.rien_autour_position((5, 5), 'up'))
        self.assertTrue(map.rien_autour_position((5, 5), 'down'))
        self.assertTrue(map.rien_autour_position((5, 5), 'left'))
        self.assertTrue(map.rien_autour_position((5, 5), 'right'))
        self.assertFalse(map.rien_autour_position((1, 1), 'up'))
        self.assertFalse(map.rien_autour_position((1, 1), 'left'))
        self.assertFalse(map.rien_autour_position((map.h-1, map.l-1), 'right'))
        self.assertFalse(map.rien_autour_position((map.h-1, map.l-1), 'down'))
        map[5][5] = False
        self.assertFalse(map.rien_autour_position((4, 5), 'right'))
        self.assertFalse(map.rien_autour_position((6, 5), 'left'))
        self.assertFalse(map.rien_autour_position((5, 4), 'down'))
        self.assertFalse(map.rien_autour_position((5, 6), 'up'))


if __name__ == '__main__':
    unittest.main()