# Python imoprts
import math
import array
from math import sqrt

# Panda3D imports
from direct.gui.OnscreenImage import OnscreenImage
from pandac.PandaModules import *

# Project imports
from Character import *
from Image import *
from CHamburger import *

# It manages the main character
class CMain (Character):
    def __init__(self, x, y, z):
        Character.__init__(self, x, y, z)
        
        #-----------------------------------------------------------------------------------------------------------------------------------------------
        #---------------------------------------------------VARIABLE DECLARATION------------------------------------------------------------------------
        #-----------------------------------------------------------------------------------------------------------------------------------------------
        self.energy = 100
        self.power = array.array("I",[0,0,0,0,0])
        self.life = 3
        self.scale = 3.0
        self.bitmap = Image();
        self.walking = False
        self.model = self.bitmap.loadModel("./models/Square.egg", "./tex/boy.png", self.posX, self.posY, self.posZ, self.scale)
        self.isInvincible = False
        self.isVisible = True
        self.att = None
        self.attacking = False
        self.nearEnemy = None
        self.lastTime = 0.0
        self.soundDamage = base.loadSfx('./sound/damage.wav')
        self.soundDamage.setVolume(.8)
        
        self.lastPosX = 0
        self.lastPosY = 0
    #end __init__
    
    #-----------------------------------------------------------------------------------------------------------------------------------------------
    #----------------------------------------------------------------FUNCTIONS----------------------------------------------------------------------
    #-----------------------------------------------------------------------------------------------------------------------------------------------
    # It moves the character depending on sun pointer position on the screen
    def movement(self, x, y):
        self.walking = False
        
        if (y>=-1) and (y<=1):
            # Moving the character
            if (y<-0.75): realZ = 28
            if (y>-0.35) and (y<=1): realZ = 59
            if (y<=-0.35) and (y>=-0.75):
                #Z coordinate
                realZ = ( ( (y-(-0.35))/(-0.75-(-0.35)) )*(28-59) ) + 59
            
            # X coordinate    
            realX = ( ( (realZ-(28))/(59-28) )*(21-10) ) + 10
            
            # Velocity of the character depends on the distance to the sun pointer
            velX = math.fabs((x*realX) - self.posX)
            velY = math.fabs(realZ - self.posZ)
            modVel = (velX*velX) + 1.0
            modVel = (velX*velX) + (velY*velY)
            modVel = math.sqrt(modVel)
            modVelX = velX/modVel
            modVelY = velY/modVel

            # Moving the character to the correct side
            pointX = x*realX
            pointZ = realZ
            if self.posX > x*realX: pointX = self.posX - 0.625*modVelX
            if self.posX < x*realX: pointX = self.posX + 0.625*modVelX
            if self.posZ < realZ:   pointZ = self.posZ + 0.625*modVelY
            if self.posZ > realZ:   pointZ = self.posZ - 0.625*modVelY
            if( (self.posX < x*realX+0.3) and (self.posX > x*realX-0.3)  ):
                pass
            else:
                self.interval = self.model.posInterval(0.0625, Point3(pointX,pointZ,self.posY))
                self.interval.start()
            
            # Update position
            self.lastPosX = self.posX
            self.lastPosY = self.posY
            self.posX = self.model.getX()
            self.posZ = self.model.getY()
            
            # Checking if the character is walking or not
            if ( (math.fabs(self.posX-self.lastPosX) != 0) | (math.fabs(self.posY-self.lastPosY) != 0 ) ):
                self.walking = True
    #end movement
    
    # It gets an item and indentify the type to extract energy and power to the character
    def itemCollect(self, item):
        item.collectIt = True
        self.energy = self.energy + item.energy
        
        if self.energy>200: self.energy=200
        
        # Power ability
        if item.type == "GRAIN":        self.power[0] = self.power[0] + 1
        if item.type == "FRUIT":        self.power[1] = self.power[1] + 1
        if item.type == "MILK":         self.power[2] = self.power[2] + 1
        if item.type == "VEGETABLE":    self.power[3] = self.power[3] + 1
        if item.type == "FISH":         self.power[4] = self.power[4] + 1
        
        # Energy
        self.energy = self.energy + item.energy
    #end itemCollect
    
    # It sets the character invincible and start the corresponding task
    def setInvincible(self, invincible):
        self.isInvincible = True
        taskMgr.add(self.taskInvincible, 'taskInvincible' )
    #end setInvincible
    
    # It makes disappear the character
    def hide(self):
        self.model.hide()
    #end hide
    
    #-----------------------------------------------------------------------------------------------------------------------------------------------
    #----------------------------------------------------------------TASKS,THREADS------------------------------------------------------------------
    #-----------------------------------------------------------------------------------------------------------------------------------------------
    # It makes that sprite's character have an alpha effect for 2 seconds
    def taskInvincible(self, task):
        if task.time > 2:
            # Finishes the invicible property
            self.isInvincible = False
            self.model.show()
            self.isVisible = True
            self.lastTime = 0.0
            return task.done
        else:
            if (task.time - self.lastTime) > 0.15:
                self.lastTime = task.time
                if self.isVisible == True:  
                    self.model.hide()
                    self.isVisible = False
                else:
                    self.model.show()
                    self.isVisible = True
                
            return task.cont
    #end taskInvincible
    
#end class CMain