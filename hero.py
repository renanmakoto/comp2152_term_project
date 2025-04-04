from character import Character
from staminaFeature import StaminaManager
import random

class Hero(Character):
    def __init__(self):
        super().__init__()
        self.character_class = self.assign_class()
        self.assign_class_randomly()
        print(f"Hero is a {self.character_class}")

        self.heroName = "Default Hero"
        self.storedHeroName = self.heroName
        self.previousHeroName = self.storedHeroName
        self.heroLevel = 1
        self.previousLevel = self.heroLevel
        self.storedLevel = self.previousLevel
        self.experiencePoints = 0
        self.totalXP = 0
        self.storedXP = self.totalXP
        self.specialAbility = "Power Strike"
        self.armorType = "Basic Armor"
        self.weaponType = "Basic Sword"
        self.spellPower = 50
        self.maximumSpellPower = 100
        self.heroStatus = "Active"
        self.backupStatus = self.heroStatus

        self.stamina = StaminaManager()
        self.storedStamina = self.stamina.currentStamina
        self.maximumStamina = self.stamina.maxStamina

    @property
    def hero_name(self):
        return self.heroName

    @hero_name.setter
    def hero_name(self, name):
        if isinstance(name, str) and name.strip():
            self.previousHeroName = self.heroName
            self.heroName = name
            self.storedHeroName = self.heroName

    @property
    def hero_level(self):
        return self.heroLevel

    @hero_level.setter
    def hero_level(self, level):
        if isinstance(level, int) and level > 0:
            self.previousLevel = self.heroLevel
            self.heroLevel = level
            self.storedLevel = self.heroLevel

    @property
    def experience_points(self):
        return self.experiencePoints

    @experience_points.setter
    def experience_points(self, points):
        if isinstance(points, int) and points >= 0:
            self.totalXP += points
            self.storedXP = self.totalXP
            self.experiencePoints = points
            if self.experiencePoints >= 10:
                self.level_up()

    def hero_attacks(self):
        if not self.stamina.can_attack():
            self.heroStatus = "Too Tired"
            return
        attackStrength = self.combat_strength + self.heroLevel
        self.stamina.use_stamina(5)
        self.storedStamina = self.stamina.currentStamina

    def rest(self):
        self.stamina.recover_stamina(10)
        self.storedStamina = self.stamina.currentStamina

    def level_up(self):
        self.heroLevel += 1
        self.storedLevel += 1
        self.experiencePoints = 0
        self.combat_strength += 1

    def __del__(self):
        print(f"This object is being destroyed by the garbage collector.")

    
    def assign_class(self):
        return random.choice(["Warrior","Thief","Mage","Tank"])
    

    def assign_class_randomly(self):
        if self.character_class == "Warrior":
            self.combat_strength += 2
            self.spellPower += 20
            self.health_points = max(0, self.health_points - 2)
        elif self.character_class == "Thief":
            self.combat_strength += 1
            self.spellPower += 1
            self.health_points = 2
        elif self.character_class == "Mage":
            self.combat_strength += 2
            self.spellPower += 20
            self.health_points = max(0, self.health_points - 2)
        elif self.character_class == "Tank":
            self.combat_strength = max(0, self.combat_strength - 1)
            self.spellPower += 1
            self.health_points = 5


    def special_abilities(self):
        print("    |    Activating Special Ability")
        if self.character_class == "Mage":
            print("    |    casts a Fire and burns everything around")
        elif self.character_class == "Tank":
            print("    |    blocks the attack and regains 2 health")
            self.health_points += 2
        elif self.character_class == "Thief":
            print("    |    disappears into the shadows")
            self.combat_strength += 1
        elif self.character_class == "Warrior":
            print("    |    strength goes up big time")
            self.combat_strength += 2
        else:
            print("    |    You don't have any abilities yet.")



