#from labyrinth import Labyrinth
#from game import Game
import sys
import os

class GUI(object):
    def __init__(self, game):
        self.game = game
        self.clear = lambda: os.system('cls') #for windows cls instead of clear
        
    def ask_height(self):
        ret = 0
        while (ret < 3):
            ret = int(input("Set labyrinth height:"))
        return ret
    
    def ask_width(self):
        ret = 0
        while (ret < 3):
            ret = int(input("Set labyrinth width:"))
        return ret        
    
    def print_player_info(self):
        print("Moves: "+str(self.game.player.getMoves()))
        
        
    def print_options(self):
        print("OPTIONS:\nw: Move up\ns: Move down\na: Move left\nd: Move right\nq: Quit game\ng: Save game\n")
            
    def handle_options(self):
        option = str(input())
        self.clear()
        
        if(option == "w"):
            self.game.move(self.game.UP)
        elif(option == "s"):
            self.game.move(self.game.DOWN)
        elif(option == "a"):
            self.game.move(self.game.LEFT)
        elif(option == "d"):
            self.game.move(self.game.RIGHT)
        elif(option == "q"):
            self.game.labyrinth.solve_maze(self.game.player.getCurrentNode())
            return False
        elif(option == "g"):
            self.game.save_game()
            return True
        else:
            self.print_options()
        return True
    
    def print_game(self, maze):
        for y in range(0, len(maze[0])):
            for x in range(0, len(maze)):
                sys.stdout.write(maze[x][y])
            sys.stdout.write("\n")
            
        self.print_player_info()
            
    def print_menu(self):
        accepted_choice ={0,1,2,3}
        menu_choice = -1
        while(not menu_choice in accepted_choice):
            menu_choice = int(input("MENU:\n1 = Start new game\n2 = Load game from a file\n3 = Exit\n"))
        return int(menu_choice)
        
    def game_loop(self):
        self.clear()
        self.print_options()
        while(True):
            
            maze = self.game.labyrinth.getMaze()
            self.print_game(maze)
            
            if(self.handle_options() == False):
                maze = self.game.labyrinth.getMaze()
                self.print_game(maze)
                break
            
            
            if (self.game.hasWon()):
                print("You won!")
                break
            

            
            
            