import unittest
import game
from gui import GUI
import io

class TestGame(unittest.TestCase):
        
    def setUp(self):
        self.game = game.Game()
        
    def testPlayGame(self):

        self.game.play_game(GUI(self.game, io.StringIO("1\n10\n7\nq\n3\n")))
        
        self.assertEquals(self.game.labyrinth.width, 10)
        self.assertEquals(self.game.player.getX(), 5)
        
    def testSaveAndLoadGame(self):

        self.game.play_game(GUI(self.game, io.StringIO("1\n5\n4\ng\nq\n2\nq\n3\n")))
        
        self.assertEquals(self.game.labyrinth.width, 5)
        self.assertEquals(self.game.labyrinth.height, 4)
        