import Code.partie as prt
import Code.personnage as perso
import unittest
import os

path = os.getcwd()
path = path.split("\\Test_unitaires")[0]
os.chdir(os.path.join(path, "Data"))


class TestSave(unittest.TestCase):

    def test_save(self):
        game = prt.Partie(10, 10)
        Test_Save3 = perso.Sorcier(game, (5, 5), 'Test_Save3', niveau=5)
        Test_Save4 = perso.Archer(game, (5, 5), 'Test_Save4', niveau=5)
        path = game.joueurs['Test_Save4']
        for k in range(5):
            game.spawn_ennemi()
        game.create_save()
        game.write_save('Test_Save3')
        game.write_save('Test_Save4')
        game.joueurs = {}
        list_perso = game.lecture_perso()
        personnage = list([liste for liste in list_perso if liste[0] == 'Test_Save4'])[0]
        game.new_player(personnage[0], personnage[2], personnage[3], (personnage[4], personnage[5]))
        self.assertEqual(path.game, game.joueurs['Test_Save4'].game)
        self.assertEqual(path.position, game.joueurs['Test_Save4'].position)
        self.assertEqual(path.niveau, game.joueurs['Test_Save4'].niveau)
        self.assertEqual(path.nom, game.joueurs['Test_Save4'].nom)
        print(list_perso)


if __name__ == '__main__':
    unittest.main()
