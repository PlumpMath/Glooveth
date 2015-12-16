# Project imports
from Level import *

# Level 6
class Level_6(Level):
    def __init__(self, background):
        Level.__init__(self, background)
        #-----------------------------------------------------------------------------------------------------------------------------------------------
        #---------------------------------------------------LEVEL CONFIGURATION-------------------------------------------------------------------------
        #-----------------------------------------------------------------------------------------------------------------------------------------------
        self.num_level = 6
        
        # Scenes
        self.scene1 = 0
        self.scene2 = 0
        self.scene3 = 0
        self.scene4 = 0
        self.scene5 = 0
        self.scene6 = 0
    #end __init__
    
    # It manages the level on every scene.
    def taskLevel(self, task):
        #------------------------------------------------------------------SCENE 1------------------------------------------------------------------
        # Appending items and enemies
        if self.scene1 == 0:
            self.scene1 = 1
            self.items.append(IStrawberry(-6,-6,55,0.75))
            self.items.append(ILetuce(0,-6,37,0.75))
            self.items.append(IRice(10,-6,45,0.75))            
        
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
                self.items.append(IMilk(4,-6,39,0.75))
                self.items.append(ILetuce(-4,-6,45,0.75))
                self.items.append(IEgg(-10,-6,55,0.75))
                self.enemies.append(CHamburger(16,-6,45))
                self.enemies.append(CCan(20,-6,55))
                self.enemies.append(CPotatoes(-21,-6,37))
        
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
                self.items.append(IStrawberry(-9,-6,55,0.75))
                self.items.append(ILetuce(-7,-6,40,0.75))
                self.items.append(IMilk(8,-6,45,0.75))
                self.items.append(ICereal(10,-6,37,0.75))
                self.enemies.append(CDonu(17,-6,40))
                self.enemies.append(CCan(22,-6,55))
        
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
                self.items.append(IFish(0,-6,55,0.75))
                self.items.append(ICheese(10,-6,55,0.75))
                self.enemies.append(CPotatoes(15,-6,45))
                self.enemies.append(CPotatoes(-15,-6,45))
        
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
                self.items.append(IFish(-4,-6,42,0.75))
                self.items.append(IMilk(2,-6,50,0.75))
                self.items.append(IBanana(-8,-6,45,0.75))
                self.enemies.append(CHamburger(-15,-6,55))
                self.enemies.append(CDonu(-15,-6,37))
                self.enemies.append(CPotatoes(15,-6,55))
                self.enemies.append(CCan(15,-6,37))
        
        # Scene finished
        if self.scene5 == 1:
            if self.enemies == []:
                self.scene5 = 2
                self.moveOn()
                self.removeItems()
                        
        #------------------------------------------------------------------SCENE 6------------------------------------------------------------------
        # Appending items and enemies
        if (self.scene5 == 2) & (self.scene6 == 0):
            if self.movingBackground == False:
                self.scene6 = 1
                self.items.append(IFish(-6,-6,50,0.75))
                self.items.append(IStrawberry(6,-6,50,0.75))
                self.items.append(IRice(6,-6,40,0.75))
                self.items.append(ITomato(-6,-6,40,0.75))
                self.enemies.append(CHamburger(-15,-6,45))
                self.enemies.append(CDonu(15,-6,37))
                self.enemies.append(CPotatoes(15,-6,55))
                        
        # Scene finished
        if (self.scene6 == 1)&(self.state==0):
            if self.enemies == []:
                #Game won
                self.win = OnscreenImage(image="./tex/win.png", pos = (0, 0, 0),hpr=None, scale = (1.4,1.0,1.0), color=None, parent=None, sort=30)
                        
                taskMgr.remove('taskLevel')
                
        return task.cont 
    #end taskLevel