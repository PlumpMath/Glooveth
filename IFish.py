# Project imports
from Item import *
from Image import *

# Fish Item
class IFish (Item):
    def __init__(self, x, y, z, scale):
        Item.__init__(self, x, y, z)
        
        #-----------------------------------------------------------------------------------------------------------------------------------------------
        #---------------------------------------------------VARIABLE DECLARATION------------------------------------------------------------------------
        #-----------------------------------------------------------------------------------------------------------------------------------------------
        self.scale = scale;
        self.energy = 5;
        self.powerAbility = 35;
        self.type = "FISH"
        self.specialItem = False
        self.bitmap = Image()
        self.model = self.bitmap.loadModel("./models/Square.egg", "./tex/fish.png", self.posX, self.posY, self.posZ, self.scale)        
    #end __init__
    
#end class IFish