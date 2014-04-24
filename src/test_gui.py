import unittest
import game
from gui import GUI
import io

class TestGui(unittest.TestCase):
        
    def setUp(self):
        self.game = game.Game()
        
    def testDimensions(self):

        self.game.play_game(GUI(self.game, io.StringIO("1\n10\n7\nq\n3\n")))
        
        self.assertEquals(self.game.labyrinth.width, 10)
        self.assertEquals(self.game.labyrinth.height, 7)
        
    def testTooSmallDimensions(self):
        #try to set 3x3 it should fail
        #set 4x4
        self.game.play_game(GUI(self.game, io.StringIO("1\n3\n4\n3\n4\nq\n3\n")))
        #verify
        self.assertEquals(self.game.labyrinth.width, 4)
        self.assertEquals(self.game.labyrinth.height, 4)
        
    def testMoving(self):
        #create 5x5 labyrinth and move in all directions. The player should not be in the middle
        self.game.play_game(GUI(self.game, io.StringIO("1\n11\n11\nw\na\ns\nd\nq\n3\n")))
        #verify
        self.assertNotEquals(self.game.player.getCurrentNode(), self.game.labyrinth.getStartNode())