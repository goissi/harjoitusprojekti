#from labyrinth import Labyrinth
#from game import Game
import sys
import os
import platform

class GUI(object):
    def __init__(self, game, stdin = sys.stdin):
        self.game = game
        self.stdin = stdin
        if platform.system() == 'Windows':
            self.clear = lambda: os.system('cls')
        else:
            self.clear = lambda: os.system('clear')
    
    def ask(self):
        return self.stdin.readline().strip()
    
    def ask_width(self):
        ret = 0
        while (ret < 4):
            print("Set labyrinth width:")
            ret = int(self.ask())
        return ret
    
    def ask_height(self):
        ret = 0
        while (ret < 4):
            print("Set labyrinth height:")
            ret = int(self.ask())
        return ret
    
    def print_player_info(self):
        print("Moves: "+str(self.game.player.getMoves()))
        
        
    def print_options(self):
        print("OPTIONS:\nw: Move up\ns: Move down\na: Move left\nd: Move right\nq: Quit game\ng: Save game\n")
            
    def handle_options(self):
        option = str(self.ask())
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
    
    def print_game(self):
        maze = self.game.labyrinth.getMaze()
        
        for y in range(0, len(maze[0])):
            for x in range(0, len(maze)):
                sys.stdout.write(maze[x][y])
            sys.stdout.write("\n")
            
        self.print_player_info()
            
    def print_menu(self):
        accepted_choice ={0,1,2,3}
        menu_choice = -1
        while(not menu_choice in accepted_choice):
            print("MENU:\n1 = Start new game\n2 = Load game from a file\n3 = Exit\n")
            menu_choice = int(self.ask())
        return int(menu_choice)
        
    def game_loop(self):
        self.clear()
        self.print_options()
        while(True):
            
            
            self.print_game()
            
            if(self.handle_options() == False):
                self.print_game()
                break
            
            
            if (self.game.hasWon()):
                print("You won!")
                break
            

            
            
            