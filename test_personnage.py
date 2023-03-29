import personnage as perso
import partie as prt
import unittest

class TestEpeiste(unittest.TestCase):
    def test_stat_lv5(self):
        game = prt.Partie(10, 10)
        epeiste = perso.Epeiste(game, (5, 5), 'Link', niveau=5)
        self.assertEqual(epeiste.attaque, 27)

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
        with self.assertRaises(AssertionError):
            Link.vie -= Link.viemax

    def test_attaque(self):
        game = prt.Partie(10, 10)
        LeHeroDuTemps = perso.Epeiste(game, (4, 5), 'Link', niveau=5)
        squelette = perso.Squelette(game, (4, 4), niveau=5)
        test = LeHeroDuTemps.attaquer()
        self.assertTrue(test)
        LeHeroDuTemps.orientation = 'left'
        test = LeHeroDuTemps.attaquer()
        self.assertFalse(test)

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