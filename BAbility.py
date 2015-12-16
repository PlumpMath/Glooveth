# Panda3D imports
from direct.gui.OnscreenImage import OnscreenImage
from pandac.PandaModules import TransparencyAttrib

# Project imports
from Bar import *

# Ability bar, it manages the amount of power of the specific ability
class BAbility (Bar):
    def __init__(self, power):
        Bar.__init__(self)
        
        #-----------------------------------------------------------------------------------------------------------------------------------------------
        #---------------------------------------------------VARIABLE DECLARATION------------------------------------------------------------------------
        #-----------------------------------------------------------------------------------------------------------------------------------------------
        self.amount = 0
        self.power = []
        
        #-----------------------------------------------------------------------------------------------------------------------------------------------
        #---------------------------------------------------------BAR INIT------------------------------------------------------------------------------
        #-----------------------------------------------------------------------------------------------------------------------------------------------
        if power == "GRAIN": 
            self.path = "./tex/ability_cereal_bar.png"
            self.path2 = "./tex/rice.png"
            self.path3 = "./tex/ability_cereal_amount.png"
            self.posX = -1.20
            self.posY = -0.85
        if power == "FRUIT": 
            self.path = "./tex/ability_fruit_bar.png"
            self.path2 = "./tex/straw.png"
            self.path3 = "./tex/ability_fruit_amount.png"
            self.posX = -1.08
            self.posY = -0.85
        if power == "MILK": 
            self.path = "./tex/ability_milk_bar.png"
            self.path2 = "./tex/milk.png"
            self.path3 = "./tex/ability_milk_amount.png"
            self.posX = -0.96
            self.posY = -0.85
        if power == "VEGETABLE": 
            self.path = "./tex/ability_vegetable_bar.png"
            self.path2 = "./tex/letuce.png"
            self.path3 = "./tex/ability_vegetable_amount.png"
            self.posX = -0.84
            self.posY = -0.85
        if power == "FISH": 
            self.path = "./tex/ability_fish_bar.png"
            self.path2 = "./tex/fish.png"
            self.path3 = "./tex/ability_fish_amount.png"
            self.posX = -0.72
            self.posY = -0.85
        
        # Initial sprite bar    
        self.bar = OnscreenImage(image=self.path, pos = (self.posX, 0, self.posY),hpr=None, scale = (0.05,1.0,0.035), color=None, parent=None, sort=1)
        self.bar.setTransparency(TransparencyAttrib.MAlpha)
        
        # Shape ability bar
        self.item = OnscreenImage(image=self.path2, pos = (self.posX, 0, -0.90),hpr=None, scale = 0.06, color=None, parent=None, sort=2)
        self.item.setTransparency(TransparencyAttrib.MAlpha)
        
        # It prepares sprites amount bar
        i=0
        while i<5:
            self.power.append(OnscreenImage(image=self.path3, pos = (self.posX, 0, self.posY+((i+1)*0.055)),hpr=None, scale = (0.05,1.0,0.025), color=None, parent=None, sort=1))
            self.power[i].setTransparency(TransparencyAttrib.MAlpha)
            self.power[i].hide()
            i=i+1
    #end __init__
    
    #-----------------------------------------------------------------------------------------------------------------------------------------------
    #----------------------------------------------------------------FUNCTIONS----------------------------------------------------------------------
    #-----------------------------------------------------------------------------------------------------------------------------------------------
    # It increases the amount of the bar
    def itemCollected(self,amnt):
        if      self.amount > 4: self.amount = 5
        else:   
            self.power[self.amount].show()
            self.amount = self.amount + amnt
    #end itemCollected
    
    # It decreases the amount of the bar
    def powerUsed(self,amnt):
        self.amount = self.amount - 1
        self.power[self.amount].hide();        
    #end powerUsed
    
    # It makes empty the bar
    def setEmpty(self):
        while self.amount > 0:
            self.amount = self.amount - 1
            self.power[self.amount].hide()
    #end setEmpty

    # It makes disappear the bar
    def hide(self):
        self.bar.hide()
        self.item.hide()
        
        i=0
        while i<5:
            self.power[i].hide()
            i=i+1
    #end hide
    
    # It makes that sprite have an intermitent alpha effect for 2 seconds
    def taskGlowing(self, task):
        if task.time > 2:
            self.bar.show()
            self.item.show()
            i=0
            while i<self.amount:
                self.power[i].show()
                i=i+1
            
            self.isVisible = True
            self.lastTime = 0.0
            return task.done
        else:
            if (task.time - self.lastTime) > 0.15:
                self.lastTime = task.time
                if self.isVisible == True:  
                    self.bar.hide()
                    self.item.hide()
                    i=0
                    while i<self.amount:
                        self.power[i].hide()
                        i=i+1
                
                    self.isVisible = False
                else:
                    self.bar.show()
                    self.item.show()
                    i=0
                    while i<self.amount:
                        self.power[i].show()
                        i=i+1
                        
                    self.isVisible = True
                
            return task.cont
    #end taskInvincible
 #end class BAbility
        