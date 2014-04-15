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