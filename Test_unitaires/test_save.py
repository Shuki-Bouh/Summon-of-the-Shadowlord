import Code.partie as prt
import unittest
import os

path = os.getcwd()
path = path.split("\\Test_unitaires")[0]
os.chdir(os.path.join(path, "Data"))


class TestSave(unittest.TestCase):

    def test_create_and_suppr_bdd(self):
        game = prt.Partie(10, 10)
        game.destroy_dbb("First_try")
        game.create_save("First_try")
        game.create_save("First_try")
        game.destroy_dbb("First_try")
        game.destroy_dbb("First_try")
        os.remove("./_Save/First_try")

    def test_write_save(self):
        game = prt.Partie(10, 10)
        with self.assertRaises(KeyError):
            game.write_save("Link", "terrible.db")
        game.new_player("Link", "epeiste")
        game.spawn('squelette', 5)
        game.write_save("Link", "terrible.db")
        os.remove("./_Save/terrible.db")

    def test_load_save(self):
        game = prt.Partie(10, 10)
        game.new_player("Saria", "sorcier", 5, (4, 6))
        game.write_save("Saria", "encore une bdd.db")
        result = game.lecture_perso("encore une bdd.db")[0]
        self.assertEqual(result, ("Saria", 1, "sorcier", 5, 4, 6, 0, 0, 0))
        os.remove("./_Save/encore une bdd.db")


if __name__ == '__main__':
    unittest.main()
