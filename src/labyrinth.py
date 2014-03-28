from pos import Pos
from random import shuffle
from random import randint

class Labyrinth():
    WALL = '#'
    CLEAR = ' '
    
    def __init__(self, width, height):
        self.width = width
        self.height = height
        
        self.maze = [[self.WALL for i in range(width)] for j in range(height)]
        
        #make a list of the possible directions
        self.directions = list()
        self.directions.append(Pos(1,0))
        self.directions.append(Pos(-1,0))                
        self.directions.append(Pos(0,1))
        self.directions.append(Pos(0,-1))
        
        #set the starting position
        self.drawTile(Pos(1,1), Pos(1,1))
    
    def drawTile(self, prevPos, pos):
        if (self.isDrawable(pos)):
            #calculate delta from prevPos
            dx = pos.x - prevPos.x
            dy = pos.y - prevPos.y
            
            #make sure the neighboring tiles haven't been drawn to
            if (
                self.isDrawable(pos.add(dx, dy)) #the next tile is drawable
                and self.isDrawable(pos.add(dy, dx)) #90 deg angle in both directions is drawable so that we have walls
                and self.isDrawable(pos.add(-dy, -dx))
                and self.isDrawable(pos.add(dx, dy).add(dy, dx)) #90 deg angle in both directions beside the next tile is drawable so that we have walls
                and self.isDrawable(pos.add(dx, dy).add(-dy, -dx))
            ):
                self.maze[pos.x][pos.y] = self.CLEAR
                
                #shuffle the direction list every once in a while
                if (randint(0,5) < 1):
                    shuffle(self.directions)
                
                #copy the list of all the possible directions
                dirs = list(self.directions)
                
                for dir in dirs:
                    self.drawTile(pos, pos.add(dir))
        
        
    def isDrawable(self, pos):
        #make sure the proposed position is within the map
        if (pos.x<0 or pos.y<0):
            return False
        if (pos.x>=self.width or pos.y>=self.height):
            return False
        #make sure the proposed position has not yet been drawn to
        if (self.maze[pos.x][pos.y] != self.WALL):
            return False
        return True
    
    def getMaze(self):
        return self.maze
    
    def solve_maze(self):
        return "ssseeeeeesss"