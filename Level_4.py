# Project imports
from Level import *

# Level 4
class Level_4(Level):
    def __init__(self, background):
        Level.__init__(self, background)
        #-----------------------------------------------------------------------------------------------------------------------------------------------
        #---------------------------------------------------LEVEL CONFIGURATION-------------------------------------------------------------------------
        #-----------------------------------------------------------------------------------------------------------------------------------------------
        self.num_level = 4
        
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
            self.items.append(ILetuce(-2,-6,52,0.75))
            self.items.append(ILetuce(2,-6,52,0.75))
            self.items.append(ILetuce(-10,-6,45,0.75))
            self.items.append(ITomato(10,-6,45,0.75))
            self.items.append(IFish(2,-6,37,0.75))
            self.items.append(IMilk(-2,-6,37,0.75))
        
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
                self.items.append(ILetuce(10,-6,51,0.75))
                self.items.append(ILetuce(6,-6,45,0.75))
                self.items.append(ICereal(2,-6,41,0.75))
                self.enemies.append(CPotatoes(16,-6,42))
                self.enemies.append(CCan(21,-6,42))
        
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
                self.items.append(ILetuce(-11,-6,53,0.75))
                self.items.append(ILetuce(-11,-6,50,0.75))
                self.items.append(ICheese(-11,-6,44,0.75))
                self.items.append(IMilk(-11,-6,39,0.75))
                self.enemies.append(CCan(15,-6,55))
                self.enemies.append(CCan(17,-6,40))
        
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
                self.items.append(ILetuce(-11,-6,45,0.75))
                self.items.append(ILetuce(-1,-6,45,0.75))
                self.items.append(ILetuce(9,-6,45,0.75))
                self.items.append(IRice(0,-6,55,0.75))
                self.items.append(IEgg(0,-6,37,0.75))
        
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
                self.items.append(ILetuce(0,-6,55,0.75))
                self.items.append(ILetuce(0,-6,47,0.75))
                self.items.append(ILetuce(0,-6,42,0.75))
                self.items.append(IBanana(0,-6,37,0.75))
                self.enemies.append(CHamburger(15,-6,45))
                self.enemies.append(CPotatoes(19,-6,45))
                self.enemies.append(CCan(23,-6,45))
        
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