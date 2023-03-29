from partie import Partie
from personnage import Epeiste
import personnage as p
import unittest

class TestPartie(unittest.TestCase):

    def test_shape(self):
        map = Partie(10, 10)
        self.assertEqual(map.l, 12)
        self.assertEqual(map.h, 12)

    def test_spawn_squelette(self):
        game = Partie(10, 10)
        for k in range(20):
            game.spawn_ennemi(5)
        self.assertEqual(game.ennemis['Squelette 5'].vie, 31)
        game.ennemis["Squelette 4"].mort()
        self.assertEqual(p.Ennemi.compteur, p.Squelette.compteur)
        self.assertTrue(p.Ennemi.compteur <= 15)

if __name__ == '__main__':
    unittest.main()