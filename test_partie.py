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

    def test_spawn_crane(self):
        game = Partie(10, 10)
        for k in range(20):
            game.spawn_crane(5)
        self.assertEqual(game.ennemis['Crane 5'].vie, 19)
        game.ennemis["Crane 4"].mort()
        with self.assertRaises(KeyError):
            a = game.ennemis["Crane 4"]
        p.Ennemi.compteur = 0
        del game

    def test_spawn_armure(self):
        game = Partie(10, 10)
        for k in range(20):
            game.spawn_armure(5)
        self.assertEqual(game.ennemis['Armure 5'].vie, 115)
        game.ennemis["Armure 4"].mort()
        with self.assertRaises(KeyError):
            a = game.ennemis["Armure 4"]
        p.Ennemi.compteur = 0
        del game

    def test_spawn_invocateur(self):
        game = Partie(10, 10)
        for k in range(20):
            game.spawn_invocateur(5)
        self.assertEqual(game.ennemis['Invocateur 5'].vie, 45)
        game.ennemis["Invocateur 4"].mort()
        with self.assertRaises(KeyError):
            a = game.ennemis["Invocateur 4"]
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


if __name__ == '__main__':
    unittest.main()