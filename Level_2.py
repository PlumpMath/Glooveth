# Project imports
from Level import *

# Level 2
class Level_2(Level):
    def __init__(self, background):
        Level.__init__(self, background)
        #-----------------------------------------------------------------------------------------------------------------------------------------------
        #---------------------------------------------------LEVEL CONFIGURATION-------------------------------------------------------------------------
        #-----------------------------------------------------------------------------------------------------------------------------------------------
        self.num_level = 2
        
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
            self.items.append(IFish(-11,-6,45,0.75))
            self.items.append(IFish(-3,-6,33,0.75))
            self.items.append(IFish(5,-6,45,0.75))
            self.items.append(IEgg(8.5,-6,33,0.75))
        
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
                self.items.append(IFish(-2,-6,40,0.75))
                self.items.append(ICereal(3,-6,55,0.75))
                self.enemies.append(CPotatoes(16,-6,37))
        
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
                self.items.append(IFish(-10,-6,45,0.75))
                self.items.append(IFish(-5,-6,45,0.75))
                self.items.append(IRice(1,-6,45,0.75))
                self.items.append(ICheese(9,-6,45,0.75))
                self.enemies.append(CHamburger(16,-6,55))
        
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
                self.items.append(IFish(-11,-6,55,0.75))
                self.items.append(IFish(-6,-6,48.75,0.75))
                self.items.append(IBanana(-1,-6,45.5,0.75))
                self.items.append(IFish(4,-6,36.25,0.75))
                self.items.append(IFish(9,-6,30,0.75))
                
        
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
                self.items.append(IFish(-5,-6,38,0.75))
                self.items.append(IFish(-1,-6,50,0.75))
                self.items.append(ITomato(7,-6,45,0.75))
                self.enemies.append(CPotatoes(16,-6,40))
                self.enemies.append(CHamburger(20,-6,55))
        
        # Scene finished
        if (self.scene5 == 1)&(self.state==0):
            if self.enemies == []:
                #Game won
                self.win = OnscreenImage(image="./tex/win.png", pos = (0, 0, 0),hpr=None, scale = (1.4,1.0,1.0), color=None, parent=None, sort=30)
                self.state = 1
                self.removeItems()
                    
                taskMgr.remove('taskLevel')
                
        return task.cont 
    #end taskLevel
    