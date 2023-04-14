from Code.partie import Partie
import Code.personnage as p
import unittest
import os

path = os.getcwd()
if "\\" in path:
    path = path.split("\\Test_unitaires")[0]
else:
    path = path.split("/Test_unitaires")
os.chdir(os.path.join(path, "Data"))

class TestPartie(unittest.TestCase):

    def test_shape(self):
        game1 = Partie(10, 10)
        self.assertEqual(game1.l, 12)
        self.assertEqual(game1.h, 12)

    def test_new_player(self):
        game2 = Partie(10, 10)
        classes = {'epeiste': p.Epeiste,
                   'garde': p.Garde,
                   'sorcier': p.Sorcier,
                   'archer': p.Archer}
        i = 0
        for c in classes.keys():
            game2.new_player('link', c, 5, (1 + i, 5))
            self.assertIsInstance(game2[1 + i][5], classes[c])
            i += 1
        for joueur in game2.joueurs.values():
            self.assertEqual(joueur.niveau, 5)

    def test_spawn(self):
        game3 = Partie(10, 10)
        i = 0
        ennemi = {'squelette': p.Squelette,
                  'crane': p.Crane,
                  'invocateur': p.Invocateur,
                  'armure': p.Armure}
        for c in ennemi.keys():
            game3.spawn(c, 5, (1+i, 5))
            self.assertIsInstance(game3[1+i][5], ennemi[c])
            i += 1
        for ennemi in game3.ennemis.values():
            self.assertEqual(ennemi.niveau, 5)

    def test_spawn_ennemi(self):
        game4 = Partie(10, 10)
        game4.new_player('link', 'epeiste', 5, (1, 5))
        for k in range(10):
            game4.spawn_ennemi()
        for mechant in game4.ennemis.values():
            self.assertIsInstance(mechant, p.Ennemi)
        # On ne peut pas tester la partie sur la limite spawn :((

    def test_suppr_ennemi(self):
        game5 = Partie(10, 10)
        game5.spawn('squelette', 5)
        game5.spawn('crane', 5)
        game5.spawn('armure', 5)
        game5.spawn('invocateur', 5)
        for mechant in game5.ennemis.values():
            mechant.mort()
        self.assertEqual(len(game5.disparition), 4)
        game5.suppr_ennemi()
        self.assertEqual(game5.ennemis, {})
        self.assertEqual(game5.disparition, [])

if __name__ == '__main__':

    unittest.main()