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


if __name__ == '__main__':
    unittest.main()