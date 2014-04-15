from pos import Pos

class Node(object):
    def __init__(self, coords, prev):
        self.coords = coords
        self.north = False
        self.east = False
        self.south = False
        self.west = False
        
    def setPrev(self, prev):
        