from pos import Pos
from node import Node

from random import randint
from random import shuffle

class Labyrinth():
    WALL = '#'
    CLEAR = ' '
    END = 'E'
    
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.maze = [[False for i in range(height)] for j in range(width)]
        self.nodes = list()
        self.endNode = False
        
        #make a list of the possible directions
        self.directions = list()
        self.directions.append(Pos(1,0))
        self.directions.append(Pos(-1,0))                
        self.directions.append(Pos(0,1))
        self.directions.append(Pos(0,-1))
        
        #set the starting position
        initPos = Pos(1,1)
        self.initNode = self.drawTile(initPos, initPos, False)
    
    def drawTile(self, prevPos, pos, prevNode):
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
                self.maze[pos.x][pos.y] = True
                #in the first node the prev param should be false
                depth = 0
                if(prevNode != False):
                    depth = prevNode.getDepth() + 1
                newNode = Node(pos, prevNode, depth)
                #add to list
                self.nodes.append(newNode)
                
                if(self.endNode == False or self.endNode.getDepth() < newNode.getDepth()):
                    self.endNode = newNode
                
                    
                #shuffle the direction list every once in a while
                if (randint(0,5) < 1):
                    shuffle(self.directions)
                
                #copy the list of all the possible directions
                dirs = list(self.directions)
                
                for dir in dirs:
                    self.drawTile(pos, pos.add(dir), newNode)
                    
                return newNode
        
        
    def isDrawable(self, pos):
        #make sure the proposed position is within the map
        if (pos.x<0 or pos.y<0):
            return False
        if (pos.x>=self.width or pos.y>=self.height):
            return False
        #make sure the proposed position has not yet been drawn to
        if (self.maze[pos.x][pos.y]):
            return False
        return True
    
    def getMaze(self):
        maze = [[self.WALL for i in range(self.height)] for j in range(self.width)]
        
        for node in self.nodes:
            maze[node.getX()][node.getY()] = self.CLEAR
        
        maze[self.endNode.getX()][self.endNode.getY()] = self.END
        
        return maze
    
    def solve_maze(self):
        return "ssseeeeeesss"
    
    def getStartNode(self):
        return self.initNode
    
    