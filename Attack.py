# Python imports
from math import sqrt

# Panda3D imports
from direct.showbase import DirectObject
from direct.showbase.DirectObject import DirectObject
from pandac.PandaModules import Point3

# Project imports
from Image import *

# It manages character and enemies attack
class Attack (DirectObject):	
	def __init__(self, type, enemy_type, enemies, char):
		#-----------------------------------------------------------------------------------------------------------------------------------------------
		#---------------------------------------------------VARIABLE DECLARATION------------------------------------------------------------------------
		#-----------------------------------------------------------------------------------------------------------------------------------------------
		self.posX = 0
		self.posY = 0
		self.posZ = 0
		self.bitmap = None
		self.flag = True
		self.lastTime = 0.0
		self.tex1 = "None"
		self.tex2 = "None"
		self.texFinal = "None"
		self.isexploding = False
		
		# Character Attack
		self.nearEnemy = None
		self.mainChar = None
		
		# Enemy attack
		self.enemy = None
		self.finalX = 0
		self.finalY = 0
		self.finalZ = 0		
		
		if( type == "ENEMY"):
			#-----------------------------------------------------------------------------------------------------------------------------------------------
			#----------------------------------------------------------------ENEMY ATTACK INIT--------------------------------------------------------------
			#-----------------------------------------------------------------------------------------------------------------------------------------------
			# Initial position
			self.posX = enemies.posX
			self.posY = enemies.posY
			self.posZ = enemies.posZ
			
			self.enemy = enemies
			
			# Destination position
			self.finalX = char[0]
			self.finalY = char[1]
			self.finalZ = char[2]
			
			# Generate attack
			self.bitmap = Image()
			if enemy_type == "HAMBURGUER": 	
				self.bitmap = self.bitmap.loadModel("./models/Square.egg", "./tex/ham_attack1.png", self.posX, self.posY, self.posZ, scale = (1.6,1.0,0.75))
				self.tex1 = "./tex/ham_attack1.png"
				self.tex2 = "./tex/ham_attack2.png"
				self.texFinal = "./tex/ham_exp.png"
				self.sound = base.loadSfx('./sound/enemyHit.wav')
			if enemy_type == "CAN": 	
				self.bitmap = self.bitmap.loadModel("./models/Square.egg", "./tex/can_attack1.png", self.posX, self.posY, self.posZ, (1.0,1.0,0.75))
				self.tex1 = "./tex/can_attack1.png"
				self.tex2 = "./tex/can_attack2.png"
				self.texFinal = "./tex/can_exp.png"
				self.sound = base.loadSfx('./sound/enemyHit2.wav')
			if enemy_type == "DONA":	
				self.bitmap = self.bitmap.loadModel("./models/Square.egg", "./tex/dona_attack1.png", self.posX, self.posY, self.posZ, (1.6,1.0,0.75))
				self.tex1 = "./tex/dona_attack1.png"
				self.tex2 = "./tex/dona_attack2.png"
				self.texFinal = "./tex/dona_exp.png"
				self.sound = base.loadSfx('./sound/enemyHit3.wav')
			if enemy_type == "POTATOES":	
				self.bitmap = self.bitmap.loadModel("./models/Square.egg", "./tex/potatoes_attack1.png", self.posX, self.posY, self.posZ, (1.5,1.0,0.75) )
				self.tex1 = "./tex/potatoes_attack1.png"
				self.tex2 = "./tex/potatoes_attack2.png"
				self.texFinal = "./tex/potatoes_exp.png"
				self.sound = base.loadSfx('./sound/enemyHit.wav')
		
			# Shoot attack
			if self.finalX<self.posX:
				self.bitmap.setTexScale(TextureStage.getDefault(),1,1)    	
				self.interval = self.bitmap.posInterval(1.75, Point3(self.posX-15,self.finalZ,self.finalY))
				self.interval.start()
			else:
				self.bitmap.setTexScale(TextureStage.getDefault(),-1,1)
				self.interval = self.bitmap.posInterval(1.75, Point3(self.posX+15,self.finalZ,self.finalY))
				self.interval.start()
			
			# Tasks
			taskMgr.add(self.taskEnemyAttack, 'taskEnemyAttack' )
			taskMgr.add(self.taskAttackAnimation, 'taskAttackAnimation' )
		
			# Sound
			self.sound.setVolume(.3)
			self.sound.play()
		else:
			#-----------------------------------------------------------------------------------------------------------------------------------------------
			#----------------------------------------------------------------CHARACTER ATTACK INIT----------------------------------------------------------
			#-----------------------------------------------------------------------------------------------------------------------------------------------
			# Initial position
			self.posX = char.posX
			self.posY = char.posY
			self.posZ = char.posZ
			
			self.mainChar = char
	    
			# Searching nearest enemy to attack
			distMin = 99999999.9;
			if enemies == []:
			    # There are no enemies
			    self.nearEnemy = None
			else:
			    for x in enemies:
				distX = char.posX - x.posX
				distY = char.posY - x.posY
				distZ = char.posZ - x.posZ
				distX = distX*distX
				distY = distY*distY
				distZ = distZ*distZ
				distToEnemy = sqrt(distX+distY+distZ)
				
				# Nearest enemy
				if distToEnemy<distMin:
				    distMin = distToEnemy
				    self.nearEnemy = x
			
			# Generate attack    
			self.bitmap = Image()
			if(type == "GRAIN"):            self.bitmap = self.bitmap.loadModel("./models/Square.egg", "./tex/attacks/grain.png", self.posX, self.posY, self.posZ, (2.0,1.0,1.5))
			if(type == "FRUIT"):            self.bitmap = self.bitmap.loadModel("./models/Square.egg", "./tex/attacks/fruit.png", self.posX, self.posY, self.posZ, (2.0,1.0,1.5))
			if(type == "MILK"):             self.bitmap = self.bitmap.loadModel("./models/Square.egg", "./tex/attacks/milk.png", self.posX, self.posY, self.posZ, (2.0,1.0,1.5))
			if(type == "VEGETABLE"):        self.bitmap = self.bitmap.loadModel("./models/Square.egg", "./tex/attacks/vegetable.png", self.posX, self.posY, self.posZ, (2.0,1.0,1.5))
			if(type == "FISH"):             self.bitmap = self.bitmap.loadModel("./models/Square.egg", "./tex/attacks/fish.png", self.posX, self.posY, self.posZ, (2.0,1.0,1.5))
		    
			self.attacking = True;
			
			# Shoot attack
			if( self.nearEnemy == None ):
				self.interval = self.bitmap.posInterval(1.75, Point3(40,self.posZ,self.posY))
				self.interval.start()
			else:
				if self.nearEnemy.posX<self.posX:
					self.bitmap.setTexScale(TextureStage.getDefault(),1,1)    	
					self.interval = self.bitmap.posInterval(1.75, Point3(self.posX-20,self.posZ,self.posY))
					self.interval.start()
				else:
					self.bitmap.setTexScale(TextureStage.getDefault(),-1,1)
					self.interval = self.bitmap.posInterval(1.75, Point3(self.posX+20,self.nearEnemy.posZ,self.nearEnemy.posY))
					self.interval.start()
			
			# Tasks	
			taskMgr.add(self.taskCharAttack, 'taskCharAttack' )
			
			# Sound
			self.sound = base.loadSfx('./sound/charAttack.wav')
			self.sound.setVolume(.3)
			self.sound.play()
	    #end __init__

	#-----------------------------------------------------------------------------------------------------------------------------------------------
	#----------------------------------------------------------------FUNCTIONS----------------------------------------------------------------------
	#-----------------------------------------------------------------------------------------------------------------------------------------------
	# It studies distance between this enemy and character's attack.
	# It returns true if the distance is into collision's area.
	def en_charAttCollide(self, enemy):
		# Distance between the enemy and character's attack
		distX = self.posX - enemy.posX
		distY = self.posY - enemy.posY
		distZ = self.posZ - enemy.posZ
		distX = distX*distX
		distY = distY*distY
		distZ = distZ*distZ
		self.distAttack = sqrt(distX+distY+distZ)
		
		if self.distAttack <= 2.0:      return True
		else:                           return False
	#end en_charACollide
	
	# It studies the distance between Character and Enemy's Attack.
	# It returns true if the distance is into area collision.
	def char_enAttCollide(self, mainChar):
		# Distance between the character and the this enemy attack
		distX = self.posX - mainChar.posX
		distY = self.posY - mainChar.posY
		distZ = self.posZ - mainChar.posZ
		distX = distX*distX
		distY = distY*distY
		distZ = distZ*distZ
		self.distAttack = sqrt(distX+distY+distZ)
		
		if self.distAttack<=1.5:return True
		else: return False
       #end char_enACollide
       
	# Attack explosion
	def explode(self):
		taskMgr.remove('taskAttackAnimation')
		self.isexploding = True
		self.bitmap.clearTexture()
		tex = loader.loadTexture(self.texFinal) 
		self.bitmap.setTexture(tex, 1)
		self.bitmap.setScale((1.5,1.0,1.5))
	#end explode
       
	# Destroy this attack
	def destroyAttack(self):
		self.posX = -100
		self.bitmap.hide()
		self.bitmap.setX(self.posX)
		self.sound.stop()
		if self.mainChar != None:
			self.mainChar.attacking = False
		else:
			self.enemy.attacking = False
			
	#end destroyAttack
	
	
	#-----------------------------------------------------------------------------------------------------------------------------------------------
	#----------------------------------------------------------------TASKS,THREADS------------------------------------------------------------------
	#-----------------------------------------------------------------------------------------------------------------------------------------------
	# It makes move the attack of the character through the screen, 2 seconds of duration.
	def taskCharAttack(self, task):  
		if( task.time > 2 ):
		    self.destroyAttack()
		    return task.done
		else:		    
			self.posX = self.bitmap.getX()
			self.posZ = self.bitmap.getY()
			return task.cont
	#end taskCharAttack
	
	# It makes move the attack of the enemy through the screen, 2 seconds of duration.
	def taskEnemyAttack(self, task):
		if( task.time > 2 ):
		    self.destroyAttack()
		    return task.done
		else:
		    if self.isexploding == False:
				if ((self.finalX+0.075 > self.posX) and (self.finalX-0.075 < self.posX)):
					pass
				else:
					self.posX = self.bitmap.getX()
					self.posZ = self.bitmap.getY()
		    
		    return task.cont
	#end taskAttack
	
	#Attack animation
	def taskAttackAnimation(self,task):
		if task.time > 1.75:
			self.bitmap.clearTexture()
			tex = loader.loadTexture(self.texFinal) 
			self.bitmap.setTexture(tex, 1)
			self.bitmap.setScale((1.5,1.0,1.5))
			return task.done
		else:
			if (task.time - self.lastTime) > 0.15:
				self.lastTime = task.time
				if self.flag==True:
					self.bitmap.clearTexture()
					tex = loader.loadTexture(self.tex1) 
					self.bitmap.setTexture(tex, 1)
					self.flag = False
				else:
					self.bitmap.clearTexture()
					tex = loader.loadTexture(self.tex2) 
					self.bitmap.setTexture(tex, 1)
					self.flag = True
			return task.cont
	#end taskAttackAnimation
		
#end class Attack