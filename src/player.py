#from node import Node


class Player(object):
    
    def __init__(self, startNode):
        self.currentNode = startNode
        self.moves = 0
        
    def getX(self):
        return self.currentNode.getX()
    
    def getY(self):
        return self.currentNode.getY()
    
    def getZ(self):
        return self.currentNode.getZ()
    
    def move(self, direction):
        
        print("DIR:", direction)
        connection = self.currentNode.getConnection(direction)
        
        if(connection):
            self.moves += 1
            self.currentNode = connection
            
        else:
            return False
    
    def getMoves(self):
        return self.moves