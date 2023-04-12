import Code.personnage as perso
import Code.partie as prt
import unittest
import time
import os

path = os.getcwd()
path = path.split("\\Test_unitaires")[0]
os.chdir(os.path.join(path, "Data"))

class TestEntite(unittest.TestCase):

    def test_deplacement(self):
        game1 = prt.Partie(10, 10)
        link = perso.Epeiste(game1, (5, 5), 'Link', niveau=5)
        saria = perso.Sorcier(game1, (5, 6), 'Saria', niveau=5)
        self.assertEqual(game1[5][5], link)
        self.assertEqual(game1[5][6], saria)
        saria.deplacement('up')
        self.assertEqual(game1[5][6], saria)
        saria.deplacement('down')
        self.assertEqual(saria.game[5][7], saria)
        saria.deplacement('left')
        self.assertEqual(saria.game[4][7], saria)
        saria.deplacement('right')
        self.assertEqual(saria.game[5][7], saria)

    def test_set_vie(self):
        game2 = prt.Partie(10, 10)
        link = perso.Garde(game2, (5, 5), 'Link', niveau=5)
        link.vie += 5
        self.assertEqual(link.vie, link.viemax)
        self.assertTrue(link.vivant)
        link.vie -= 150
        self.assertEqual(link.vie, 0)
        self.assertFalse(link.vivant)

    def test_level_up(self):
        game3 = prt.Partie(10, 10)
        link = perso.Archer(game3, (5, 5), 'Link', niveau=5)
        link.xp += 50
        link._levelup()
        self.assertEqual(link.xp, 0)
        self.assertEqual(link.niveau, 6)

    def test_coup(self):
        game4 = prt.Partie(10,10)
        classe = [perso.Archer, perso.Garde, perso.Epeiste, perso.Sorcier]
        link = perso.Garde(game4, (5, 5), 'Link', niveau=8)
        ennemi = perso.Squelette(game4, (6, 6), 9)
        vieEInit = ennemi.vie

        link.coup(link, ennemi)
        vieEEnd = ennemi.vie
        self.assertNotEqual(vieEInit, vieEEnd)
        vieLInit = link.vie
        ennemi.coup(ennemi, link)
        vieLEnd = link.vie
        self.assertNotEqual(vieLInit, vieLEnd)

    def test_attaque_perso(self):
        game5 = prt.Partie(10, 10)
        link = perso.Epeiste(game5, (5,5), 'link', niveau=5)
        ennemiHaut = perso.Squelette(game5, (5,4), 5)
        ennemiTresHaut = perso.Squelette(game5, (5, 3), 5)
        ennemiDiag = perso.Squelette(game5, (6, 6), 5)
        ennemiCote = perso.Squelette(game5, (4, 5), 5)
        v1, v2, v3, v4 = ennemiHaut.vie, ennemiTresHaut.vie, ennemiDiag.vie, ennemiCote.vie
        self.assertEqual(link.orientation, "up")
        link.attaquer()
        self.assertNotEqual(v1, ennemiHaut.vie)
        self.assertEqual(v2, ennemiTresHaut.vie)
        self.assertEqual(v2, ennemiDiag.vie)
        self.assertEqual(v2, ennemiCote.vie)

    def test_attaque_Special_Epeiste(self):
        game6 = prt.Partie(10, 10)
        link = perso.Epeiste(game6, (5, 5), 'link', niveau=5)
        e1 = perso.Armure(game6, (5, 4), 5)
        e2 = perso.Armure(game6, (4, 4), 5)
        e3 = perso.Armure(game6, (6, 4), 5)
        mana = link.mana
        v1, v2, v3 = e1.vie, e2.vie, e3.vie
        link.attaque_speciale()
        self.assertNotEqual(mana, link.mana)
        self.assertNotEqual(v1, e1.vie)
        self.assertNotEqual(v2, e2.vie)
        self.assertNotEqual(v3, e3.vie)
        link.orientation = 'right'
        mana = link.mana
        v1, v2, v3 = e1.vie, e2.vie, e3.vie
        link.attaque_speciale()
        self.assertEqual(v1, e1.vie)
        self.assertEqual(v2, e2.vie)
        self.assertNotEqual(v3, e3.vie)

    def attaque_speciale_garde(self):
        game7 = prt.Partie(10, 10)
        link = perso.Garde(game7, (5, 5), 'link', niveau=5)
        e1 = perso.Armure(game7, (5, 4), 5)
        e2 = perso.Armure(game7, (5, 3), 5)
        e3 = perso.Armure(game7, (6, 4), 5)
        e4 = perso.Armure(game7, (6, 5), 5)
        e5 = perso.Armure(game7, (7, 5), 5)
        mana = link.mana
        v1, v2, v3, v4, v5 = e1.vie, e2.vie, e3.vie, e4.vie, e5.vie
        link.attaque_speciale()
        self.assertNotEqual(mana, link.mana)
        self.assertNotEqual(v1, e1.vie)
        self.assertNotEqual(v2, e2.vie)
        self.assertEqual(v3, e3.vie)
        self.assertEqual(v4, e4.vie)
        self.assertEqual(v5, e5.vie)
        link.orientation = 'right'
        mana = link.mana
        v1, v2, v3, v4, v5 = e1.vie, e2.vie, e3.vie, e4.vie, e5.vie
        link.attaque_speciale()
        self.assertNotEqual(mana, link.mana)
        self.assertEqual(v1, e1.vie)
        self.assertEqual(v2, e2.vie)
        self.assertEqual(v3, e3.vie)
        self.assertNotEqual(v4, e4.vie)
        self.assertNotEqual(v5, e5.vie)

    def attaque_speciale_sorcier(self):
        game8 = prt.Partie(10, 10)
        link = perso.Sorcier(game8, (5, 5), 'link', niveau=5)
        e1 = perso.Armure(game8, (5, 4), 5)
        e2 = perso.Armure(game8, (5, 3), 5)
        e3 = perso.Armure(game8, (5, 6), 5)
        e4 = perso.Armure(game8, (5, 7), 5)
        e5 = perso.Armure(game8, (6, 5), 5)
        e6 = perso.Armure(game8, (7, 5), 5)
        e7 = perso.Armure(game8, (4, 5), 5)
        e8 = perso.Armure(game8, (3, 5), 5)
        e9 = perso.Armure(game8, (6, 4), 5)

        mana = link.mana
        v1, v2, v3, v4, v5, v6, v7, v8, v9 = e1.vie, e2.vie, e3.vie, e4.vie, e5.vie, e6.vie, e7.vie, e8.vie, e9.vie
        link.attaque_speciale()
        self.assertNotEqual(mana, link.mana)
        self.assertNotEqual(v1, e1.vie)
        self.assertEqual(v1, e1.vie)
        self.assertNotEqual(v2, e2.vie)
        self.assertNotEqual(v3, e3.vie)
        self.assertNotEqual(v4, e4.vie)
        self.assertNotEqual(v5, e5.vie)
        self.assertNotEqual(v6, e6.vie)
        self.assertNotEqual(v7, e7.vie)
        self.assertNotEqual(v8, e8.vie)
        self.assertEqual(v9, e9.vie)
        self.assertTrue(False)

    """   def test_squelette(self):
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
        Zelda = perso.Archer(game, (8, 2), 'Zelda', niveau=5)
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
        self.assertEqual(Zelda.vie, 14)
        Invocateur_3.vie = 1
        Zelda.vie = Zelda.viemax
        for k in range(3):
            game.spawn_crane(5)
        # self.assertEqual(perso.Crane.compteur, 5)
        Invocateur_3.agro()
        Invocateur_3.attaque_speciale()
        self.assertEqual(Invocateur_3.vie, Invocateur_3.viemax)
        self.assertEqual(Zelda.vie, 14)
        # Test déplacement ----------------------------------------
        Invocateur_2.position = (6, 9)
        Invocateur_2.deplacement()
        self.assertEqual(Invocateur_2.position, (5, 9))
        # Suppression de la partie locale -------------------------
        perso.Ennemi.compteur = 0
        del game"""


if __name__ == '__main__':

    unittest.main()
