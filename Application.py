# Panda3D imports
import direct.directbase.DirectStart
from direct.showbase import DirectObject
from direct.showbase.DirectObject import DirectObject
from direct.gui.OnscreenImage import OnscreenImage

# Crayon3d imports
from Crayon3DScene import *
from wiimote_handler import *
from Crayon3DGesture import *

# Project imports
from Game import *
from Menu import *
from Tutorial import *

# It manages the initial menu of the game
class Application (DirectObject):
    def __init__(self):        
        #-----------------------------------------------------------------------------------------------------------------------------------------------
        #---------------------------------------------------VARIABLE DECLARATION------------------------------------------------------------------------
        #-----------------------------------------------------------------------------------------------------------------------------------------------
        self.menu = None
        self.game = None
        self.ins = None
        self.creditsActivated = False
        
        #-----------------------------------------------------------------------------------------------------------------------------------------------
        #--------------------------------------------------------------APPLICATION INIT-----------------------------------------------------------------
        #-----------------------------------------------------------------------------------------------------------------------------------------------
        # Window configuration
        props = WindowProperties( )
        props.setTitle( 'Glooveth' )
        props.setIconFilename("./icon.ico")
        base.win.requestProperties( props ) 

        # World configuration
        base.disableMouse()
        self.accept("escape", self.quit)
        
        # Background
        self.background = Image()
        self.back = []
        self.back.append(self.background.loadModel("./models/Background.egg", "./tex/back.png", 34, 0, 60 , 56))
        self.back.append(self.background.loadModel("./models/Background.egg", "./tex/back2.png", 146, 0, 60 , 56))
        
        #Init Crayon3D
        self.wmHandler = WiimoteHandler()
        if(not self.wmHandler.start([WIIMOTE_TRACKER, WIIMOTE_BUTTON])):
            self.wmHandler = None

        self.cursor = Cursor(['tex/alpha_cursor.png'], self.wmHandler, 0)
        
        #Cursor init
        self.pointer = Pointer()
        
        #Events declaration
        self.accept("WM_BUTTON_RELEASED", self.handleBtnRelease)
        
        #Tasks
        taskMgr.add(self.taskCursor, 'taskCursor')
        
        self.menu = Menu(self.cursor)
    #end __init__
    
    #-----------------------------------------------------------------------------------------------------------------------------------------------
    #----------------------------------------------------------------FUNCTIONS----------------------------------------------------------------------
    #-----------------------------------------------------------------------------------------------------------------------------------------------
    # WiiMote button released handler
    def handleBtnRelease(self, btn, dev, index):
        if(index == 1):
            if(btn == wiiuse.BUTTON_A):
                self.selection()
    #end handleBtnRelease
    
    # It manages the selection on the menu
    def selection(self):
        if( self.menu.selected == "CREDITS" ):
            # Credits
            if( self.creditsActivated == False ):
                self.menu.hide()
                self.creditsImage = OnscreenImage(image="./tex/credits.png", pos = (0, 0, 0),hpr=None, scale = (1.33,1.0,1.0), color=None, parent=None, sort=3)
                self.creditsImage.setTransparency(TransparencyAttrib.MAlpha)
                self.creditsActivated = True
            else:
                self.creditsImage.hide()
                self.menu.show()
                self.creditsActivated = False
                        
        if( self.menu.selected == "PLAY" ):
            # Game
            self.menu.hide()
            self.game = Game(self.back, self.cursor, self.pointer)
            self.menu.selected = "HIDE"
            
        if( self.menu.selected == "INS" ):
            # Tutorial
            self.ins = Tutorial(self.back, self.cursor, self.pointer)
            self.menu.hide()
            self.menu.selected = "HIDE"
    #end selection
    
    # It prepares the application to be closed and quit the game
    def quit(self):
        # Stop the wiimote handler
        if(self.wmHandler):
            self.wmHandler.stop()
            
        print "Bye-bye!"
        sys.exit()
    #end quit
    
    #-----------------------------------------------------------------------------------------------------------------------------------------------
    #----------------------------------------------------------------TASKS,THREADS------------------------------------------------------------------
    #-----------------------------------------------------------------------------------------------------------------------------------------------
    # It moves the sun pointer according to the mouse or glove.
    def taskCursor(self, task):
        # It sets the sun pointer in Crayon3D cursor coordinates
        mpos = self.cursor.getCursorPos()
        if( self.game != None ):
            self.pointer.setPosX(mpos.getX()+self.game.distXPointDraw)
            self.pointer.setPosY(mpos.getY()+self.game.distYPointDraw)
        else:
            self.pointer.setPosX(mpos.getX())
            self.pointer.setPosY(mpos.getY())
        return task.cont
    #end taskCursor
    
    
#end class Application