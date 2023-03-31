import Code.personnage as perso
import Code.partie as prt
import unittest
import time


class TestEntite(unittest.TestCase):

    def test_gen_joueur(self):
        t = time.time()
        game = prt.Partie(10, 10)
        game.new_player("Link", "epeiste")
        Link = game.joueurs["Link"]
        self.assertEqual(Link.attaque, 7)
        t1 = time.time()

    def test_pointeur(self):
        game = prt.Partie(10, 10)
        Link = perso.Epeiste(game, (5, 5), 'Link', niveau=5)
        Saria = perso.Epeiste(game, (5, 6), 'Saria', niveau=5)
        self.assertEqual(Link.game, game)
        self.assertEqual(Link.game, Saria.game)
        self.assertEqual(Saria.game[5][5], Link)
        self.assertEqual(Link.game[5][6], Saria)
        Saria.deplacement('up')
        self.assertEqual(Link.game[5][6], Saria)
        Saria.deplacement('down')
        self.assertEqual(Saria.game[5][7], Saria)

    def test_set_vie(self):
        game = prt.Partie(10, 10)
        Link = perso.Epeiste(game, (5, 5), 'Link', niveau=5)
        Link.vie += 5
        self.assertEqual(Link.vie, Link.viemax)

    def test_squelette(self):
        game = prt.Partie(10, 10)
        Link = perso.Epeiste(game, (4, 9), 'Link', niveau=5)
        Saria = perso.Epeiste(game, (8, 2), 'Saria', niveau=5)
        Sakdoss_1 = perso.Squelette(game, (5, 6), niveau=5)
        Sakdoss_2 = perso.Squelette(game, (4, 8), niveau=10)
        Sakdoss_3 = perso.Squelette(game, (8, 3), niveau=10)
        # Test compteur et mort -----------------------------------
        compteur = Sakdoss_2.compteur
        self.assertEqual(Sakdoss_1.compteur, Sakdoss_2.compteur)
        Sakdoss_1.mort()
        x, y = Sakdoss_1.position
        self.assertEqual(game[x][y], None)
        self.assertEqual(Sakdoss_2.compteur, compteur-1)
        # Test attaque --------------------------------------------
        Link.attaquer()
        Sakdoss_2.attaquer()
        self.assertEqual(Link.vie, 19)
        self.assertEqual(Sakdoss_2.vie, 84)
        # Test attaque spéciale -----------------------------------
        Sakdoss_3.attaque_speciale()
        self.assertEqual(Saria.vie, 3)
        # Test déplacement ----------------------------------------
        Sakdoss_2.deplacement()
        self.assertNotEqual(Sakdoss_2.position, (4, 8))


    def test_crane(self):
        game = prt.Partie(10,10)
        Tetdoss_1 = perso.Squelette(game, (5, 7), 5)
        Tetdoss_2 = perso.Squelette(game, (4, 8), 5)
        self.assertEqual(Tetdoss_1.compteur, Tetdoss_2.compteur)
        Tetdoss_1.mort()
        Tetdoss_2.deplacement()
        x, y = Tetdoss_1.position
        self.assertEqual(game[x][y], None)
        self.assertNotEqual(Tetdoss_2.position, (4, 8))
        """A implémenter !"""



if __name__ == '__main__':
    unittest.main()
