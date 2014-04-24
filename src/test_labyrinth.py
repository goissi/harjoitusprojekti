import unittest
import game
import pos
import node
import player
import gui
import labyrinth

class TestLabyrinth(unittest.TestCase):
        
    def setUp(self):
        self.labyrinth = labyrinth.Labyrinth(10,8)
        
    def testInit(self):
        
        self.assertEquals(self.labyrinth.width, 10)
        self.assertEquals(self.labyrinth.height, 8)
        
    def testGenerateAndGetMaze(self):
        
        self.labyrinth.generateMaze()
        self.assertEquals(len(self.labyrinth.getMaze()), 10)