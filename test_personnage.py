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
        perso.Ennemi.compteur = 0
        del game

    def test_deplacement(self):
        game = prt.Partie(10, 10)
        Link = perso.Epeiste(game, (5, 5), 'Link', niveau=5)
        Saria = perso.Epeiste(game, (5, 6), 'Saria', niveau=5)
        self.assertEqual(Saria.game[5][5], Link)
        self.assertEqual(Link.game[5][6], Saria)
        Saria.deplacement('up')
        self.assertEqual(Link.game[5][6], Saria)
        Saria.deplacement('down')
        self.assertEqual(Saria.game[5][7], Saria)
        perso.Ennemi.compteur = 0
        del game

    def test_set_vie(self):
        game = prt.Partie(10, 10)
        Link = perso.Epeiste(game, (5, 5), 'Link', niveau=5)
        Link.vie += 5
        self.assertEqual(Link.vie, Link.viemax)
         # reste à implémenter les tests pour la mort
        perso.Ennemi.compteur = 0
        del game

    def test_squelette(self):
        game = prt.Partie(10, 10)
        Link = perso.Epeiste(game, (4, 9), 'Link', niveau=5)
        Zelda = perso.Epeiste(game, (8, 2), 'Zelda', niveau=5)
        Sakdoss_1 = perso.Squelette(game, (5, 6), niveau=5)
        Sakdoss_2 = perso.Squelette(game, (4, 8), niveau=10)
        Sakdoss_3 = perso.Squelette(game, (8, 3), niveau=10)
        # Test compteur et mort -----------------------------------
        self.assertEqual(Sakdoss_1.compteur, Sakdoss_2.compteur)
        Sakdoss_1.mort()
        x, y = Sakdoss_1.position
        self.assertEqual(game[x][y], None)
        self.assertEqual(Sakdoss_2.compteur, 2)
        # Test attaque --------------------------------------------
        Link.attaquer()
        Sakdoss_2.agro()
        Sakdoss_2.attaquer()
        self.assertEqual(Link.vie, 19)
        self.assertEqual(Sakdoss_2.vie, 84)
        # Test attaque spéciale -----------------------------------
        Sakdoss_3.agro()
        Sakdoss_3.attaque_speciale()
        self.assertEqual(Zelda.vie, 3)
        # Test déplacement ----------------------------------------
        Sakdoss_2.position = (4, 7)
        Sakdoss_2.deplacement()
        self.assertEqual(Sakdoss_2.position, (4, 8))
        # Suppression de la partie locale -------------------------
        perso.Ennemi.compteur = 0
        del game

    def test_crane(self):
        game = prt.Partie(10, 10)
        Darunia = perso.Garde(game, (4, 9), 'Darunia', niveau=5)
        Impa = perso.Garde(game, (8, 4), 'Impa', niveau=5)
        Tetdoss_1 = perso.Crane(game, (5, 6), niveau=5)
        Tetdoss_2 = perso.Crane(game, (4, 8), niveau=10)
        Tetdoss_3 = perso.Crane(game, (8, 5), niveau=10)
        # Test compteur et mort -----------------------------------
        self.assertEqual(Tetdoss_1.compteur, Tetdoss_1.compteur)
        Tetdoss_1.mort()
        x, y = Tetdoss_1.position
        self.assertEqual(game[x][y], None)
        self.assertEqual(Tetdoss_2.compteur, 2)
        # Test attaque --------------------------------------------
        Darunia.attaquer()
        Tetdoss_2.agro()
        Tetdoss_2.attaquer()
        self.assertEqual(Darunia.vie, 23)
        self.assertEqual(Tetdoss_2.vie, 20)
        # Test attaque spéciale -----------------------------------
        Tetdoss_3.agro()
        Tetdoss_3.vie = 10
        Tetdoss_3.attaque_speciale()
        self.assertEqual(Tetdoss_3.vie, 23)
        self.assertEqual(Impa.vie, 27)
        self.assertEqual(Impa.position, (8, 2))
        # Test déplacement ----------------------------------------
        Tetdoss_2.position = (4, 6)
        Tetdoss_2.deplacement()
        self.assertEqual(Tetdoss_2.position, (4, 8))
        # Suppression de la partie locale -------------------------
        perso.Ennemi.compteur = 0
        del game

    def test_armure(self):
        game = prt.Partie(10, 10)
        Koume = perso.Sorcier(game, (4, 9), 'Koume', niveau=5)
        Kotake = perso.Sorcier(game, (8, 2), 'Kotake', niveau=5)
        Hache_viande_1 = perso.Armure(game, (5, 6), niveau=5)
        Hache_viande_2 = perso.Armure(game, (4, 8), niveau=10)
        Hache_viande_3 = perso.Armure(game, (8, 3), niveau=10)
        # Test compteur et mort -----------------------------------
        self.assertEqual(Hache_viande_1.compteur, Hache_viande_2.compteur)
        Hache_viande_1.mort()
        x, y = Hache_viande_1.position
        self.assertEqual(game[x][y], None)
        self.assertEqual(Hache_viande_2.compteur, 2)
        # Test attaque --------------------------------------------
        Koume.attaquer()
        Hache_viande_2.agro()
        Hache_viande_2.attaquer()
        self.assertEqual(Koume.vie, 0)
        self.assertEqual(Hache_viande_2.vie, 193)
        # Test attaque spéciale -----------------------------------
        Hache_viande_3.agro()
        Hache_viande_3.vie = 30
        Hache_viande_3.attaque_speciale()
        self.assertEqual(Hache_viande_3.vie, 40)
        self.assertEqual(Kotake.vie, 4)
        self.assertEqual(Kotake.position, (8, 1))
        # Test déplacement ----------------------------------------
        Hache_viande_2.position = (6, 9)
        Hache_viande_2.deplacement()
        self.assertEqual(Hache_viande_2.position, (5, 9))
        # Suppression de la partie locale -------------------------
        perso.Ennemi.compteur = 0
        del game

    def test_invocateur(self):
        game = prt.Partie(10, 10)
        Saria = perso.Archer(game, (4, 9), 'Saria', niveau=5)
        Mizumi = perso.Archer(game, (8, 2), 'Mizumi', niveau=5)
        Invocateur_1 = perso.Invocateur(game, (5, 6), niveau=5)
        Invocateur_2 = perso.Invocateur(game, (4, 8), niveau=10)
        Invocateur_3 = perso.Invocateur(game, (8, 3), niveau=10)
        # Test compteur et mort -----------------------------------
        self.assertEqual(Invocateur_1.compteur, Invocateur_2.compteur)
        Invocateur_1.mort()
        x, y = Invocateur_1.position
        self.assertEqual(game[x][y], None)
        self.assertEqual(Invocateur_2.compteur, 2)
        # Test attaque --------------------------------------------
        Saria.attaquer()
        Invocateur_2.agro()
        Invocateur_2.attaquer()
        self.assertEqual(Saria.vie, 22)
        self.assertEqual(Invocateur_2.vie, 54)
        # Test attaque spéciale -----------------------------------
        Invocateur_3.agro()
        Invocateur_3.attaque_speciale()
        # self.assertEqual(perso.Crane.compteur, 2)
        self.assertEqual(Mizumi.vie, 14)
        Invocateur_3.vie = 1
        Mizumi.vie = Mizumi.viemax
        for k in range(3):
            game.spawn_crane(5)
        # self.assertEqual(perso.Crane.compteur, 5)
        Invocateur_3.agro()
        Invocateur_3.attaque_speciale()
        self.assertEqual(Invocateur_3.vie, Invocateur_3.viemax)
        self.assertEqual(Mizumi.vie, 14)
        # Test déplacement ----------------------------------------
        Invocateur_2.position = (6, 9)
        Invocateur_2.deplacement()
        self.assertEqual(Invocateur_2.position, (5, 9))
        # Suppression de la partie locale -------------------------
        perso.Ennemi.compteur = 0
        del game


if __name__ == '__main__':
    unittest.main()
