class Pos(object):
    def __init__(self, x=0, y=0, z=0):
        self.setPosition(x,y, z)
    
    def add(self, x, y=False):
        if (y is False and not x.y is False):
            pos = x;
            return self.add(pos.x, pos.y)
        
        return Pos(self.x+x, self.y+y)
    
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