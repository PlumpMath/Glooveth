# Python imports
from math import sqrt

# Generic item class that manage the interaction with items
class Item:
	def __init__(self, x, y, z):
		#-----------------------------------------------------------------------------------------------------------------------------------------------
		#---------------------------------------------------VARIABLE DECLARATION------------------------------------------------------------------------
		#-----------------------------------------------------------------------------------------------------------------------------------------------
		self.posX = float(x);
		self.posY = float(y);
		self.posZ = z;
		self.bitmap = None;
		self.collectIt = False;
		self.scale = 1.0;
		self.sound = base.loadSfx('./sound/itemup.wav')
		self.sound.setVolume(.3)
	#end __init__
	
	#-----------------------------------------------------------------------------------------------------------------------------------------------
	#----------------------------------------------------------------FUNCTIONS----------------------------------------------------------------------
	#-----------------------------------------------------------------------------------------------------------------------------------------------	
	# It studies distance between this item and the character.
	# It returns true if the distance is into collision's area.
	def collide(self, mainChar):
		# Calculation of distance between the character and the item
		distX = self.posX - mainChar.posX
		distY = self.posY - mainChar.posY
		distZ = self.posZ - mainChar.posZ
		distX = distX*distX
		distY = distY*distY
		distZ = distZ*distZ
		dist = sqrt(distX+distY+distZ)
		
		if dist<=2.0:
			self.sound.play()
			return True
		else:return False
	#end collide
#end class Item