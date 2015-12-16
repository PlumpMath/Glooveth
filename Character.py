# Panda3D imports
from direct.showbase import DirectObject
from direct.showbase.DirectObject import DirectObject

# Project imports
from Image import *

# Generic character specification
class Character (DirectObject):
    def __init__(self, x, y, z):
        #-----------------------------------------------------------------------------------------------------------------------------------------------
        #---------------------------------------------------VARIABLE DECLARATION------------------------------------------------------------------------
        #-----------------------------------------------------------------------------------------------------------------------------------------------
        self.posX = x
        self.posY = y
        self.posZ = z
        self.life = 0
        self.dead = False
        self.scale = 1.0
        self.att = None
        self.attacking = False
        self.bitmap = None
    #end __init__
    
    #-----------------------------------------------------------------------------------------------------------------------------------------------
    #----------------------------------------------------------------FUNCTIONS----------------------------------------------------------------------
    #-----------------------------------------------------------------------------------------------------------------------------------------------
    #It sets the x position given to the x position of the character
    def setPosX(self, x):
        self.posX = x*1.3
        self.bitmap.setX(self.posX)
    #end setPosX
    
    #It sets the y position given to the y position of the character
    def setPosY(self, y):
        self.posY = y
        self.bitmap.setZ(self.posY)
    #end setPosY        
    
#end class Character