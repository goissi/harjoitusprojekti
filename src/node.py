from pos import Pos

class Node(object):
    def __init__(self, coords, prev=False, depth=0):
        self.coords = coords
        self.connections = [False for i in range(4)]
        self.depth = depth
        self.id = 0
        
        if(prev):
            #deduce the direction of the previous node
            direction = self.getCoords().getDirection(prev.getCoords())
            self.setConnection(direction, prev)
        
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
        
    