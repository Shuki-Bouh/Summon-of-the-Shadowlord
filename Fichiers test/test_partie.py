import Code.personnage
from Code.partie import Partie
import Code.personnage as p
import unittest

class TestPartie(unittest.TestCase):

    def test_shape(self):
        game = Partie(10, 10)
        self.assertEqual(game.l, 12)
        self.assertEqual(game.h, 12)

    def test_spawn_squelette(self):
        game = Partie(10, 10)
        for k in range(20):
            game.spawn_squelette(5)
        self.assertEqual(game.ennemis['Squelette 5'].vie, 50)
        game.ennemis["Squelette 4"].mort()
        with self.assertRaises(KeyError):
            a = game.ennemis["Squelette 4"]
        p.Ennemi.compteur = 0
        del game

    def test_mort(self):
        game = Partie(10,10)
        game.spawn_squelette(5)
        s = game.ennemis["Squelette 1"]
        s.vie += 5
        self.assertEqual(s.vie, 50)
        game.ennemis["Squelette 1"].vie -= 55
        with self.assertRaises(KeyError):
            a = game.ennemis["Squelette 1"]  # Ici on vérifie le setter de vie, il est bien mort
        p.Ennemi.compteur = 0
        del game
    def test_spawn_ennemis(self):
        game = Partie(10, 10)
        for k in range(10):
            s = game.spawn_ennemi(5)
        self.assertEqual(p.Ennemi.compteur, 5)
        p.Ennemi.compteur = 0
        del game

    def test_loop_mechant(self):
         game = Partie(10,10)
         game.new_player('Link', 'epeiste')
         game.action_mechant()
         del game

if __name__ == '__main__':
    unittest.main()