from pos import Pos
from node import Node
import game

from random import randint
from random import shuffle

class Labyrinth():
    WALL = "#"
    CLEAR = ' '
    ROUTE = '.'
    PLAYER = '@'
    END = 'E'
    BRIDGE = '='
    
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
        #initPos = Pos(self.width/2, self.height/2)
        self.initNode = self.drawTile(initPos, initPos, False)
    
    def findNode(self, pos):
        for node in self.nodes:
            if(node.getCoords() == pos):
                return node
        
        return False
    
    def addWedges(self):

        for y in range(0, len(self.maze[0])):
            for x in range(4, len(self.maze)):
                if(randint(0, 3 * self.width * self.height) < 1 and
                    self.maze[x-4][y] == True and
                    self.maze[x-3][y] == False and
                    self.maze[x-2][y] == True and
                    self.maze[x-1][y] == False and
                    self.maze[x][y] == True):
                    start = self.findNode(Pos(x-4,y))
                    end =  self.findNode(Pos(x,y))
                    #first bridge node
                    bridge1 = Node(Pos(x-3, y, 1))
                    bridge1.setConnection(game.Game.RIGHT, start)
                    self.nodes.append(bridge1)
                    
                    bridge2 = Node(Pos(x-2, y, 1))
                    bridge2.setConnection(game.Game.RIGHT, bridge1)
                    self.nodes.append(bridge2)
                    
                    bridge3 = Node(Pos(x-1, y, 1))
                    bridge3.setConnection(game.Game.RIGHT, bridge2)
                    bridge3.setConnection(game.Game.LEFT, end)
                    self.nodes.append(bridge3)
                    
                                        
                    
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
                newNode.setId(len(self.nodes))
                self.nodes.append(newNode)
                
                if(self.endNode is False or self.endNode.getDepth() < newNode.getDepth()):
                    self.endNode = newNode
                
                    
                #shuffle the direction list every once in a while
                if (randint(0,5) < 1):
                    shuffle(self.directions)
                
                #copy the list of all the possible directions
                dirs = list(self.directions)
                
                for d in dirs:
                    self.drawTile(pos, pos.add(d), newNode)
                
                self.addWedges()
                    
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
            if (node.hasPlayer()):
                maze[node.getX()][node.getY()] = self.PLAYER
            elif (node.isFlagged()):
                maze[node.getX()][node.getY()] = self.ROUTE
            elif (node.getZ() == 1):
                maze[node.getX()][node.getY()] = self.BRIDGE
            else:
                maze[node.getX()][node.getY()] = self.CLEAR
        
        maze[self.endNode.getX()][self.endNode.getY()] = self.END
        
        return maze
    
    def solve_maze(self, startNode):
        #bfs
        neighbours = list()
        
        neighbours.append(startNode)
        
        while(len(neighbours) > 0):
            currentNode = neighbours.pop()
            
            if (currentNode == self.endNode):
                break
            
            for i in range(0,4):
                neighbour = currentNode.getConnection(i)
                if(neighbour is not False and neighbour.getPrev() is False):
                    
                    neighbour.setPrev(currentNode)
                    neighbours.append(neighbour)
        
        #travel backwards the route we just discovered
        while (currentNode.getPrev() != False and currentNode != startNode):
            currentNode.setFlag()
            currentNode = currentNode.getPrev()
    
    def getStartNode(self):
        return self.initNode

    def getEndNode(self):
        return self.endNode   
    
    
    