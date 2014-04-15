from pos import Pos

class Node(object):
    def __init__(self, coords, prev=False):
        self.coords = coords
        self.connections = [False for i in range(4)]
        
        if(prev):
            #deduce the direction of the previous node
            direction = self.getCoords().getDirection(prev.getCoords())
            self.setConnection(direction, prev)
            prev.setConnection(Pos.inverse(direction), self)
                
        
    def getCoords(self):
        return self.coords
    
    def setConnection(self, direction, node):
        if(direction >= 0 and direction <= 4):
            self.connections[direction] = node
    