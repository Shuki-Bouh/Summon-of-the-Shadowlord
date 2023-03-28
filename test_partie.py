from partie import Partie
from personnage import Epeiste
import unittest

class TestPartie(unittest.TestCase):

    def test_shape(self):
        map = Partie(10, 10)
        self.assertEqual(map.l, 12)
        self.assertEqual(map.h, 12)

if __name__ == '__main__':
    unittest.main()