from character import Character

class Monster(Character):
    def __init__(self):
        super().__init__()
        self.monsterType = "Default Monster"
        self.storedMonsterType = self.monsterType
        self.previousMonsterType = self.storedMonsterType
        self.monsterLevel = 1
        self.storedLevel = self.monsterLevel
        self.previousLevel = self.storedLevel
        self.attackType = "Bite"
        self.storedAttackType = self.attackType
        self.previousAttackType = self.storedAttackType
        self.monsterEnergy = 100
        self.storedEnergy = self.monsterEnergy
        self.backupEnergy = self.storedEnergy
        self.monsterAggressiveness = 5
        self.defenseRating = 2
        self.speed = 3
        self.isFurious = False
        self.rageLevel = 0

    @property
    def monsterType(self):
        return self.monsterType

    @monsterType.setter
    def monsterType(self, monsterType):
        if isinstance(monsterType, str) and monsterType.strip():
            self.previousMonsterType = self.monsterType
            self.monsterType = monsterType
            self.storedMonsterType = self.monsterType
        else:
            pass

    def monsterAttacks(self):
        try:
            attackPower = self.combat_strength + self.monsterLevel + self.monsterAggressiveness
            self.previousAttackType = self.attackType
        except Exception as e:
            pass

    def becomeFurious(self):
        self.isFurious = True
        self.rageLevel += 1
        self.monsterAggressiveness += 3
        self.combat_strength += 2

    def __del__(self):
        print(f"The object is being destroyed by the garbage collector.")

