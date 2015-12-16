# Python imports
import math

#P anda3D imports
import direct.directbase.DirectStart
from direct.showbase import DirectObject
from direct.showbase.DirectObject import DirectObject
from direct.gui.OnscreenImage import OnscreenImage
from pandac.PandaModules import TransparencyAttrib

# It manages the initial menu of the game
class Menu (DirectObject):
    def __init__(self, cursor):        
        #-----------------------------------------------------------------------------------------------------------------------------------------------
        #---------------------------------------------------VARIABLE DECLARATION------------------------------------------------------------------------
        #-----------------------------------------------------------------------------------------------------------------------------------------------
        self.title = None
        self.play = None
        self.credits = None
        self.ins = None
        self.selected = "PLAY"
        
        self.pastTime = 0.0
        self.oldX = 0.0
        self.run = True
        self.moved = 0.0
        
        #-----------------------------------------------------------------------------------------------------------------------------------------------
        #----------------------------------------------------------------MENU INIT----------------------------------------------------------------------
        #-----------------------------------------------------------------------------------------------------------------------------------------------
        self.title = OnscreenImage("./tex/menu/glooveth.png", (0, 0, -0.25), None, (1.0,1.0,0.25), None, None, 10)
        self.title.setTransparency(TransparencyAttrib.MAlpha)
        
        self.credits = OnscreenImage("./tex/menu/credits.png", (-1.0, 0, -0.75), None, (0.25,1.0,0.125), None, None, 10)
        self.credits.setTransparency(TransparencyAttrib.MAlpha)
        
        self.ins = OnscreenImage("./tex/menu/ins.png", (1.0, 0, -0.75), None, (0.25,1.0,0.125), None, None, 10)
        self.ins.setTransparency(TransparencyAttrib.MAlpha)
        
        self.play = OnscreenImage("./tex/menu/playOver.png", (0, 0, -0.75), None, (0.35,1.0,0.20), None, None, 10)
        self.play.setTransparency(TransparencyAttrib.MAlpha)
        
        # Cursor
        self.cursor = cursor
        
        # Start tasks
        taskMgr.add(self.taskMenuMovement, 'taskMenuMovement')
    #end __init__
    
    #-----------------------------------------------------------------------------------------------------------------------------------------------
    #----------------------------------------------------------------FUNCTIONS----------------------------------------------------------------------
    #-----------------------------------------------------------------------------------------------------------------------------------------------    
    # It hides the main menu of the game
    def hide(self):
        self.title.hide()
        self.play.hide()
        self.credits.hide()
        self.ins.hide()
        self.run = False
    #end hide
    
    # It shows the main menu of the game
    def show(self):
        self.title.show()
        self.play.show()
        self.credits.show()
        self.ins.show()
        taskMgr.add( self.taskMenuMovement, 'taskMenuMovement' )
        self.run = True
    #end show
    
    #-----------------------------------------------------------------------------------------------------------------------------------------------
    #----------------------------------------------------------------TASKS,THREADS------------------------------------------------------------------
    #-----------------------------------------------------------------------------------------------------------------------------------------------
    # Menu interaction
    def taskMenuMovement(self, task):
        if( self.run == True ):
            mpos = self.cursor.getCursorPos()
            
            if( (mpos.getX() < -0.33) and (self.oldX >= -0.33 ) ):      self.selected = "CREDITS"
            elif( (mpos.getX() > -0.33) and (self.oldX <= -0.33) ):     self.selected = "PLAY"
            elif( (mpos.getX() < 0.33) and (self.oldX >= 0.33) ):       self.selected = "PLAY"                 
            elif( (mpos.getX() > 0.33) and (self.oldX <= 0.33) ):       self.selected = "INS"
            
            # Making bigger the button selected depending on the region of the cursor
            if( self.selected == "PLAY" ):
                self.play.setImage("./tex/menu/playOver.png")
                self.play.setTransparency(TransparencyAttrib.MAlpha)
                self.play.setScale((0.35,1.0,0.20))
            elif( self.selected == "CREDITS" ):
                self.credits.setImage("./tex/menu/creditsOver.png")
                self.credits.setTransparency(TransparencyAttrib.MAlpha)
                self.credits.setScale((0.35,1.0,0.20))
            elif( self.selected == "INS" ):
                self.ins.setImage("./tex/menu/insOver.png")
                self.ins.setTransparency(TransparencyAttrib.MAlpha)
                self.ins.setScale((0.35,1.0,0.20))
                
            self.oldX = mpos.getX()
            
            # Setting the others to a smaller size
            if( self.selected == "PLAY" ):
                self.credits.setImage("./tex/menu/credits.png")
                self.credits.setTransparency(TransparencyAttrib.MAlpha)
                self.credits.setScale((0.25,1.0,0.125))
                
                self.ins.setImage("./tex/menu/ins.png")
                self.ins.setTransparency(TransparencyAttrib.MAlpha)
                self.ins.setScale((0.25,1.0,0.125))
            elif( self.selected == "CREDITS" ):
                self.play.setImage("./tex/menu/play.png")
                self.play.setTransparency(TransparencyAttrib.MAlpha)
                self.play.setScale((0.25,1.0,0.125))
                
                self.ins.setImage("./tex/menu/ins.png")
                self.ins.setTransparency(TransparencyAttrib.MAlpha)
                self.ins.setScale((0.25,1.0,0.125))
            elif( self.selected == "INS" ):
                self.play.setImage("./tex/menu/play.png")
                self.play.setTransparency(TransparencyAttrib.MAlpha)
                self.play.setScale((0.25,1.0,0.125))
                
                self.credits.setImage("./tex/menu/credits.png")
                self.credits.setTransparency(TransparencyAttrib.MAlpha)
                self.credits.setScale((0.25,1.0,0.125))
            
            return task.cont
        else:   return task.done
    #end taskMenuMovement
        
#end class Menu