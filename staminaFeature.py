class StaminaManager:
    def __init__(self, initialStamina=100):
        self.stamina = initialStamina
        self.maxStamina = initialStamina
        self.actionCost = {
            "attack": 20,
            "dodge": 15,
            "run": 10,
            "weak_attack": 5
        }

    def canPerform(self, action):
        return self.stamina >= self.actionCost.get(action, 0)

    def performAction(self, action):
        if self.canPerform(action):
            self.stamina -= self.actionCost[action]
            return True
        elif action == "attack" and self.stamina < self.actionCost["attack"]:
            return self.tryWeakAttack()
        else:
            return False

    def tryWeakAttack(self):
        if self.stamina >= self.actionCost["weak_attack"]:
            self.stamina -= self.actionCost["weak_attack"]
            return True
        return False

    def rest(self, amount=20):
        self.stamina = min(self.maxStamina, self.stamina + amount)

    def getValidActions(self):
        return [action for action in self.actionCost if self.stamina >= self.actionCost[action]]
