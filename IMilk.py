# Project imports
from Item import *
from Image import *

# Milk item
class IMilk (Item):
    def __init__(self, x, y, z, scale):
        Item.__init__(self, x, y, z)
        
        #-----------------------------------------------------------------------------------------------------------------------------------------------
        #---------------------------------------------------VARIABLE DECLARATION------------------------------------------------------------------------
        #-----------------------------------------------------------------------------------------------------------------------------------------------
        self.scale = scale;
        self.energy = 20;
        self.powerAbility = 35;
        self.type = "MILK"
        self.specialItem = False
        self.bitmap = Image()
        self.model = self.bitmap.loadModel("./models/Square.egg", "./tex/milk.png", self.posX, self.posY, self.posZ, self.scale)        
    #end __init__
    
#end class IMilk