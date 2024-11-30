class Character:
    def __init__(self, health : int, strenght : int, speed : float, attackSpeed : float, healthRegenSpeed : int, positionRow : int = 0, positionCol : int = 0):
        if type(health) != int or type(strenght) != int or type(healthRegenSpeed) != int or type(positionCol) != int or type(positionRow) != int:
            raise Exception("it must be int")
        if type(speed) != float or type(attackSpeed) != float:
            raise Exception("speeds must be float")
        self.health = health
        self.strenght = strenght
        self.speed = speed
        self.attackSpeed = attackSpeed
        self.healthRegenSpeed = healthRegenSpeed
        self.positionRow = positionRow
        self.positionCol = positionCol
    
    def helthPlus(self, plusHealth):
        if type(plusHealth) != int:
            raise Exception("must be an Integer")
        self.health += plusHealth
        return self

    def setStrength(self, newStrenght):
        if type(newStrenght) != int:
            raise Exception("strenght must be a Integer")
        self.strenght = newStrenght
        return self

    def setStrength(self, newPosCol):
        if type(newPosCol) != int:
            raise Exception("positon Col must be a Integer")
        self.strenght = newPosCol
        return self

    def setStrength(self, newRow):
        if type(newRow) != int:
            raise Exception("position Row must be a Integer")
        self.strenght = newRow
        return self

    def setHealth(self, newHealth):
        if type(newHealth) != int:
            raise Exception("health must be a Integer")
        self.strenght = newHealth
        return self
    
    def setSpeed(self, newSpeed):
        if type(newSpeed) != int:
            raise Exception("speed must be a Integer")
        self.strenght = newSpeed
        return self

    def setAttackSpeed(self, newAttackSpeed):
        if type(newAttackSpeed) != int:
            raise Exception("AttackSpeed must be a Integer")
        self.strenght = newAttackSpeed
        return self

    def setHealthRegenSpeed(self, newHealthRegenSpeed):
        if type(newHealthRegenSpeed) != int:
            raise Exception("healthRegenSpeed must be a Integer")
        self.strenght = newHealthRegenSpeed
        return self
    
    def getStrength(self):
        return self.strenght
    
    def getHealth(self):
        return self.health
    
    def getSpeed(self):
        return self.speed
    
    def getAttackSpeed(self):
        return self.attackSpeed
    
    def getHealthRegenSpeed(self):
        return self.getHealthRegenSpeed

    def getPositionCol(self):
        return self.positionCol

    def getPositionRow(self):
        return self.positionRow