# Panda3D imports
from direct.gui.OnscreenImage import OnscreenImage
from pandac.PandaModules import TransparencyAttrib

# Project imports
from Bar import *

# Special Items Bar, it manages and show on screen the special items collected by the character
class BSpecial (Bar):
    def __init__(self):
        Bar.__init__(self)
        
        #-----------------------------------------------------------------------------------------------------------------------------------------------
        #---------------------------------------------------VARIABLE DECLARATION------------------------------------------------------------------------
        #-----------------------------------------------------------------------------------------------------------------------------------------------
        # Init the bar with alpha sprites
        self.cereal = False
        self.specialCereal = OnscreenImage(image="./tex/cereal_not_special.png", pos = (0.43, 0, 0.87),hpr=None, scale = 0.11, color=None, parent=None, sort=1)
        self.specialCereal.setTransparency(TransparencyAttrib.MAlpha)
        
        self.banana = False
        self.specialBanana = OnscreenImage(image="./tex/banana_not_special.png", pos = (0.63, 0, 0.87),hpr=None, scale = 0.11, color=None, parent=None, sort=1)
        self.specialBanana.setTransparency(TransparencyAttrib.MAlpha)
        
        self.cheese = False
        self.specialCheese = OnscreenImage(image="./tex/cheese_not_special.png", pos = (0.83, 0, 0.87),hpr=None, scale = 0.11, color=None, parent=None, sort=1)
        self.specialCheese.setTransparency(TransparencyAttrib.MAlpha)
        
        self.tomato = False
        self.specialTomato = OnscreenImage(image="./tex/tomato_not_special.png", pos = (1.03, 0, 0.87),hpr=None, scale = 0.11, color=None, parent=None, sort=1)
        self.specialTomato.setTransparency(TransparencyAttrib.MAlpha)
        
        self.egg = False
        self.specialEgg= OnscreenImage(image="./tex/egg_not_special.png", pos = (1.23, 0, 0.87),hpr=None, scale = 0.11, color=None, parent=None, sort=1)
        self.specialEgg.setTransparency(TransparencyAttrib.MAlpha)
        
    #end __init__
    
    #-----------------------------------------------------------------------------------------------------------------------------------------------
    #----------------------------------------------------------------FUNCTIONS----------------------------------------------------------------------
    #-----------------------------------------------------------------------------------------------------------------------------------------------
    # It makes visible (change alpha sprite) the item corresponding to the type given
    def itemCollected(self,type):
        if type == "GRAIN":
            self.cereal = True
            self.specialCereal.setImage("./tex/cereal_special.png")
            self.specialCereal.setTransparency(TransparencyAttrib.MAlpha)
        if type == "FRUIT":
            self.banana = True
            self.specialBanana.setImage("./tex/banana_special.png")
            self.specialBanana.setTransparency(TransparencyAttrib.MAlpha)
        if type == "MILK":
            self.cheese = True
            self.specialCheese.setImage("./tex/cheese_special.png")
            self.specialCheese.setTransparency(TransparencyAttrib.MAlpha)
        if type == "VEGETABLE":
            self.tomato = True
            self.specialTomato.setImage("./tex/tomato_special.png")
            self.specialTomato.setTransparency(TransparencyAttrib.MAlpha)
        if type == "FISH":
            self.egg = True
            self.specialEgg.setImage("./tex/egg_special.png")
            self.specialEgg.setTransparency(TransparencyAttrib.MAlpha)
    #end itemCollected
    
    # It puts the bar at the same characteristics as its initialization
    def reInit(self):
        self.cereal = False
        self.specialCereal.setImage("./tex/cereal_not_special.png")
        self.specialCereal.setTransparency(TransparencyAttrib.MAlpha)
        
        self.banana = False
        self.specialBanana.setImage("./tex/banana_not_special.png")
        self.specialBanana.setTransparency(TransparencyAttrib.MAlpha)
        
        self.cheese = False
        self.specialCheese.setImage("./tex/cheese_not_special.png")
        self.specialCheese.setTransparency(TransparencyAttrib.MAlpha)
        
        self.tomato = False
        self.specialTomato.setImage("./tex/tomato_not_special.png")
        self.specialTomato.setTransparency(TransparencyAttrib.MAlpha)
        
        self.egg = False
        self.specialEgg.setImage("./tex/egg_not_special.png")
        self.specialEgg.setTransparency(TransparencyAttrib.MAlpha)
    #end reInit
    
    # It check if all the special items are collected.
    # Return true if it's correct.
    def hasAllSpecial(self):
        if( (self.cereal == True) and (self.banana == True) and (self.cheese == True) and (self.tomato == True) and (self.egg == True) ):
            return True
        else:
            return False
    #end hasAllSpecial
    
    # It makes disappear the bar
    def hide(self):
        self.specialCereal.hide()
        self.specialBanana.hide()
        self.specialCheese.hide()
        self.specialTomato.hide()
        self.specialEgg.hide()
    #end hide
    
    # It makes appear the bar
    def show(self):
        self.specialCereal.show()
        self.specialBanana.show()
        self.specialCheese.show()
        self.specialTomato.show()
        self.specialEgg.show()
    #end show
            