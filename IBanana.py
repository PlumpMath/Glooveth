# Project imports
from Item import *
from Image import *

# Banana Special Item
class IBanana (Item):
    def __init__(self, x, y, z, scale):
        Item.__init__(self, x, y, z)
        
        #-----------------------------------------------------------------------------------------------------------------------------------------------
        #---------------------------------------------------VARIABLE DECLARATION------------------------------------------------------------------------
        #-----------------------------------------------------------------------------------------------------------------------------------------------
        self.scale = scale;
        self.energy = 25;
        self.powerAbility = 35;
        self.type = "FRUIT"
        self.specialItem = True
        self.bitmap = Image()
        self.model = self.bitmap.loadModel("./models/Square.egg", "./tex/banana_s.png", self.posX, self.posY, self.posZ, self.scale)        
    #end __init__
    
#end class IBanana