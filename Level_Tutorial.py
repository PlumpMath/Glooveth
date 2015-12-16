#Project imports
from Level import *

#Level 1
class Level_Tutorial(Level):
    def __init__(self, background):
        Level.__init__(self, background)
        #-----------------------------------------------------------------------------------------------------------------------------------------------
        #---------------------------------------------------LEVEL CONFIGURATION-------------------------------------------------------------------------
        #-----------------------------------------------------------------------------------------------------------------------------------------------
        self.num_level = 0
        
        #Scenes
        self.scene1 = 0
        self.scene2 = 0
    #end __init__
    
    def taskLevel(self, task):
        #------------------------------------------------------------------SCENE 1------------------------------------------------------------------
        #Append items
        if self.scene1 == 0:
            self.scene1 = 1
            self.items.append(IRice(-12,-6,40,0.75))
            self.items.append(IFish(-6,-6,40,0.75))
            self.items.append(IMilk(0,-6,40,0.75))
            self.items.append(ILetuce(6,-6,40,0.75))
            self.items.append(IStrawberry(12,-6,40,0.75))
        
        if self.scene1 == 1:
            if self.items == []:
                self.scene1 = 2
        
        #------------------------------------------------------------------SCENE 2------------------------------------------------------------------
        #Append items and enemies
        if (self.scene1 == 2) & (self.scene2 == 0):
            self.scene2 = 1
            
        return task.cont
    #end taskLevel
    