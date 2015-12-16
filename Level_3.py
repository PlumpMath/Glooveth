# Project imports
from Level import *

# Level 3
class Level_3(Level):
    def __init__(self, background):
        Level.__init__(self, background)
        #-----------------------------------------------------------------------------------------------------------------------------------------------
        #---------------------------------------------------LEVEL CONFIGURATION-------------------------------------------------------------------------
        #-----------------------------------------------------------------------------------------------------------------------------------------------
        self.num_level = 3
        
        #Scenes
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
            self.items.append(IMilk(-10,-6,55,0.75))
            self.items.append(IMilk(-6,-6,42,0.75))
            self.items.append(IMilk(-1,-6,30,0.75))
            self.items.append(ICheese(1,-6,53,0.75))
            self.items.append(IRice(5,-6,42,0.75))
            self.items.append(IFish(9,-6,30,0.75))
        
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
                self.items.append(IMilk(6,-6,51,0.75))
                self.items.append(IMilk(6,-6,40,0.75))
                self.items.append(IEgg(-11,-6,55,0.75))
                self.enemies.append(CDonu(17,-6,42))
        
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
                self.items.append(IMilk(-8,-6,45,0.75))
                self.items.append(IMilk(-4,-6,45,0.75))
                self.items.append(IMilk(0,-6,45,0.75))
                self.items.append(ICereal(4,-6,45,0.75))
                self.enemies.append(CDonu(15,-6,45))
                self.enemies.append(CDonu(18,-6,37))
        
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
                self.items.append(IMilk(-0,-6,51,0.75))
                self.items.append(IMilk(6,-6,41,0.75))
                self.items.append(IMilk(-6,-6,41,0.75))
                self.items.append(IRice(0,-6,46,0.75))
                self.items.append(ITomato(-8,-6,55,0.75))
        
        # Scene finished
        if self.scene4 == 1:
            if self.items == []:
                self.scene4 = 2
                self.moveOn()
        
        #------------------------------------------------------------------SCENE 5------------------------------------------------------------------
        # Appending items and enemies
        if (self.scene4 == 2) & (self.scene5 == 0):
            if self.movingBackground == False:
                self.scene5 = 1
                self.items.append(IMilk(6,-6,46,0.75))
                self.items.append(IMilk(1,-6,41,0.75))
                self.items.append(IMilk(-3,-6,43,0.75))
                self.items.append(IBanana(-7,-6,37,0.75))
                self.enemies.append(CDonu(19,-6,55))
                self.enemies.append(CHamburger(16,-6,37))
        
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