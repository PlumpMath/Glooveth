# Panda3D imports
from pandac.PandaModules import WindowProperties
import sys

# Crayon3d imports
from Crayon3DScene import *
from wiimote_handler import *
from Crayon3DGesture import *

# Project imports
from Level_1 import *
from Level_2 import *
from Level_3 import *
from Level_4 import *
from Level_5 import *
from Level_6 import *
from CMain import *
from Pointer import *
from BEnergy import *
from BLifes import *
from BSpecial import *
from BAbility import *
from Attack import *

# Game flow. Management through the items, enemies and character, controlled by the user.
class Game(DirectObject):
    def __init__(self, background, cursor, pointer):
        #-----------------------------------------------------------------------------------------------------------------------------------------------
        #---------------------------------------------------VARIABLE DECLARATION------------------------------------------------------------------------
        #-----------------------------------------------------------------------------------------------------------------------------------------------
        # Timers
        self.jumpTiming = 0
        self.jumpTime = 0
        self.lastTimeEnergy = 0
        self.energyTimer = None
        
        # Booleans
        self.jumping = False
        self.drawing = False
        self.attacking = False
        self.busy = False       #true if there are some image on screen making note something
        self.isGameOver = False
        
        # Auxiliar calculations
        self.vecX = 0
        self.vecY = 0
        
        # Graphic components
        #Blackboard
        self.blackboard = OnscreenImage(image="./tex/blackboard.png", pos = (0, 0, 0),hpr=None, scale = (1.25,1.0,0.90), color=None, parent=None, sort=0)
        self.blackboard.setTransparency(TransparencyAttrib.MAlpha)
        self.blackboard.hide()
        self.distXPointDraw = 0.0
        self.distYPointDraw = 0.0
        #Level
        self.level = Level_1(background)
        #Main Character
        self.char = CMain(-18,-5,59)
        #Energy Bar
        self.energyBar = BEnergy()
        self.energyBar.increase(50);
        #Life Bar
        self.lifes = BLifes()
        self.lifes.increase(1)
        self.lifes.increase(1)
        self.lifes.increase(1)
        #Special Items Bar
        self.specialItems = BSpecial()
        #Abilies Bar
        self.grainAbility = BAbility("GRAIN")
        self.fruitAbility = BAbility("FRUIT")
        self.milkAbility = BAbility("MILK")
        self.vegetableAbility = BAbility("VEGETABLE")
        self.fishAbility = BAbility("FISH")
        #Info
        self.infError = OnscreenImage(image="./tex/wrong_attack.png", pos = (0.4, 0, 0),hpr=None, scale=(0.47,1.0,0.55), color=None, parent=None, sort=5)
        self.infError.setTransparency(TransparencyAttrib.MAlpha)
        self.infError.hide()
        self.infCereal = OnscreenImage(image="./tex/cereal_attack.png", pos = (0.4, 0, 0),hpr=None, scale=0.45, color=None, parent=None, sort=5)
        self.infCereal.setTransparency(TransparencyAttrib.MAlpha)
        self.infCereal.hide()
        self.infCerealError = OnscreenImage(image="./tex/cereal_not_attack.png", pos = (0.4, 0, 0),hpr=None, scale=0.45, color=None, parent=None, sort=5)
        self.infCerealError.setTransparency(TransparencyAttrib.MAlpha)
        self.infCerealError.hide()
        self.infFish = OnscreenImage(image="./tex/fish_attack.png", pos = (0.4, 0, 0),hpr=None, scale=0.5, color=None, parent=None, sort=5)
        self.infFish.setTransparency(TransparencyAttrib.MAlpha)
        self.infFish.hide()
        self.infFishError = OnscreenImage(image="./tex/fish_not_attack.png", pos = (0.4, 0, 0),hpr=None, scale=0.5, color=None, parent=None, sort=5)
        self.infFishError.setTransparency(TransparencyAttrib.MAlpha)
        self.infFishError.hide()
        self.infMilk = OnscreenImage(image="./tex/milk_attack.png", pos = (0.4, 0, 0),hpr=None, scale=0.5, color=None, parent=None, sort=5)
        self.infMilk.setTransparency(TransparencyAttrib.MAlpha)
        self.infMilk.hide()
        self.infMilkError = OnscreenImage(image="./tex/milk_not_attack.png", pos = (0.4, 0, 0),hpr=None, scale=0.5, color=None, parent=None, sort=5)
        self.infMilkError.setTransparency(TransparencyAttrib.MAlpha)
        self.infMilkError.hide()
        self.infVege = OnscreenImage(image="./tex/vege_attack.png", pos = (0.4, 0, 0),hpr=None, scale=0.4, color=None, parent=None, sort=5)
        self.infVege.setTransparency(TransparencyAttrib.MAlpha)
        self.infVege.hide()
        self.infVegeError = OnscreenImage(image="./tex/vege_not_attack.png", pos = (0.4, 0, 0),hpr=None, scale=0.4, color=None, parent=None, sort=5)
        self.infVegeError.setTransparency(TransparencyAttrib.MAlpha)
        self.infVegeError.hide()
        self.infFruit = OnscreenImage(image="./tex/fruit_attack.png", pos = (0.4, 0, 0),hpr=None, scale=0.4, color=None, parent=None, sort=5)
        self.infFruit.setTransparency(TransparencyAttrib.MAlpha)
        self.infFruit.hide()
        self.infFruitError = OnscreenImage(image="./tex/fruit_not_attack.png", pos = (0.4, 0, 0),hpr=None, scale=0.4, color=None, parent=None, sort=5)
        self.infFruitError.setTransparency(TransparencyAttrib.MAlpha)
        self.infFruitError.hide()
        #Logo
        self.logo = OnscreenImage(image="./tex/laSalleAlpha.png", pos = (1.05, 0, -0.85),hpr=None, scale=(0.22,1.0,0.075), color=None, parent=None, sort=5)
        self.logo.setTransparency(TransparencyAttrib.MAlpha)
        
        # Sounds
        self.winMusic = base.loadMusic('./sound/win.wav')
        self.winMusic.setVolume(.5)
        self.winMusic.setLoopCount(1)
        self.gameOverMusic = base.loadMusic('./sound/lose.wav')
        self.gameOverMusic.setVolume(.5)
        self.gameOverMusic.setLoopCount(1)
        self.allSpecial = base.loadSfx('./sound/win_mysterious.wav')
        self.allSpecial.setVolume(.7)
        self.allSpecialPlayed = False
                        
        # Others
        self.type = "NONE"
        self.gameover = None
        self.gameActive = True
        
        #-----------------------------------------------------------------------------------------------------------------------------------------------
        #----------------------------------------------------------------GAME INIT----------------------------------------------------------------------
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
        
        # Cursor init
        self.pointer = pointer
        
        # Start tasks
        taskMgr.add(self.taskMove, 'taskMove')
        taskMgr.add(self.taskCollision, 'taskCollision' )
        taskMgr.add(self.taskEnergy, 'taskEnergy' )
        taskMgr.add(self.taskLevels, 'taskLevels')
    
        # Events declaration
        self.accept("WM_BUTTON_PRESSED", self.handleBtnPress)
        self.accept("WM_BUTTON_RELEASED", self.handleBtnRelease)
        
    #end __init__
        
    #-----------------------------------------------------------------------------------------------------------------------------------------------
    #----------------------------------------------------------------FUNCTIONS----------------------------------------------------------------------
    #-----------------------------------------------------------------------------------------------------------------------------------------------
    # Called when we start drawing, set ready the drawing interface  
    def showBlackboard(self):
        if self.char.attacking == False:
            # There isn't another character attack on course        
            if self.busy == False:
                # The screen is empty of sprites information, like abilty attacks
                self.drawing = True
                
                self.blackboard.show()
                self.specialItems.hide()
                self.char.walking = False
                self.energyBar.hide()
                self.lifes.hide()
                
                taskMgr.remove('taskMove')
                
                # Stop the enemies
                for x in self.level.enemies:
                    x.stopEnemy(True)
    #end showBlackboard
    
    # It hides the blackboard and makes appear the disappeared elements
    def hideBlackboard(self):
        self.drawing = False
        self.blackboard.hide()
        self.specialItems.show()
        self.char.walking = True
        self.energyBar.show()
        self.lifes.show()
        self.infError.hide()
        self.infCereal.hide()
        self.infCerealError.hide()
        self.infFish.hide()
        self.infFishError.hide()
        self.infMilk.hide()
        self.infMilkError.hide()
        self.infVege.hide()
        self.infVegeError.hide()
        self.infFruit.hide()
        self.infFruitError.hide()
    #end hideBlackboard
    
    # It stops drawing
    def stopAttack(self):
        if self.char.attacking == False:
            if self.busy == False:
                self.gestureHandler.endGesture()
    #end stopAttack
    
    # WiiMote button pressed handler
    def handleBtnPress(self, btn, dev, index):
        if(index == 1):
            if(btn == wiiuse.BUTTON_A):
                if(self.gameActive == True):
                    if self.drawing == True:        
                        if self.busy == False:  self.gestureHandler.beginGesture()
    #end handleBrnPress
    
    # WiiMote button released handler
    def handleBtnRelease(self, btn, dev, index):
        if(index == 1):
            if(btn == wiiuse.BUTTON_A):
                if(self.gameActive == True):
                    if self.drawing == True:        self.stopAttack()
                    else:                           self.showBlackboard()
    #end handleBtnRelease
    
    # Identify the information drawed on drawing process and if this is well drawed and we have enough ability power prepare's the attack.
    def gestureProcessing(self, id, x, y):
        if(self.gameActive == True):  
            #------------------------------------------------------------------FRUIT---------------------------------------------------------------------
            if id==1:
                if self.char.power[1] < 1:
                    self.infFruitError.show()
                else:
                    self.infFruit.show()
                    self.char.power[1] = self.char.power[1] - 1
                    self.fruitAbility.powerUsed(1);
                    self.attacking = True
                    self.type="FRUIT"
                    
            #------------------------------------------------------------------MILK----------------------------------------------------------------------
            elif id==2:
                if self.char.power[2] < 1:
                    self.infMilkError.show()
                else:
                    self.infMilk.show()
                    self.char.power[2] = self.char.power[2] - 1
                    self.milkAbility.powerUsed(1);
                    self.attacking = True
                    self.type="MILK"
            
            #---------------------------------------------------------------VEGETABLE-------------------------------------------------------------------
            elif id==3:
                if self.char.power[3] < 1:
                    self.infVegeError.show()
                else:
                    self.infVege.show()
                    self.char.power[3] = self.char.power[3] - 1
                    self.vegetableAbility.powerUsed(1);
                    self.attacking = True
                    self.type="VEGETABLE"
                    
            #------------------------------------------------------------------FISH---------------------------------------------------------------------
            elif id==4:
                if self.char.power[4] < 1:
                    self.infFishError.show()
                else:
                    self.infFish.show()
                    self.char.power[4] = self.char.power[4] - 1
                    self.fishAbility.powerUsed(1);
                    self.attacking = True
                    self.type="FISH"
                    
            #----------------------------------------------------------------CEREAL--------------------------------------------------------------------
            elif id==5:
                if self.char.power[0] < 1:
                   self.infCerealError.show() 
                else:
                    self.infCereal.show()
                    self.char.power[0] = self.char.power[0] - 1
                    self.grainAbility.powerUsed(1);
                    self.attacking = True
                    self.type="GRAIN"
                    
            #------------------------------------------------------------------NONE-------------------------------------------------------------------
            else:
                self.infError.show()
            
            #Shows on the screen the result of the drawing process
            taskMgr.add(self.taskSpriteAttack, 'taskSpriteAttack' )
            self.busy = True
            self.gestureHandler.clearGestures();
    #end gestureProcessing
    
    # Process the damage for the character
    def damage(self):
            self.char.life = self.char.life - 1
            if self.char.life >= 0:
                    self.char.soundDamage.play()
                    self.lifes.decrease(1)
                    self.char.setInvincible(True)
                    if self.char.life <= 0:
                            self.setGameOver()
    #end damage
    
    # Configures the game for Game Over process
    def setGameOver(self):
        self.gameover = OnscreenImage(image="./tex/gameover.png", pos = (0, 0, 0),hpr=None, scale = (1.4,1.0,1.0), color=None, parent=None, sort=30)
        self.isGameOver = True
        self.gameOverMusic.play()
        self.level.state = 2
        self.level.removeAll()
        taskMgr.remove('taskLevel')
        taskMgr.remove('taskLevels')
        taskMgr.remove('taskMove')
        taskMgr.add(self.taskChangeLevel, 'taskChangeLevel')
        self.energyBar.hide()
        self.specialItems.hide()
        self.grainAbility.hide()
        self.fruitAbility.hide()
        self.milkAbility.hide()
        self.vegetableAbility.hide()
        self.fishAbility.hide()
        self.lifes.hide()
    #end setGameOver
    
    #-----------------------------------------------------------------------------------------------------------------------------------------------
    #----------------------------------------------------------------TASKS,THREADS------------------------------------------------------------------
    #-----------------------------------------------------------------------------------------------------------------------------------------------
    # It moves the main character to the sun pointer point.
    def taskMove(self, task):
        mpos = self.cursor.getCursorPos()
        if(self.drawing == False):
            # We're not drawing.
            if(self.level.movingBackground != False):
                # We're on a transition sequence
                self.level.moveBackground(mpos.getX(),mpos.getY())
        
            # Moving the main character
            self.char.movement(mpos.getX(),mpos.getY())
        
        # We have all special items
        if( (self.specialItems.hasAllSpecial() == True) and (self.allSpecialPlayed == False) ):
            self.allSpecial.play()
            self.allSpecialPlayed = True
            self.lifes.increase(1)
            self.char.life = self.char.life + 1
        
        # We're run out of energy
        if self.energyBar.amount <= 0:
            self.setGameOver()
            
        return task.cont
    #end taskCursor
    
    # It holds ability's information on screen for 1 second and then throws the attack to the enemy.
    def taskSpriteAttack(self, task):
        if task.time>1:            
            # Making disappear the sprite information attack
            self.hideBlackboard()
            
            if self.attacking == True:
                # If we draw correctly and we have the correct power item
                self.att = Attack(self.type,"-",self.level.enemies,self.char)
                self.attacking = False
                self.char.attacking = True
                
            self.busy = False
            
            # Making move the enemies again
            for x in self.level.enemies:
                x.stopEnemy(False)
            
            # Making move the character again
            taskMgr.add(self.taskMove, 'taskMove')
            return task.done
        else:
            return task.cont
    #end taskAttack
    
    # It checks Character-Item, Character-Enemy, Character-Enemy Attack and Enemy-Character Attack collision every frame.
    def taskCollision(self, task):
        if self.isGameOver == True: return task.done
        else:
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
                    
                    #Abilites bar
                    if x.type == "GRAIN":
                        self.grainAbility.itemCollected(1)
                    if x.type == "FRUIT":
                        self.fruitAbility.itemCollected(1)
                    if x.type == "MILK":
                        self.milkAbility.itemCollected(1)
                    if x.type == "VEGETABLE":
                        self.vegetableAbility.itemCollected(1)
                    if x.type == "FISH":
                        self.fishAbility.itemCollected(1)
            
            #Character-Enemy collision, Character-Enemy Attack collision
            for x in self.level.enemies:
                if x.collide(self.char):
                    if self.char.isInvincible == False:
                        self.damage()
                                
                if x.attacking == True:
                    if x.att.char_enAttCollide(self.char):
                        if self.char.isInvincible == True:
                            if x.att.isexploding == False:
                                x.att.destroyAttack()
                        else:
                            if( x.att != None ):
                                x.att.explode()
                            self.damage()
                                
            #Enemy-Character Attack collision
            if self.char.attacking == True:
                for x in self.level.enemies:
                    if self.att.en_charAttCollide(x)==True:
                        x.life = x.life - 1
                        self.level.enemies.remove(x)
                        self.att.destroyAttack()
           
            return task.cont
    #end taskCollision
    
    # It decreases character energy every frame, only when he's moving over the screen.
    def taskEnergy(self, task):
        if self.isGameOver == True: 
            return task.done
        else:
            if self.char.walking:
                if (task.time-self.lastTimeEnergy) > 1: 
                    self.lastTimeEnergy = task.time
                    self.energyBar.decrease(3)
            else:
                if (task.time-self.lastTimeEnergy) > 1: 
                    self.lastTimeEnergy = task.time
                    self.energyBar.decrease(1)
            return task.cont
    #end taskEnergy
    
    # It waits for a level finalization (YOU WIN) and prepares the application for the next level
    def taskLevels(self, task):
        if self.level.state == 1:
            taskMgr.add(self.taskChangeLevel, 'taskChangeLevel')
            self.winMusic.play()
            self.level.state = 2
        return task.cont
    #end taskLevels
    
    # It change the level.
    # The next level if the user has won the game or a reinit if it is a game over.
    def taskChangeLevel(self, task):
        if(task.time > 4.0):
            if( self.isGameOver == True ):      self.gameover.hide()
            else:                               self.level.hideLevel()
            
            back = self.level.back
            
            if( self.isGameOver == True ):      num_level = 0
            else:                               num_level = self.level.num_level
            
            self.level = None
            
            self.grainAbility.setEmpty()
            self.fruitAbility.setEmpty()
            self.milkAbility.setEmpty()
            self.vegetableAbility.setEmpty()
            self.fishAbility.setEmpty()
            
            self.char.power[0] = 0
            self.char.power[1] = 0
            self.char.power[2] = 0
            self.char.power[3] = 0
            self.char.power[4] = 0
            
            if( self.isGameOver == False ): self.specialItems.reInit()
            self.allSpecialPlayed = False
            
            if(num_level == 0):
                self.char.model.hide()
                self.gameActive = False
                Game(back,self.cursor,self.pointer)
            if(num_level == 1): self.level = Level_2(back)
            if(num_level == 2): self.level = Level_3(back)
            if(num_level == 3): self.level = Level_4(back)
            if(num_level == 4): self.level = Level_5(back)
            if(num_level == 5): self.level = Level_6(back)

            return task.done
        else:
            return task.cont
    #end taskChangeLevel