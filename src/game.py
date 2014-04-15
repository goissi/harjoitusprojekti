from gui import GUI
from labyrinth import Labyrinth

class Game(object):
    
    UP = 0
    DOWN = 1
    RIGHT = 2
    LEFT = 3
    
    gui = False
    
    def move(self, direction):
        return True
    
    def save_game(self):
        return True
    
    def play_game(self):
        while(True):
            self.gui = GUI(self)
            
            menu_sel = self.gui.print_menu()
            if(menu_sel == 1):
                #start new game
                """while(True):
                    options = self.gui.print_options()
                    if(options == "w"):
                        move(UP)
                    if(options == "s"):
                        move(DOWN)
                    if(options == "a"):
                        move(LEFT)
                    if(options == "d"):
                        move(RIGHT)
                    if(options == "q"):
                        break   
                    if(options == "l"):
                        self.save_game()"""
                labyrinth = Labyrinth(20,20)
                self.gui.print_game(labyrinth.getMaze())
                
                
            if(menu_sel == 2):
                #Load game from a file
                print("b")
            if(menu_sel == 3):
                #Exit game
                return self.end_game()
        
                
    def end_game(self):
        print("Ending game.")
        return 0
    

