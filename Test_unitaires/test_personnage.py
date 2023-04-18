import Code.personnage as perso
import Code.partie as prt
import unittest
import time
import os

path = os.getcwd()
if "\\" in path:
    path = path.split("\\Test_unitaires")[0]
else:
    path = path.split("/Test_unitaires")
os.chdir(os.path.join(path, "Data"))

class TestEntite(unittest.TestCase):

    def test_deplacement_joueur(self):
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
        self.assertEqual(link.vie, link.vieMax)
        self.assertTrue(link.vivant)
        link.vie -= 150
        self.assertEqual(link.vie, 0)
        self.assertFalse(link.vivant)

    def test_level_up(self):
        game3 = prt.Partie(10, 10)
        link = perso.Archer(game3, (5, 5), 'Link', niveau=5)
        link.xp += 50
        link._level_up()
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

    def test_attaque_speciale_garde(self):
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

    def test_attaque_speciale_sorcier(self):
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
        self.assertNotEqual(v2, e2.vie)
        self.assertNotEqual(v3, e3.vie)
        self.assertNotEqual(v4, e4.vie)
        self.assertNotEqual(v5, e5.vie)
        self.assertNotEqual(v6, e6.vie)
        self.assertNotEqual(v7, e7.vie)
        self.assertNotEqual(v8, e8.vie)
        self.assertEqual(v9, e9.vie)

    def test_attaque_speciale_archer(self):
        game9 = prt.Partie(10, 10)
        link = perso.Archer(game9, (5, 5), 'link', niveau=20)
        e1 = perso.Armure(game9, (5, 4), 5)
        e2 = perso.Armure(game9, (4, 4), 5)
        e3 = perso.Armure(game9, (6, 4), 5)
        e4 = perso.Armure(game9, (4, 5), 5)
        e5 = perso.Armure(game9, (6, 5), 5)
        e6 = perso.Armure(game9, (4, 6), 5)
        e7 = perso.Armure(game9, (5, 6), 5)
        e8 = perso.Armure(game9, (6, 6), 5)

        mana = link.mana
        v1, v2, v3, v4, v5, v6, v7, v8 = e1.vie, e2.vie, e3.vie, e4.vie, e5.vie, e6.vie, e7.vie, e8.vie
        link.attaque_speciale()
        self.assertNotEqual(mana, link.mana)
        self.assertNotEqual(v1, e1.vie)
        self.assertNotEqual(v2, e2.vie)
        self.assertNotEqual(v3, e3.vie)
        self.assertNotEqual(v4, e4.vie)
        self.assertNotEqual(v5, e5.vie)
        self.assertNotEqual(v6, e6.vie)
        self.assertNotEqual(v7, e7.vie)
        self.assertNotEqual(v8, e8.vie)

    def test_attaque_ennemi(self):
        game10 = prt.Partie(10, 10)
        e = perso.Crane(game10, (5, 5), 10)
        link = perso.Archer(game10, (5, 5), 'link', niveau= 10)
        e.cible = link
        e.attaquer()

    def test_deplacement_ennemi(self):
        game11 = prt.Partie(10, 10)
        e = perso.Armure(game11, (5, 5), 10)
        link = perso.Garde(game11, (5, 8), 'link', 10)
        e.cible = link
        e.deplacement()
        self.assertEqual(e.position, (5, 6))

    def test_portee(self):
        game12 = prt.Partie(10, 10)
        e1 = perso.Squelette(game12, (5, 5), 10)
        link = perso.Sorcier(game12, (6, 5), 'link', 10)
        self.assertFalse(e1.portee())
        e1.cible = link
        self.assertTrue(e1.portee())
        link.position = (6, 6)
        self.assertFalse(e1.portee())

    def test_agro(self):
        game13 = prt.Partie(10, 10)
        e = perso.Invocateur(game13, (5, 1), 10)
        e.agro()
        self.assertIs(e.cible, None)
        link = perso.Archer(game13, (5, 8), 'link', niveau=10)
        e.agro()
        self.assertIs(e.cible, None)
        link.position = (5, 6)
        e.agro()
        self.assertIs(e.cible, None)
        link.position = (5, 5)
        e.agro()
        self.assertIs(e.cible, link)

    def test_mort_ennemi(self):
        game14 = prt.Partie(10, 10)
        e = perso.Squelette(game14, (5, 5), 1)
        self.assertIs(game14[5][5], e)
        e.mort()
        self.assertIs(game14[5][5], None)
        self.assertIs(game14.disparition[0], e)

    def test_attaque_speciale_squelette(self):
        game15 = prt.Partie(10, 10)
        e = perso.Squelette(game15, (5, 5), 1)
        link = perso.Archer(game15, (5, 8), 'link', niveau=10)
        e.cible = link
        v = link.vie
        e.attaque_speciale()
        self.assertNotEqual(v, link.vie)

    def test_attaque_speciale_crane(self):
        game16 = prt.Partie(10, 10)
        e = perso.Crane(game16, (5, 5), 10)
        link = perso.Archer(game16, (5, 8), 'link', niveau=10)
        res = link.vie // 3
        e.vie -= res
        e.cible = link
        v = link.vie
        e.attaque_speciale()
        self.assertEqual(v - res, link.vie)
        self.assertEqual(e.vie, e.vieMax)

    def test_attaque_speciale_armure(self):
        game17 = prt.Partie(10, 10)
        e = perso.Armure(game17, (5, 5), 10)
        link = perso.Archer(game17, (5, 8), 'link', niveau=10)
        e.cible = link
        v = link.vie
        pos = link.position
        e.attaque_speciale()
        self.assertNotEqual(v, link.vie)
        self.assertNotEqual((5, 7), link.position)

    def test_attaque_speciale_invocateur(self):
        game18 = prt.Partie(10, 10)
        e = perso.Invocateur(game18, (5, 5), 10)
        link = perso.Archer(game18, (5, 8), 'link', niveau=10)
        e.cible = link
        e.attaque_speciale()
        self.assertIsInstance(game18[5][4], perso.Crane)
        self.assertIsInstance(game18[5][6], perso.Crane)
        link.deplacement("left")
        e.attaque_speciale()
        self.assertIsInstance(game18[4][5], perso.Crane)
        self.assertIsInstance(game18[6][5], perso.Crane)

    def test_niveau(self):
        game19 = prt.Partie(10, 10)
        for k in range(25):
            # On teste qu'on arrive bien à instancier les joueurs/ennemis à chaque niveau
            joueur = perso.Epeiste(game19, (5, 5), 'link', niveau=k)
            ennemi = perso.Squelette(game19, (5, 5), k)

if __name__ == '__main__':

    unittest.main()
