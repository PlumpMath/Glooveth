# Panda3D imports
import direct.directbase.DirectStart
from direct.showbase import DirectObject
from direct.showbase.DirectObject import DirectObject
from pandac.PandaModules import TextureStage
from direct.actor.Actor import Actor

# Load all the models of the game
class Image (DirectObject):
    def __init__(self):        
        pass       
    #end __init__
    
    #-----------------------------------------------------------------------------------------------------------------------------------------------
    #----------------------------------------------------------------FUNCTIONS----------------------------------------------------------------------
    #-----------------------------------------------------------------------------------------------------------------------------------------------
    # It takes an .egg file and put a texture on it.
    # It returns the model.
    def loadModel(self, modelPath, texturePath, x, y, depth, scale):
        obj = Actor(modelPath)
        obj.reparentTo(camera)             
        
        obj.setPos(x,depth,y) 
        obj.setScale(scale)                
                                          
        obj.setTransparency(1) 
        
        tex = loader.loadTexture(texturePath)
        obj.setTexture(tex, 1)
        
        return obj
    #end loadModel
    
#end class Image