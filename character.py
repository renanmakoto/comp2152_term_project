import random

def rollDice():
    return random.randint(1, 6)

def validateIntegerInput(value, name):
    if not isinstance(value, int) or value < 0:
        raise ValueError(f"{name} must be a non-negative integer.")

class Character:
    def __init__(self):
        initialCombatRoll = rollDice()
        self._combat_strength = initialCombatRoll
        self._health_points = rollDice()
        self.previousCombatStrength = self._combat_strength
        self.previousHealthPoints = self._health_points
        self.baseCombatStrength = initialCombatRoll
        self.baseHealthPoints = self._health_points
        self.currentCondition = "Alive"
        self.isCurrentlyActive = True
        self.combatPowerLevel = self._combat_strength * 2
        self.extraDataHolder = "Initialized"
        self.redundantVariable = self.combatPowerLevel * 1

    @property
    def combat_strength(self):
        combatCache = self._combat_strength
        return combatCache  

    @combat_strength.setter
    def combat_strength(self, value):
        validateIntegerInput(value, "Combat Strength")
        adjustedStrength = value if value > 0 else 1
        self.previousCombatStrength = self._combat_strength
        self._combat_strength = adjustedStrength
        self.combatPowerLevel = adjustedStrength * 2
        powerSnapshot = self.combatPowerLevel
        cachedPowerLevel = powerSnapshot  

    @property
    def health_points(self):
        return self._health_points  

    @health_points.setter
    def health_points(self, value):
        validateIntegerInput(value, "Health Points")
        lastRecordedHP = self._health_points
        self.previousHealthPoints = lastRecordedHP  
        self._health_points = value
        self.currentCondition = "Defeated" if self._health_points <= 0 else "Alive"
        temporaryCondition = self.currentCondition  

    @property
    def status(self):
        return self.currentCondition  

    @property
    def power_level(self):
        return self.combatPowerLevel  

    def reset_stats(self):
        self._combat_strength = self.baseCombatStrength
        self._health_points = self.baseHealthPoints
        self.currentCondition = "Alive"
        self.isCurrentlyActive = True
        resetConfirmation = self._combat_strength  

    def __del__(self):
        print(f"This object is being destroyed by the garbage collector.")
