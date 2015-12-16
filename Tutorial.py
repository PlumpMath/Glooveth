# Panda3D imports
import direct.directbase.DirectStart
from direct.showbase import DirectObject
from direct.showbase.DirectObject import DirectObject
from direct.gui.OnscreenImage import OnscreenImage
from pandac.PandaModules import TransparencyAttrib

# Crayon3d imports
from Crayon3DScene import *
from wiimote_handler import *
from Crayon3DGesture import *

# Project imoprts
from CMain import *
from BEnergy import *
from BAbility import *
from Level_Tutorial import *
from Game import *

# It manages the tutorial of drawing shapes
class Tutorial (DirectObject):
    def __init__(self, background, cursor, pointer):
        #-----------------------------------------------------------------------------------------------------------------------------------------------
        #---------------------------------------------------VARIABLE DECLARATION------------------------------------------------------------------------
        #-----------------------------------------------------------------------------------------------------------------------------------------------
        # Background
        self.back = background
        
        # Level
        self.level = Level_Tutorial(background)
        
        # Graphic components
        #Blackboard
        self.blackboard = OnscreenImage(image="./tex/blackboard_empty.png", pos = (0, 0, 0),hpr=None, scale = (1.25,1.0,0.90), color=None, parent=None, sort=0)
        self.blackboard.setTransparency(TransparencyAttrib.MAlpha)
        self.blackboard.hide()
        #Main Character
        self.char = CMain(-18,-5,59)
        #Energy Bar
        self.energyBar = BEnergy()
        self.energyBar.increase(50)
        #Abilies Bar
        self.grainAbility = BAbility("GRAIN")
        self.fruitAbility = BAbility("FRUIT")
        self.milkAbility = BAbility("MILK")
        self.vegetableAbility = BAbility("VEGETABLE")
        self.fishAbility = BAbility("FISH")
        #Shape
        self.shape = OnscreenImage(image="./tex/cereal_ability_shape.png", pos = (-0.75, 0, 0),hpr=None, scale = 0.25, color=None, parent=None, sort=1)
        self.shape.setTransparency(TransparencyAttrib.MAlpha)
        self.shape.hide()
        #Item
        self.item = OnscreenImage(image="./tex/rice.png", pos = (-0.75, 0, -0.4),hpr=None, scale = 0.09, color=None, parent=None, sort=1)
        self.item.setTransparency(TransparencyAttrib.MAlpha)
        self.item.hide()
        #Texts
        self.text = OnscreenImage(image="./tex/tryToDrawThisShape.png", pos = (-0.75, 0, 0.6),hpr=None, scale = 0.35, color=None, parent=None, sort=1)
        self.text.setTransparency(TransparencyAttrib.MAlpha)
        self.text.hide()
        self.grassText = OnscreenImage(image="./tex/moveThroughTheGrass.png", pos = (0, 0, 0),hpr=None, scale = 0.7, color=None, parent=None, sort=1)
        self.grassText.setTransparency(TransparencyAttrib.MAlpha)
        #Info
        self.infError = OnscreenImage(image="./tex/wrong_attack.png", pos = (0.4, 0, 0),hpr=None, scale=(0.47,1.0,0.55), color=None, parent=None, sort=5)
        self.infError.setTransparency(TransparencyAttrib.MAlpha)
        self.infError.hide()
        self.infCereal = OnscreenImage(image="./tex/cereal_attack.png", pos = (0.4, 0, 0),hpr=None, scale=0.45, color=None, parent=None, sort=5)
        self.infCereal.setTransparency(TransparencyAttrib.MAlpha)
        self.infCereal.hide()
        self.infFish = OnscreenImage(image="./tex/fish_attack.png", pos = (0.4, 0, 0),hpr=None, scale=0.5, color=None, parent=None, sort=5)
        self.infFish.setTransparency(TransparencyAttrib.MAlpha)
        self.infFish.hide()
        self.infMilk = OnscreenImage(image="./tex/milk_attack.png", pos = (0.4, 0, 0),hpr=None, scale=0.5, color=None, parent=None, sort=5)
        self.infMilk.setTransparency(TransparencyAttrib.MAlpha)
        self.infMilk.hide()
        self.infVege = OnscreenImage(image="./tex/vege_attack.png", pos = (0.4, 0, 0),hpr=None, scale=0.4, color=None, parent=None, sort=5)
        self.infVege.setTransparency(TransparencyAttrib.MAlpha)
        self.infVege.hide()
        self.infFruit = OnscreenImage(image="./tex/fruit_attack.png", pos = (0.4, 0, 0),hpr=None, scale=0.4, color=None, parent=None, sort=5)
        self.infFruit.setTransparency(TransparencyAttrib.MAlpha)
        self.infFruit.hide()
        #Logo
        self.logo = OnscreenImage(image="./tex/laSalleAlpha.png", pos = (1.05, 0, -0.85),hpr=None, scale=(0.22,1.0,0.075), color=None, parent=None, sort=5)
        self.logo.setTransparency(TransparencyAttrib.MAlpha)
          
        # Others
        self.shapeNum = 0
        self.drawedOK = 0
        self.finished = False
        self.drawing = False
        self.readyForGame = False
        self.inGame = False
        self.busy = False
        
        #-----------------------------------------------------------------------------------------------------------------------------------------------
        #----------------------------------------------------------TUTORIAL INIT------------------------------------------------------------------------
        #-----------------------------------------------------------------------------------------------------------------------------------------------
        # Glove gestures configuration
        self.cursor = cursor
        self.gestureHandler = GestureRecognition("Gesture_Handler", 
                                                 [("1",0), ("2",0), ("3",0), ("4",0), ("6",0), ("7",0), ("8",0), ("9",0),                               #NONE
                                                  ("12",0), ("13",0), ("16",0), ("18",0), ("17",0), ("14",0),                                           #NONE
                                                  ("23",0), ("26",0), ("29",0), ("27",0), ("24",0), ("21",0),                                           #NONE
                                                  ("36",0), ("39",0), ("38",0), ("34",0), ("31",0), ("32",0),                                           #NONE
                                                  ("41",0), ("42",0), ("43",0), ("49",0), ("48",0), ("47",0),                                           #NONE
                                                  ("69",0), ("68",0), ("67",0), ("61",0), ("62",0), ("63",0),                                           #NONE
                                                  ("74",0), ("71",0), ("72",0), ("76",0), ("79",0), ("78",0),                                           #NONE
                                                  ("87",0), ("84",0), ("81",0), ("83",0), ("86",0), ("89",0),                                           #NONE
                                                  ("98",0), ("97",0), ("94",0), ("92",0), ("93",0), ("96",0),                                           #NONE
                                                  ("93934",1),                                                                                          #FRUIT
                                                  ("7624",2),                                                                                           #MILK
                                                  ("67616",3),                                                                                          #VEGETABLE
                                                  ("183",4),                                                                                            #FISH
                                                  ("3434",5)],                                                                                          #CEREAL
                                                 self.cursor, True, 1, 0, 0)
                                                 
        self.accept("Gesture_Handler", self.gestureProcessing)
        
        self.pointer = pointer
        
        # Events declaration
        self.accept("WM_BUTTON_PRESSED", self.handleBtnPress)
        self.accept("WM_BUTTON_RELEASED", self.handleBtnRelease)
        
        taskMgr.add(self.taskMove, 'taskMove')
        taskMgr.add(self.taskCollision, 'taskCollision' )
        taskMgr.add(self.taskTextGrass, 'taskTextGrass' )
    #end __init__
    
    #-----------------------------------------------------------------------------------------------------------------------------------------------
    #----------------------------------------------------------------FUNCTIONS----------------------------------------------------------------------
    #-----------------------------------------------------------------------------------------------------------------------------------------------
    # WiiMote button pressed handler
    def handleBtnPress(self, btn, dev, index):
        if( self.finished == False ):
            if(index == 1):
                if(btn == wiiuse.BUTTON_A):
                    if self.drawing == True: 
                        # We're on the second part of the tutorial
                        if( self.readyForGame == False ):
                            # We're ready for playing
                            if( self.inGame == False ): 
                                if( self.busy == False ):       self.gestureHandler.beginGesture()
    #end handleBrnPress
    
    # WiiMote button released handler
    def handleBtnRelease(self, btn, dev, index):
        if( self.finished == False ):
            if(index == 1):
                if(btn == wiiuse.BUTTON_A):
                    if self.drawing == True:
                        # We're on the second part of the tutorial      
                        if( self.readyForGame == True ):
                            # We're going to play the game
                            self.hide()
                            self.game = Game(self.back, self.cursor, self.pointer)
                            self.inGame = True
                            self.readyForGame = False
                        else:
                            #We're on the second part of the tutorial
                            if( self.inGame == False ): 
                                if( self.busy == False ):       self.gestureHandler.endGesture()
                    else:       
                        #We're on the first part of the tutorial
                        self.showBlackboard()
    #end handleBtnRelease
    
    # It makes appear the blackboard
    def showBlackboard(self):
        if self.level.scene2 == 2:
            self.grassText.hide()
            taskMgr.remove('taskMove')
            taskMgr.remove('taskGlowing6')
            self.energyBar.hide()
            self.blackboard.show()
            self.shape.show()
            self.item.show()
            self.text.show()
            self.drawing = True
    #end showBlackboard
    
    # It hides the tutorial application
    def hide(self):
        self.blackboard.hide()
        self.shape.hide()
        self.shape = None
        self.text.hide()
        self.text = None
        self.grassText.hide()
        self.grassText = None
        self.char.hide()
        taskMgr.remove('taskMove')
        self.char = None
        self.energyBar.hide()
        self.energyBar = None
        self.grainAbility.hide()
        self.grainAbility = None
        self.fruitAbility.hide()
        self.fruitAbility = None
        self.milkAbility.hide()
        self.milkAbility = None
        self.vegetableAbility.hide()
        self.vegetableAbility = None
        self.fishAbility.hide()
        self.fishAbility = None
        taskMgr.remove('taskCollision')
        self.level.removeItems()
        self.level = None
        self.item.hide()
        self.item = None
	#end hide
        
    # It identifies the shapes drawn.
    def gestureProcessing(self, id, x, y):
        if(self.inGame == False):
            #------------------------------------------------------------------FRUIT---------------------------------------------------------------------
            if id==1:
                if(self.shapeNum == 4):
                    self.infFruit.show()
                    self.drawedOK = self.drawedOK + 1
                    taskMgr.add( self.taskCorrect, 'taskCorrect' )
                else:
                    self.infError.show()
                    taskMgr.add( self.taskError, 'taskError' )
                   
            #------------------------------------------------------------------MILK----------------------------------------------------------------------
            elif id==2:
                if(self.shapeNum == 2):
                    self.infMilk.show()
                    self.drawedOK = self.drawedOK + 1
                    taskMgr.add( self.taskCorrect, 'taskCorrect' )           
                else:
                    self.infError.show()
                    taskMgr.add( self.taskError, 'taskError' )
            #---------------------------------------------------------------VEGETABLE-------------------------------------------------------------------
            elif id==3:
                if(self.shapeNum == 3):
                    self.infVege.show()
                    self.drawedOK = self.drawedOK + 1
                    taskMgr.add( self.taskCorrect, 'taskCorrect' )
                else:
                    self.infError.show()
                    taskMgr.add( self.taskError, 'taskError' )
               
           #------------------------------------------------------------------FISH---------------------------------------------------------------------
            elif id==4:
                if(self.shapeNum == 1):
                    self.infFish.show()
                    self.drawedOK = self.drawedOK + 1
                    taskMgr.add( self.taskCorrect, 'taskCorrect' )
                else:
                    self.infError.show()
                    taskMgr.add( self.taskError, 'taskError' )
                          
            #----------------------------------------------------------------CEREAL--------------------------------------------------------------------
            elif id==5:
                if(self.shapeNum == 0):
                    self.infCereal.show()
                    self.drawedOK = self.drawedOK + 1
                    taskMgr.add( self.taskCorrect, 'taskCorrect' )
                else:
                    self.infError.show()
                    taskMgr.add( self.taskError, 'taskError' )
                    
            #------------------------------------------------------------------NONE-------------------------------------------------------------------
            else:
                taskMgr.add( self.taskError, 'taskError' )
                self.infError.show()
          
            self.gestureHandler.clearGestures();
            self.busy = True
        
    #end gestureProcessing
    
    # It changes the shape showed to the user, depending on the shape practised.
    def changeShape(self):
        if( self.shapeNum == 0 ):       
            self.shape.setImage("./tex/cereal_ability_shape.png")
            self.item.setImage("./tex/rice.png")
            self.item.setTransparency(TransparencyAttrib.MAlpha)
        if( self.shapeNum == 1 ):       
            self.shape.setImage("./tex/fish_ability_shape.png")
            self.item.setImage("./tex/fish.png")
            self.item.setTransparency(TransparencyAttrib.MAlpha)
        if( self.shapeNum == 2 ):       
            self.shape.setImage("./tex/milk_ability_shape.png")
            self.item.setImage("./tex/milk.png")
            self.item.setTransparency(TransparencyAttrib.MAlpha)
        if( self.shapeNum == 3 ):       
            self.shape.setImage("./tex/vegetable_ability_shape.png")
            self.item.setImage("./tex/letuce.png")
            self.item.setTransparency(TransparencyAttrib.MAlpha)
        if( self.shapeNum == 4 ):       
            self.shape.setImage("./tex/fruit_ability_shape.png")
            self.item.setImage("./tex/straw.png")
            self.item.setTransparency(TransparencyAttrib.MAlpha)
        if( self.shapeNum == 5 ):
            self.shape.hide()
            self.text.setImage("./tex/youAreReady.png")
            self.text.setTransparency(TransparencyAttrib.MAlpha)
            self.item.hide()
    #end changeShape
    
    #-----------------------------------------------------------------------------------------------------------------------------------------------
    #----------------------------------------------------------------TASKS,THREADS------------------------------------------------------------------
    #-----------------------------------------------------------------------------------------------------------------------------------------------
    # It moves the main character to the sun pointer point.
    def taskMove(self, task):
        mpos = self.cursor.getCursorPos()
        
        # Moving the main character
        self.char.movement(mpos.getX(),mpos.getY())
        
        if self.level.scene2 == 1:
            self.grassText.setImage("./tex/PressAButton.png")
            self.grassText.setTransparency(TransparencyAttrib.MAlpha)
            self.grassText.show()
            self.level.scene2 = 2
            
        return task.cont
    #end taskCursor
    
    # It checks Character-Item collision
    def taskCollision(self, task):
        #Character-Item collision
        for x in self.level.items:
            if x.collide(self.char):
                self.char.itemCollect(x)
                self.level.items.remove(x)
                x.posX = -100
                x.model.setX(x.posX)
                x.posY = -100
                x.model.setZ(x.posY)
                x.collectIt = True
                
                self.energyBar.increase(x.energy)
                
                if x.specialItem==True: self.specialItems.itemCollected(x.type)
                
                # Producing glowing on abilities bar
                if x.type == "GRAIN":
                    self.grainAbility.itemCollected(1)
                    taskMgr.add(self.grainAbility.taskGlowing, 'taskGlowing1')
                    taskMgr.add(self.energyBar.taskGlowing, 'taskGlowing6')
                if x.type == "FRUIT":
                    self.fruitAbility.itemCollected(1)
                    taskMgr.add(self.fruitAbility.taskGlowing, 'taskGlowing2')
                    taskMgr.add(self.energyBar.taskGlowing, 'taskGlowing6')
                if x.type == "MILK":
                    self.milkAbility.itemCollected(1)
                    taskMgr.add(self.milkAbility.taskGlowing, 'taskGlowing3')
                    taskMgr.add(self.energyBar.taskGlowing, 'taskGlowing6')
                if x.type == "VEGETABLE":
                    self.vegetableAbility.itemCollected(1)
                    taskMgr.add(self.vegetableAbility.taskGlowing, 'taskGlowing4')
                    taskMgr.add(self.energyBar.taskGlowing, 'taskGlowing6')
                if x.type == "FISH":
                    self.fishAbility.itemCollected(1)
                    taskMgr.add(self.fishAbility.taskGlowing, 'taskGlowing5')
                    taskMgr.add(self.energyBar.taskGlowing, 'taskGlowing6')
                    
        return task.cont
    #end taskCollision
    
    # It manages the tutorial in order to teach all the shapes to the user.
    # Each shape is practised two times.
    def taskCorrect(self, task):
        if( task.time > 1 ):
            if(self.shapeNum == 0): self.infCereal.hide()
            if(self.shapeNum == 1): self.infFish.hide()
            if(self.shapeNum == 2): self.infMilk.hide()
            if(self.shapeNum == 3): self.infVege.hide()
            if(self.shapeNum == 4): self.infFruit.hide()
            
            self.busy = False
            self.text.setImage("./tex/onceAgain.png")
            self.text.setTransparency(TransparencyAttrib.MAlpha)
            if( self.drawedOK > 1 ):
                self.shapeNum = self.shapeNum + 1
                if( self.shapeNum == 5 ): self.readyForGame = True
                self.drawedOK = 0
                self.text.setImage("./tex/tryNewOne.png")
                self.text.setTransparency(TransparencyAttrib.MAlpha)
                self.changeShape()
                
            return task.done
        else:   return task.cont
    #end taskCursor
    
    # It shows a message of don't worry to the user.
    def taskError(self, task):
        if( task.time > 1 ):
            self.busy = False
            self.infError.hide()
            self.text.setImage("./tex/dontWorry.png")
            self.text.setTransparency(TransparencyAttrib.MAlpha)    
            return task.done
        else:   return task.cont
    #end taskCursor
    
    # It shows a determined text for 3 seconds.
    def taskTextGrass(self, task):
        if( task.time > 3):
            self.grassText.hide()
            return task.done
        else:   return task.cont
    #end taskTextGrass