from pos import Pos
import game

class Node(object):
    def __init__(self, coords, prev=False, depth=0):
        self.coords = coords
        self.connections = [False for i in range(4)]
        self.depth = depth
        self.id = 0
        self.flagged = False
        self.playerOnboard = False
        self.prev = False #this is for solving the maze and is obsolete before that
        
        if(prev):
            #deduce the direction of the previous node
            direction = self.getCoords().getDirection(prev.getCoords())
            self.setConnection(direction, prev)
    
    def __eq__(self, obj):
        return isinstance(obj, Node) and self.getCoords() == obj.getCoords()
    
    def __ne__(self, obj):
        return not self.__eq__(obj)
    
    def getDepth(self):
        return self.depth
    
    def getCoords(self):
        return self.coords
    
    def getX(self):
        return self.coords.getX()
    
    def getY(self):
        return self.coords.getY()
    
    def getZ(self):
        return self.coords.getZ()
    
    def setConnection(self, direction, node):
        if(direction >= 0 and direction <= 3):
            self.connections[Pos.inverse(direction)] = node
            node.connections[direction] = self;
            
    def getConnection(self, direction):
        #tarkasta!
        if(direction >= 0 and direction <= 3):
            return self.connections[direction]
        
    def isFlagged(self):
        return self.flagged
    
    def setFlag(self):
        self.flagged = True
        
    def setPrev(self, node):
        self.prev = node
        
    def getPrev(self):
        return self.prev
    
    def hasPlayer(self):
        return self.playerOnboard
    
    def setPlayer(self, hasPlayer):
        self.playerOnboard = hasPlayer
        
    def setId(self, ident):
        self.id = ident
        
    def getId(self):
        return self.id
    
    def info(self):
        
        s = "Id:" + str(self.getId()) + "\n"
        s += "X:" + str(self.getX()) + "\n"
        s += "Y:" + str(self.getY()) + "\n"
        s += "Z:" + str(self.getZ()) + "\n"
        if(self.getConnection(game.Game.UP)):
            s += "ConnectionUP:" + str(self.getConnection(game.Game.UP).getId) + "\n"
        if(self.getConnection(game.Game.DOWN)):
            s += "ConnectionDOWN:" + str(self.getConnection(game.Game.DOWN).getId) + "\n"
        if(self.getConnection(game.Game.RIGHT)):
            s += "ConnectionRIGHT:" + str(self.getConnection(game.Game.RIGHT).getId) + "\n"
        if(self.getConnection(game.Game.LEFT)):
            s += "ConnectionLEFT:" + str(self.getConnection(game.Game.LEFT).getId) + "\n"              
        
        return s
        
        