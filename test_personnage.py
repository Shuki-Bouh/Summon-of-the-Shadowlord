import personnage as perso
import partie as prt
import unittest

class TestEpeiste(unittest.TestCase):
    def test_stat_lv5(self):
        game = prt.Partie(10, 10)
        epeiste = perso.Epeiste(game, (5, 5), 5, 'Link', niveau=5)
        self.assertEqual(epeiste.attaque, 27)

    def test_pointeur(self):
        game = prt.Partie(10, 10)
        Link = perso.Epeiste(game, (5, 5), 5, 'Link', niveau=5)
        Saria = perso.Epeiste(game, (5, 6), 5, 'Saria', niveau=5)
        self.assertEqual(Link.game, game)
        self.assertEqual(Link.game, Saria.game)
        self.assertEqual(Saria.game[5][5], Link)
        self.assertEqual(Link.game[6][5], Saria)
        Saria.deplacement('up')
        self.assertEqual(Link.game[6][5], Saria)
        Saria.deplacement('down')
        self.assertEqual(Saria.game[7][5], Saria)

# Il faut creer le doc "Squelette_lvl.txt" ...

    # def test_squelette(self):
    #     game = prt.Partie(10, 10)
    #     Sakdoss_1 = perso.Squelette(game, (5,7), 5)
    #     self.assertEqual(Sakdoss_1.compteur, Sakdoss_1.total_compteur)
    #     Sakdoss_2 = perso.Squelette(game, (4,8), 5)
    #     self.assertEqual(Sakdoss_1.compteur,Sakdoss_2.compteur)
    #     self.assertEqual(Sakdoss_2.total_compteur, 2)
    #     Sakdoss_1.mort()
    #     self.assertEqual(Sakdoss_2.total_compteur, 2)
    #     self.assertEqual(Sakdoss_2.compteur, 1)
    #     self.assertNotIsInstance(Sakdoss_1, perso.Entite)

    # def test_attaque(self):
    #     game = prt.Partie(10, 10)
    #     Link = perso.Epeiste(game, (5, 5), 5, 'Link', niveau=5)
    #     Sakdoss_1 = perso.Squelette(game, (6, 4), 5)
    #     Sakdoss_2 = perso.Squelette(game, (6, 5), 5)
    #     Sakdoss_3 = perso.Squelette(game, (6, 6), 5)
    #     # Test d'attaque...


if __name__ == '__main__':
    unittest.main()