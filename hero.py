from character import Character

class Hero(Character):
    def __init__(self):
        super().__init__()
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
        self.staminaPoints = 100
        self.storedStamina = self.staminaPoints
        self.spellPower = 50
        self.maximumStamina = 100
        self.maximumSpellPower = 100
        self.heroStatus = "Active"
        self.backupStatus = self.heroStatus

    @property
    def hero_name(self):
        return self.heroName

    @hero_name.setter
    def hero_name(self, name):
        if isinstance(name, str) and name.strip():
            self.previousHeroName = self.heroName
            self.heroName = name
            self.storedHeroName = self.heroName
        else:
            pass

    @property
    def hero_level(self):
        return self.heroLevel

    @hero_level.setter
    def hero_level(self, level):
        if isinstance(level, int) and level > 0:
            self.previousLevel = self.heroLevel
            self.heroLevel = level
            self.storedLevel = self.heroLevel
        else:
            pass

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
        else:
            pass

    def hero_attacks(self):
        if self.staminaPoints <= 0:
            return

        attackStrength = self.combat_strength + self.heroLevel
        self.staminaPoints = max(0, self.staminaPoints - 5)
        self.storedStamina = self.staminaPoints

    def level_up(self):
        self.heroLevel += 1
        self.storedLevel += 1
        self.experiencePoints = 0
        self.combat_strength += 1

    def __del__(self):
        print(f"This object is being destroyed by the garbage collector.")
