from gui import GUI
from labyrinth import Labyrinth
from player import Player
from pos import Pos
from node import Node


class Game(object):
    
    UP = 0
    DOWN = 1
    RIGHT = 2
    LEFT = 3
    
    gui = False
    
    def move(self, direction):
        self.player.move(direction)
    
    def save_game(self):
        #create file
        f = open('saved_games.dat', 'w+')
        
        
        f.write("W:"+str(self.labyrinth.width)+'\n')
        f.write("H:"+str(self.labyrinth.height)+'\n')
        
        for node in self.labyrinth.nodes:
            f.write(node.info())  # print(node.info(), file=f)
        
        f.write("Player position:"+str(self.player.getCurrentNode().getId())+'\n') # print("player position:"+str(self.player.getCurrentNode().getId()), file=f)
        f.write("End node:"+str(self.labyrinth.getEndNode().getId())+'\n')
            
        f.close()
        
        print("Saved!")
        
    
    def load_game(self):
        #file handle
        f = open('saved_games.dat', 'r');
        fileContent = f.read()
        f.close()
        
        w = 0

        #create labyrinth and nodes
        for line in fileContent.split('\n'):
            lineAr = line.split(':')
            if (len(lineAr) == 2):
                key = lineAr[0].strip()
                value = lineAr[1].strip()
                
                if (key == 'W'):
                    w = int(value)
                if (key == 'H'):
                    #create labyrinth
                    self.labyrinth = Labyrinth(w, int(value))
                
                if (key == 'Id'):
                    self.labyrinth.addNode(Node(Pos()))
                    self.labyrinth.getLastNode().setId(int(value))
                    
                if (key == 'X'):
                    self.labyrinth.getLastNode().setX(int(value))
                if (key == 'Y'):
                    self.labyrinth.getLastNode().setY(int(value))
                if (key == 'Z'):
                    self.labyrinth.getLastNode().setZ(int(value))

        #set connections
        id = 0
        for line in fileContent.split('\n'):
            lineAr = line.split(':')
            if (len(lineAr) == 2):
                key = lineAr[0].strip()
                value = lineAr[1].strip()
                
                if (key == 'Id'):
                    id = int(value)
                if (key == 'ConnectionRIGHT'):
                    self.labyrinth.findNodeById(int(value)).setConnection(self.RIGHT, self.labyrinth.findNodeById(id))
                if (key == 'ConnectionLEFT'):
                    self.labyrinth.findNodeById(int(value)).setConnection(self.LEFT, self.labyrinth.findNodeById(id))
                if (key == 'ConnectionUP'):
                    self.labyrinth.findNodeById(int(value)).setConnection(self.UP, self.labyrinth.findNodeById(id))
                if (key == 'ConnectionDOWN'):
                    self.labyrinth.findNodeById(int(value)).setConnection(self.DOWN, self.labyrinth.findNodeById(id))
                if (key == 'Player position'):
                    playerNode = self.labyrinth.findNodeById(int(value))
                    playerNode.setPlayer(True)
                    self.player = Player(playerNode)
                if (key == 'End node'):
                    self.labyrinth.endNode = self.labyrinth.findNodeById(int(value))
                    
    
    def play_game(self):
        while(True):
            self.gui = GUI(self)
            
            menu_sel = self.gui.print_menu()
            
            if(menu_sel == 1):
                #start new game
                #set labyrinth size:
                width = self.gui.ask_width()
                height = self.gui.ask_height()
                
                #create labyrinth
                self.labyrinth = Labyrinth(width, height)
                self.labyrinth.generateMaze()
                
                #createa player
                self.player = Player(self.labyrinth.getStartNode())                

                #the game itself
                
                self.gui.game_loop()
                
                
            if(menu_sel == 2):
                #Load game from a file
                self.load_game()
                self.gui.game_loop()
                
            if(menu_sel == 3):
                #Exit game
                return self.end_game()
        
    def hasWon(self):
        return self.player.getCurrentNode() == self.labyrinth.getEndNode()
        
    
    def end_game(self):
        print("Ending game.")
        return 0
    

