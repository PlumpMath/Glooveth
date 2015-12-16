# Panda3D imports
from direct.gui.OnscreenImage import OnscreenImage
from pandac.PandaModules import TransparencyAttrib

# It manages the sun pointer on screen
class Pointer():
    def __init__(self):
        #-----------------------------------------------------------------------------------------------------------------------------------------------
        #---------------------------------------------------VARIABLE DECLARATION------------------------------------------------------------------------
        #-----------------------------------------------------------------------------------------------------------------------------------------------
        self.bitmap = OnscreenImage(image="./tex/sun_cursor.png", pos = (0, 0, 0),hpr=None, scale=0.05, color=None, parent=None, sort=200)
        self.bitmap.setTransparency(TransparencyAttrib.MAlpha)
    #end __init__
    
    #-----------------------------------------------------------------------------------------------------------------------------------------------
    #----------------------------------------------------------------FUNCTIONS----------------------------------------------------------------------
    #-----------------------------------------------------------------------------------------------------------------------------------------------
    # It sets the x position given
    def setPosX(self, x):
        self.posX = x*1.3
            
        self.bitmap.setX(self.posX)
    #end setPosX
    
    # It sets the y position given
    def setPosY(self, y):
        self.posY = y
        self.bitmap.setZ(self.posY)
    #end setPosY