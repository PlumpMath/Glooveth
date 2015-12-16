# Panda3D imports
from direct.gui.OnscreenImage import OnscreenImage
from pandac.PandaModules import TransparencyAttrib

# Project imports
from Image import *
from CEnemy import *
from Attack import *

# Can Enemy
class CCan (CEnemy):
    def __init__(self, x, y, z):
        CEnemy.__init__(self, x, y, z)
        
        #-----------------------------------------------------------------------------------------------------------------------------------------------
        #---------------------------------------------------VARIABLE DECLARATION------------------------------------------------------------------------
        #-----------------------------------------------------------------------------------------------------------------------------------------------
        self.life = 1
        self.scale = (1.5,1.0,3.0)
        self.bitmap = Image();
        self.model = self.bitmap.loadModel("./models/Square.egg", "./tex/eCan.png", self.posX, self.posY, self.posZ, self.scale)
        
        # Sound
        self.soundDeath = base.loadSfx('./sound/die4.wav')
        self.soundDeath.setVolume(.5)
        
    #end __init__
    
    #-----------------------------------------------------------------------------------------------------------------------------------------------
    #----------------------------------------------------------------FUNCTIONS----------------------------------------------------------------------
    #-----------------------------------------------------------------------------------------------------------------------------------------------
    # It Shooots an attack to the point where is the main character at that moment
    def attack(self,mainCharX,mainCharY,mainCharZ):
        char = [mainCharX,mainCharY,mainCharZ]
        enemy = [self.posX,self.posY,self.posZ]
        
        self.att = Attack("ENEMY", "CAN", self, char)
        self.attacking = True;
    #end attack
    
#end class CMain