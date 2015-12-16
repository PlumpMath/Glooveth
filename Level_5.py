# Project imports
from Level import *

# Level 5
class Level_5(Level):
    def __init__(self, background):
        Level.__init__(self, background)
        #-----------------------------------------------------------------------------------------------------------------------------------------------
        #---------------------------------------------------LEVEL CONFIGURATION-------------------------------------------------------------------------
        #-----------------------------------------------------------------------------------------------------------------------------------------------
        self.num_level = 5
        
        # Scenes
        self.scene1 = 0
        self.scene2 = 0
        self.scene3 = 0
        self.scene4 = 0
        self.scene5 = 0
    #end __init__
    
    # It manages the level on every scene.
    def taskLevel(self, task):
        #------------------------------------------------------------------SCENE 1------------------------------------------------------------------
        # Appending items and enemies
        if self.scene1 == 0:
            self.scene1 = 1
            self.items.append(IStrawberry(-6,-6,55,0.75))
            self.items.append(IStrawberry(-6,-6,46,0.75))
            self.items.append(IStrawberry(-6,-6,37,0.75))
            self.items.append(IBanana(-4,-6,47,0.75))
            self.items.append(IFish(-4,-6,43,0.75))
            self.items.append(ILetuce(0,-6,55,0.75))
            self.items.append(IRice(0,-6,37,0.75))
        
        # Scene finished
        if self.scene1 == 1:
            if self.items == []:
                self.scene1 = 2
                self.moveOn()
        
        #------------------------------------------------------------------SCENE 2------------------------------------------------------------------
        # Appending items and enemies
        if (self.scene1 == 2) & (self.scene2 == 0):
            if self.movingBackground == False:
                self.scene2 = 1
                self.items.append(IStrawberry(4,-6,37,0.75))
                self.items.append(IStrawberry(4,-6,41,0.75))
                self.items.append(IStrawberry(4,-6,45,0.75))
                self.items.append(ICheese(4,-6,55,0.75))
                self.enemies.append(CDonu(16,-6,42))
                self.enemies.append(CCan(18,-6,42))
                self.enemies.append(CDonu(21,-6,42))
        
        # Scene finished
        if self.scene2 == 1:
            if self.enemies == []:
                self.scene2 = 2
                self.moveOn()
                self.removeItems()
        
        #------------------------------------------------------------------SCENE 3------------------------------------------------------------------
        # Appending items and enemies
        if (self.scene2 == 2) & (self.scene3 == 0):
            if self.movingBackground == False:
                self.scene3 = 1
                self.items.append(IStrawberry(2,-6,53,0.75))
                self.items.append(IStrawberry(2,-6,49,0.75))
                self.items.append(IStrawberry(2,-6,42,0.75))
                self.items.append(IEgg(6,-6,42,0.75))
                self.enemies.append(CPotatoes(17,-6,40))
                self.enemies.append(CCan(-17,-6,55))
        
        # Scene finished
        if self.scene3 == 1:
            if self.enemies == []:
                self.scene3 = 2
                self.moveOn()
                self.removeItems()
    
        #------------------------------------------------------------------SCENE 4------------------------------------------------------------------
        # Appending items and enemies
        if (self.scene3 == 2) & (self.scene4 == 0):
            if self.movingBackground == False:
                self.scene4 = 1
                self.items.append(IStrawberry(-9,-6,37,0.75))
                self.items.append(IStrawberry(-3,-6,43,0.75))
                self.items.append(IStrawberry(3,-6,49,0.75))
                self.items.append(ITomato(6,-6,55,0.75))
                self.enemies.append(CHamburger(-15,-6,45))
        
        # Scene finished
        if self.scene4 == 1:
            if self.enemies == []:
                self.scene4 = 2
                self.moveOn()
                self.removeItems()
        
        #------------------------------------------------------------------SCENE 5------------------------------------------------------------------
        # Appending items and enemies
        if (self.scene4 == 2) & (self.scene5 == 0):
            if self.movingBackground == False:
                self.scene5 = 1
                self.items.append(IStrawberry(8,-6,45,0.75))
                self.items.append(IStrawberry(9,-6,37,0.75))
                self.items.append(ICereal(-10,-6,37,0.75))
                self.enemies.append(CHamburger(15,-6,40))
                self.enemies.append(CHamburger(-15,-6,55))
                self.enemies.append(CPotatoes(-19,-6,37))
        
        # Scene finished
        if (self.scene5 == 1)&(self.state==0):
            if self.enemies == []:
                # Game won
                self.win = OnscreenImage(image="./tex/win.png", pos = (0, 0, 0),hpr=None, scale = (1.4,1.0,1.0), color=None, parent=None, sort=30)
                self.state = 1
                self.removeItems()
                        
                taskMgr.remove('taskLevel')
                
        return task.cont 
    #end taskLevel