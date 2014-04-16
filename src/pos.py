import game

class Pos(object):
    def __init__(self, x=0, y=0, z=0):
        if (isinstance(x, Pos)):
            self.setPosition(x.getX(), x.getY(), x.getZ())
        else:
            self.setPosition(x,y,z)
    
    def add(self, x, y=0, z=0):
        p = Pos(x, y, z)
        
        #calculate new position
        return Pos(self.getX()+p.getX(), self.getY()+p.getY(), self.getZ()+p.getZ())
    
    def subtract(self, x, y=0, z=0):
        p = Pos(x, y, z)
        
        #calculate new position
        return Pos(self.getX()-p.getX(), self.getY()-p.getY(), self.getZ()-p.getZ())
    
    def __eq__(self, obj):
        #http://www.dimagi.com/overriding-equals-in-python/
        return isinstance(obj, Pos) and self.getX() == obj.getX() and self.getY() == obj.getY() and self.getZ() == obj.getZ()
        
    
    def getDirection(self, x, y=0, z=0):
        p = Pos(x, y, z)
        deltaX = self.getX()-p.getX()
        deltaY = self.getY()-p.getY()
        
        if(abs(deltaX) > abs(deltaY)):
            if(deltaX > 0):
                return game.Game.RIGHT
            else:
                return game.Game.LEFT
        else:
            if(deltaY > 0):
                return game.Game.DOWN
            else:
                return game.Game.UP
            
    def setPosition(self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z
    
    def getX(self):
        return self.x
    
    def getY(self):
        return self.y
    
    def getZ(self):
        return self.z
    
    @staticmethod
    def inverse(direction):
        if(direction == game.Game.UP):
            return game.Game.DOWN
        
        if(direction == game.Game.DOWN):
            return game.Game.UP
        
        if(direction == game.Game.RIGHT):
            return game.Game.LEFT

        if(direction == game.Game.LEFT):
            return game.Game.RIGHT
        