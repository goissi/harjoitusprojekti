#from node import Node


class Player(object):
    
    def __init__(self, startNode):
        self.currentNode = startNode
        #set the hasPlayer to true on the startNode
        self.currentNode.setPlayer(True)
        self.moves = 0
        
    def getX(self):
        return self.currentNode.getX()
    
    def getY(self):
        return self.currentNode.getY()
    
    def getZ(self):
        return self.currentNode.getZ()
    
    def move(self, direction):
        
        connection = self.currentNode.getConnection(direction)
        
        if(connection):
            self.moves += 1
            #set the hasPlayer to false on the old node
            self.currentNode.setPlayer(False)
            self.currentNode = connection
            #set the hasPlayer to true on the new node
            self.currentNode.setPlayer(True)
            
        else:
            return False
    
    def getMoves(self):
        return self.moves
    
    def getCurrentNode(self):
        return self.currentNode