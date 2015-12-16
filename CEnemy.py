# Python imports
from math import sqrt
import random

# Project imports
from Character import *
from pandac.PandaModules import Point3

# Generic enemy
class CEnemy (Character):
    def __init__(self, x, y, z):
        Character.__init__(self, x, y, z)
        
        #-----------------------------------------------------------------------------------------------------------------------------------------------
        #---------------------------------------------------VARIABLE DECLARATION------------------------------------------------------------------------
        #-----------------------------------------------------------------------------------------------------------------------------------------------
        self.distEnemy = 0
        self.distAttack = 0
        
        self.mainCharX = 0
        self.mainCharY = 0
        self.mainCharZ = 0
        
        #Start tasks
        taskMgr.add(self.taskEnemyMove, 'taskEnemyMove' )
        taskMgr.add(self.taskEnemyAction, 'taskEnemyAction' )
    #end __init__
    
    #-----------------------------------------------------------------------------------------------------------------------------------------------
    #----------------------------------------------------------------FUNCTIONS----------------------------------------------------------------------
    #-----------------------------------------------------------------------------------------------------------------------------------------------
    # It studies the distance between Character and Enemy.
    # It returns true if the distance is into area collision.
    def collide(self,mainChar):
        # Distance between the character and the this enemy
        self.mainCharX = mainChar.posX
        self.mainCharY = mainChar.posY
        self.mainCharZ = mainChar.posZ
        
        distX = self.posX - mainChar.posX
        distY = self.posY - mainChar.posY
        distZ = self.posZ - mainChar.posZ
        distX = distX*distX
        distY = distY*distY
        distZ = distZ*distZ
        self.distEnemy = sqrt(distX+distY+distZ)
        
        if self.distEnemy<=3.0: return True
        else: return False
    #end collide
    
    # Depending on the stop variable, will stop or move the enemy
    def stopEnemy(self, stop):
        if stop == True:
            #Move the enemy again
            taskMgr.remove('taskEnemyMove')
            taskMgr.remove('taskEnemyAction')
        else:
            #Stop the enemy
            taskMgr.add(self.taskEnemyMove, 'taskEnemyMove' )
            taskMgr.add(self.taskEnemyAction, 'taskEnemyAction' )
    #def stopEnemy
    
    #-----------------------------------------------------------------------------------------------------------------------------------------------
    #----------------------------------------------------------------TASKS,THREADS------------------------------------------------------------------
    #-----------------------------------------------------------------------------------------------------------------------------------------------
    # It makes the enemy move every frame towards the main character. And when is beside to him he stay there.
    def taskEnemyMove(self, task):
        if self.life <= 0:
            # Enemy's dead
            self.soundDeath.play()
            self.posX = -100
            self.model.hide()
            self.model.setX(self.posX)
            
            if self.attacking == True:
                self.att.destroyAttack()
            return task.done
        
        else:
            # Move the enemy
            if self.distEnemy >5.0:
                # Go nearer
                if self.posX > self.mainCharX:       pointX = self.posX - 0.3125
                else:                                pointX = self.posX + 0.3125
                
                if self.posZ > self.mainCharZ:       pointZ = self.posZ - 0.3125
                else:                                pointZ = self.posZ + 0.3125
            
                self.interval = self.model.posInterval(0.25, Point3(pointX,pointZ,self.posY))
                self.interval.start()
            
            self.posX = self.model.getX()
            self.posZ = self.model.getY()
                
            return task.cont
    #end taskEnemyMove
    
    # It decides which action the enemy is going to take
    def taskEnemyAction(self, task):
        if self.life<=0: 
            return task.done
        else:
            # It takes a random number from 1 to 1000
            num = random.randint(1,1000);
            
            if (num == 0): 
                if self.attacking == False: self.attack(self.mainCharX,self.mainCharY,self.mainCharZ)
            
            if (num == 250): 
                if self.attacking == False: self.attack(self.mainCharX,self.mainCharY,self.mainCharZ)
            
            if (num == 550): 
                if self.attacking == False: self.attack(self.mainCharX,self.mainCharY,self.mainCharZ)
          
            if (num == 750): 
                if self.attacking == False: self.attack(self.mainCharX,self.mainCharY,self.mainCharZ)
           
            if (num == 1000): 
                if self.attacking == False: self.attack(self.mainCharX,self.mainCharY,self.mainCharZ)
            
            return task.cont
    #end taskEnemyAttack
#end class CEnemy