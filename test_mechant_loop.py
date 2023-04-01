from Code.partie import Partie
import unittest

class TestPartie(unittest.TestCase):

    def test_loop_mechant(self):
         game = Partie(10,10)
         game.new_player('Link', 'epeiste')
         game.action_mechant()


if __name__ == '__main__':
    unittest.main()