global healthBoost
healthBoost = False
global combatBoost
combatBoost = False

def temp_HP_boost():
        global healthBoost        
        # Check if the boost has been activated
        if healthBoost:            
            print("    |    Your health has been boosted by 3!")
            # Deactivates the boost, so it can't be used again
            healthBoost = False
            # Returns the amount of health boosted
            return 3
        else:
            return 0

def temp_ATK_boost():
        global combatBoost        
        if combatBoost:                        
            print("    |    Your combat power has been boosted by 3!")
            combatBoost = False
            return 3
        else:
            return 0
    