from labyrinth import Labyrinth

class GUI(object):
    


    def __init__(self, game):
        self.game = game
    
    
    def print_options(self):
        return str(input("OPTIONS:\nw: Move up\ns: Move down\na: Move left\nd: Move right\nq: Quit game\ng: Save game\n"))
        
    def print_game(self, maze):
        #print("|@#####|\n| #   #|\n| #*###|\n|    * |\n| #### |\n|#####E|\n")
        #|@#####|
        #| #   #|
        #| #*###|
        #|    * |
        #| #### |
        #|#####E|
        
        for row in maze:
            print(row)
            
            
    def print_menu(self):
        accepted_choice ={0,1,2,3}
        menu_choice = -1
        while(not menu_choice in accepted_choice):
            return int(input("MENU:\n1 = Start new game\n2 = Load game from a file\n3 = Exit\n"))
        
        
            

            
        def print_options():
            print("OPTIONS: w: Move up\ns: Move down\na: Move left\nd: Move right\n q: Quit game\n g: Save game\n")
            
            
            