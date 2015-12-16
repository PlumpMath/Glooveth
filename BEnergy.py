# Panda3D imports
from direct.gui.OnscreenImage import OnscreenImage
from pandac.PandaModules import TransparencyAttrib

# Project imports
from Bar import *

# Energy Bar, it manages the amount of energy of the character
class BEnergy (Bar):
    def __init__(self):
        Bar.__init__(self)
        
        #-----------------------------------------------------------------------------------------------------------------------------------------------
        #---------------------------------------------------VARIABLE DECLARATION------------------------------------------------------------------------
        #-----------------------------------------------------------------------------------------------------------------------------------------------
        self.amount = 0
        self.tmpAmount = 0
        
        # Background bar
        self.bar = OnscreenImage(image="./tex/energy_bar.png", pos = (-0.74, 0, 0.90),hpr=None, scale = (0.59,1.0,0.09), color=None, parent=None, sort=1)
        self.bar.setTransparency(TransparencyAttrib.MAlpha)
        
        # Energy spites
        self.energyBar = [];
        
        # It prepares sprites amount bar
        i = 0
        while(i<40):
            self.energyBar.append(None)
            self.energyBar.insert(i,OnscreenImage(image="./tex/energy/"+str(i+1)+".png", pos = (-1.27+((i*5)*0.0053), 0, 0.92),hpr=None, scale = (0.01,1.0,0.03), color=None, parent=None, sort=2))
            self.energyBar[i].setTransparency(TransparencyAttrib.MAlpha)
            self.energyBar[i].hide()
            i = i+1
            
    #end __init__
    
    #-----------------------------------------------------------------------------------------------------------------------------------------------
    #----------------------------------------------------------------FUNCTIONS----------------------------------------------------------------------
    #-----------------------------------------------------------------------------------------------------------------------------------------------
    # It increases the amount of the bar given
    def increase(self, amnt):
        finalAmount = self.amount+amnt
        if finalAmount <= 200:
            while( self.amount<finalAmount ):
                self.energyBar[self.amount/5].show()
                self.amount = self.amount + 5
    #end increase
    
    # It decreases the amount of the bar given
    def decrease(self, amnt):
        if amnt<5:
            self.tmpAmount = self.tmpAmount + amnt
            if self.tmpAmount >= 5:
                num = (self.amount-5)/5
                self.energyBar[num].hide();
                self.amount = self.amount - 5
                self.tmpAmount = 0
                
        else:
            if self.amount>0:
                initAmount = self.amount
                while( self.amount>(initAmount-amnt) ):
                    num = (self.amount-5)/5
                    if num>=0:
                        self.energyBar[num].hide();
                    self.amount = self.amount - 5 
    #end decrease
    
    # It makes disappear the bar
    def hide(self):
        self.bar.hide()
        
        i = 0
        while(i<40):
            self.energyBar[i].hide()
            i = i+1
    #end hide
    
    # It makes appear the bar
    def show(self):
        self.bar.show()
        
        i = 0
        while(i<(self.amount/5)):
            self.energyBar[i].show()
            i = i+1
    #end show
    
    # It makes that sprite have an intermitent alpha effect for 2 seconds
    def taskGlowing(self, task):
        if task.time > 2:
            self.bar.show()
            i = 0
            while(i<(self.amount/5)):
                self.energyBar[i].show()
                i = i+1
            
            self.isVisible = True
            self.lastTime = 0.0
            return task.done
        else:
            if (task.time - self.lastTime) > 0.15:
                self.lastTime = task.time
                if self.isVisible == True:  
                    self.bar.hide()
                    i = 0
                    while(i<(self.amount/5)):
                        self.energyBar[i].hide()
                        i = i+1
                
                    self.isVisible = False
                else:
                    self.bar.show()
                    i = 0
                    while(i<(self.amount/5)):
                        self.energyBar[i].show()
                        i = i+1
                        
                    self.isVisible = True
                
            return task.cont
    #end taskInvincible