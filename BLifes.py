# Panda3D imports
from direct.gui.OnscreenImage import OnscreenImage
from pandac.PandaModules import TransparencyAttrib

# Project imports
from Bar import *

# Lifes Bar, it manages the number of lifes of the character
class BLifes (Bar):
    def __init__(self):
        Bar.__init__(self)
        
        #-----------------------------------------------------------------------------------------------------------------------------------------------
        #---------------------------------------------------VARIABLE DECLARATION------------------------------------------------------------------------
        #-----------------------------------------------------------------------------------------------------------------------------------------------
        self.amount = 0
        self.lifes = []
        i=0
        
        # It prepares sprites amount bar
        while i<5:
            self.lifes.append(None)
            self.lifes.insert(i,OnscreenImage(image="./tex/life.png", pos = (-1.2+(i*0.20), 0, 0.75),hpr=None, scale = (0.08,1.0,0.075), color=None, parent=None, sort=1))
            self.lifes[i].setTransparency(TransparencyAttrib.MAlpha)
            self.lifes[i].hide()
            i = i+1      
    #end __init__
    
    #-----------------------------------------------------------------------------------------------------------------------------------------------
    #----------------------------------------------------------------FUNCTIONS----------------------------------------------------------------------
    #-----------------------------------------------------------------------------------------------------------------------------------------------
    # It increases the amount of the bar given
    def increase(self, amnt):
        if self.amount < 5:
            self.lifes[self.amount].show()
            self.amount = self.amount+1
    #end increase
    
    # It decreases the amount of the bar given
    def decrease(self, amnt):
        self.amount = self.amount-1
        self.lifes[self.amount].hide()
    #end decrease
    
    # It makes disappear the bar
    def hide(self):
        i=0
        while i<5:
            self.lifes[i].hide()
            i = i+1
    #end hide
    
    # It makes appear the bar
    def show(self):
        i=0
        while i<self.amount:
            self.lifes[i].show()
            i = i+1
    #end show