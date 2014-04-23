from gui import GUI
from labyrinth import Labyrinth
from player import Player



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
        
        
        f.write("player position:"+str(self.player.getCurrentNode().getId())+'\n') # print("player position:"+str(self.player.getCurrentNode().getId()), file=f)
        #print() labyrinth size
        for node in self.labyrinth.nodes:
            f.write(node.info())  # print(node.info(), file=f)
            
        f.close()
        
    
    def play_game(self):
        while(True):
            self.gui = GUI(self)
            
            menu_sel = self.gui.print_menu()
            
            #debug
            print("MENU SEL:", menu_sel)
            if(menu_sel == 1):
                #start new game
                #set labyrinth size:
                height = 0
                width = 0
                width = self.gui.ask_width()
                height = self.gui.ask_height()
                
                #create labyrinth
                self.labyrinth = Labyrinth(width, height)
                
                #createa player
                self.player = Player(self.labyrinth.getStartNode())                

                #the game itself
                
                self.gui.game_loop()
                
                
            if(menu_sel == 2):
                #Load game from a file
                print("b")
            if(menu_sel == 3):
                #Exit game
                return self.end_game()
        
    def hasWon(self):
        return self.player.getCurrentNode() == self.labyrinth.getEndNode()
        
    
    def end_game(self):
        print("Ending game.")
        return 0
    

