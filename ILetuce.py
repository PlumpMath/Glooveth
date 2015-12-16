# Project imports
from Item import *
from Image import *

# Letuce item
class ILetuce (Item):
    def __init__(self, x, y, z, scale):
        Item.__init__(self, x, y, z)
        
        #-----------------------------------------------------------------------------------------------------------------------------------------------
        #---------------------------------------------------VARIABLE DECLARATION------------------------------------------------------------------------
        #-----------------------------------------------------------------------------------------------------------------------------------------------
        self.scale = scale;
        self.energy = 15;
        self.powerAbility = 35;
        self.type = "VEGETABLE"
        self.specialItem = False
        self.bitmap = Image()
        self.model = self.bitmap.loadModel("./models/Square.egg", "./tex/letuce.png", self.posX, self.posY, self.posZ, self.scale)        
    #end __init__
    
#end class ILetuce