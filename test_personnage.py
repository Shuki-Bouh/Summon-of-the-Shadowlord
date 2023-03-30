import personnage as perso
import partie as prt
import unittest


class TestEntite(unittest.TestCase):

    """Ne pas mettre game tout le temps, sinon, il y a conflit entre les tests,
    notamment avec les compteurs_total qui ne renvoient pas la bonne chose..."""

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

    def test_squelette(self):
        game = prt.Partie(10, 10)
        print(game.ennemis)
        Sakdoss_1 = perso.Squelette(game, (5,7), 5)
        print(game.ennemis)
        self.assertEqual(Sakdoss_1.compteur, Sakdoss_1.total_compteur)
        Sakdoss_2 = perso.Squelette(game, (4,8), 5)
        print(game.ennemis)
        self.assertEqual(Sakdoss_1.compteur,Sakdoss_2.compteur)
        self.assertEqual(Sakdoss_2.total_compteur, 2)
        Sakdoss_1.mort()
        self.assertEqual(Sakdoss_2.total_compteur, 2)
        self.assertEqual(Sakdoss_2.compteur, 1)


    def test_attaque(self):
        game = prt.Partie(10, 10)
        Link = perso.Epeiste(game, (5,5), 'Link', niveau=5)
        Sakdoss = perso.Squelette(game, (5,5), niveau=10)
        print(game.ennemis)
        self.assertEqual(Link.vie, 35)
        self.assertEqual(Sakdoss.vie, 100)
        Link.coup(Link, Sakdoss)
        Sakdoss.coup(Sakdoss, Link)
        self.assertEqual(Sakdoss.vie, 84)
        self.assertEqual(Link.vie, 19)

if __name__ == '__main__':
    unittest.main()