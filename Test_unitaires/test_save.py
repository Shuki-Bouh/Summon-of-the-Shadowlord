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
        Test = perso.Epeiste(game, (5, 5), 'Test', niveau=5)
        path = game.joueurs['Test']
        for k in range(5):
            game.spawn_ennemi()
        game.create_save()
        game.write_save(Test)
        game.joueurs = {}
        game.open_save('Test')
        self.assertEqual(path.game, game.joueurs['Test'].game)
        self.assertEqual(path.position, game.joueurs['Test'].position)
        self.assertEqual(path.niveau, game.joueurs['Test'].niveau)
        self.assertEqual(path.nom, game.joueurs['Test'].nom)


if __name__ == '__main__':
    unittest.main()