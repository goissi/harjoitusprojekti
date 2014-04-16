from labyrinth import Labyrinth
#from game import Game
import sys
import os

class GUI(object):
    def __init__(self, game):
        self.game = game
        self.clear = lambda: os.system('clear') #for windows cls instead of clear
        
    def ask_height(self):
        ret = 0
        while (ret < 3):
            ret = int(raw_input("Set labyrinth height:"))
        return ret
    
    def ask_width(self):
        ret = 0
        while (ret < 3):
            ret = int(raw_input("Set labyrinth width:"))
        return ret        
    
    def print_player_info(self):
        print("Moves: "+str(self.game.player.getMoves()))
        
        
    def print_options(self):
        option = str(raw_input("OPTIONS:\nw: Move up\ns: Move down\na: Move left\nd: Move right\nq: Quit game\ng: Save game\n"))
        
        if(option == "w"):
            self.game.move(self.game.UP)
        if(option == "s"):
            self.game.move(self.game.DOWN)
        if(option == "a"):
            self.game.move(self.game.LEFT)
        if(option == "d"):
            self.game.move(self.game.RIGHT)
        if(option == "q"):
            return 'x'
        if(option == "l"):
            self.game.save_game()
        
    def print_game(self, maze):
        self.clear()
        
        for y in xrange(0, len(maze[0])):
            for x in xrange(0, len(maze)):
                sys.stdout.write(maze[x][y])
            sys.stdout.write("\n")
            
        self.print_player_info()
            
    def print_menu(self):
        accepted_choice ={0,1,2,3}
        menu_choice = -1
        while(not menu_choice in accepted_choice):
            menu_choice = input("MENU:\n1 = Start new game\n2 = Load game from a file\n3 = Exit\n")
        return int(menu_choice)
        
    def game_loop(self):
        while(True):
            maze = self.game.labyrinth.getMaze()
            maze[self.game.player.getX()][self.game.player.getY()] = "@"
            
            self.print_game(maze)
            
            if(self.print_options() == "x"):
                break
            
            
            