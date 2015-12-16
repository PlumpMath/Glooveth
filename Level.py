# Python imports
import math

# Panda3D imports
from direct.gui.OnscreenImage import OnscreenImage
from pandac.PandaModules import Point3

# Project imports
from IStrawberry import *
from IFish import *
from IMilk import *
from ILetuce import *
from IRice import *
from IBanana import *
from ICereal import *
from ICheese import *
from IEgg import *
from ITomato import *
from CHamburger import *
from CCan import *
from CDonu import *
from CPotatoes import *

# Generic Level
class Level:
    def __init__(self, background):
        #-----------------------------------------------------------------------------------------------------------------------------------------------
        #---------------------------------------------------VARIABLE DECLARATION------------------------------------------------------------------------
        #-----------------------------------------------------------------------------------------------------------------------------------------------
        # Background
        self.back = background
        self.back[0].setX(34)
        self.back[1].setX(146)
        
        # Arrow
        self.arrow = OnscreenImage(image="./tex/fletxa.png", pos = (1.1, 0, 0.60),hpr=None, scale = (0.20,0,0.20), color=None, parent=None, sort=5)
        self.arrow.setTransparency(TransparencyAttrib.MAlpha)
        self.arrow.hide()
        self.arrowSound = base.loadSfx('./sound/fletxa.wav')
        self.arrowSound.setVolume(.5)
        
        # Items, enemies list
        self.items = []
        self.enemies = []
        
        # Others
        self.numMoveIt = 0
        self.movingBackground = False
        self.state = 0
        self.win = None
        
        #-----------------------------------------------------------------------------------------------------------------------------------------------
        #---------------------------------------------------LEVEL CONFIGURATION-------------------------------------------------------------------------
        #-----------------------------------------------------------------------------------------------------------------------------------------------
        # Start tasks
        taskMgr.add(self.taskLevel, 'taskLevel')
        
    #end __init__
    
    #-----------------------------------------------------------------------------------------------------------------------------------------------
    #----------------------------------------------------------------FUNCTIONS----------------------------------------------------------------------
    #-----------------------------------------------------------------------------------------------------------------------------------------------
    # It moves the background on screen.
    def moveBackground(self,x,y):
        if( math.fabs(self.numMoveIt-self.back[0].getX()) >= 30.0 ):
            self.movingBackground = False
            self.arrow.hide()
    #end moveBackground
    
    # It hides the level.
    def hideLevel(self):
        self.win.hide()
    #end hideLevel
    
    # It configures the level for a level transition.
    def moveOn(self):
        self.numMoveIt = 0
        self.movingBackground = True
        self.interval = self.back[0].posInterval(5.0, Point3(self.back[0].getX()-30,self.back[0].getY(),self.back[0].getZ()))
        self.interval.start()
        self.interval2 = self.back[1].posInterval(5.0, Point3(self.back[1].getX()-30,self.back[1].getY(),self.back[1].getZ()))
        self.interval2.start()
        self.numMoveIt = self.back[0].getX()
        self.arrow.show()
        self.arrowSound.play()
    #end moveOn
    
    # It removes all items from screen.
    def removeItems(self):
        while self.items != []:
            for x in self.items:
                x.model.setX(-100)
                self.items.remove(x)
    #end removeItems
    
    # It removes all the items and enemies from screen.
    def removeAll(self):
        while self.items != []:
            for x in self.items:
                x.model.setX(-100)
                self.items.remove(x)
                
        while self.enemies != []:
            for x in self.enemies:
                x.model.setX(-100)
                x.life = x.life - 1
                self.enemies.remove(x)
    #end removeAll
    
    #-----------------------------------------------------------------------------------------------------------------------------------------------
    #----------------------------------------------------------------TASKS,THREADS------------------------------------------------------------------
    #-----------------------------------------------------------------------------------------------------------------------------------------------
    # It manages the level on every scene.
    def taskLevel(self, task):
        return task.cont
    #end taskLevel
    
#end class Level