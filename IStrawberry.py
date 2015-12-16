# Project imports
from Item import *
from Image import *

# Strawberry item
class IStrawberry (Item):
    def __init__(self, x, y, z, scale):
        Item.__init__(self, x, y, z)
        
        #-----------------------------------------------------------------------------------------------------------------------------------------------
        #---------------------------------------------------VARIABLE DECLARATION------------------------------------------------------------------------
        #-----------------------------------------------------------------------------------------------------------------------------------------------
        self.scale = scale;
        self.energy = 10;
        self.powerAbility = 35;
        self.type = "FRUIT"
        self.specialItem = False
        self.bitmap = Image()
        self.model = self.bitmap.loadModel("./models/Square.egg", "./tex/straw.png", self.posX, self.posY, self.posZ, self.scale)        
    #end __init__
    
#end class IStrawberry