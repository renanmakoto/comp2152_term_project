import random

# Define available loot that can be found in loot rooms
loot_options = ["Health Potion", "Poison Potion", "Secret Note", "Leather Boots", "Flimsy Gloves"]

# Class representing a single room in the dungeon
class DungeonRoom:
    def __init__(self, room_type):
        self.room_type = room_type
        self.description = self.set_description()
        self.effect = self.set_effect()

    # Assign description to room based on type
    def set_description(self):
        descriptions = {
            "loot": "You found loot!",
            "monster": "A monster appears from the shadows!",
            "trap": "You triggered a trap!",
            "empty": "The room is silent... nothing happens."
        }
        return descriptions.get(self.room_type, "A cold, empty, dusty room...")

    # Define effect of room on the player
    def set_effect(self):
        effects = {
            "loot": {"health": 0, "item": None},
            "monster": {"health": -3, "combat": +1},
            "trap": {"health": -1},
            "empty": {"health": 0}
        }
        return effects.get(self.room_type, {"health": 0})

# Generate dungeon with random number of rooms (set between 2 and 5 rooms)
def generate_random_dungeon(num_rooms=None):
    room_types = ["loot", "monster", "trap", "empty"]
    num_rooms = num_rooms if num_rooms else random.randint(2, 5)
    return [DungeonRoom(random.choice(room_types)) for _ in range(num_rooms)]

# Handle dungeon exploration logic
def explore_dungeon(belt, health_points, combat_strength, num_stars=0):
    print("\n You enter a dark dungeon...")
    dungeon = generate_random_dungeon()

    # Iterate through each room in dungeon
    for idx, room in enumerate(dungeon, start=1):
        print(f"\nRoom {idx}: {room.description}")

        # Loot room logic
        if room.room_type == "loot":
            loot = random.choice(loot_options)
            print(f" You found: {loot}")
            belt.append(loot)

            if loot in ["Health Potion", "Leather Boots"]:
                health_points = min(20, health_points + 2)
                print(" Gained +2 health.")
            elif loot == "Poison Potion":
                health_points = max(0, health_points - 2)
                print(" Lost -2 health.")
            else:
                print(" It's just for flavor. No effect.")

        # Monster room logic
        elif room.room_type == "monster":
            print(" A monster attacks! You defeat it but lost 3 health and gain 1 combat strength.")
            health_points = max(0, health_points - 3)
            combat_strength = min(6, combat_strength + 1)

        # Trap room logic
        elif room.room_type == "trap":
            print(" You fall into a trap! You lose 1 health.")
            health_points = max(0, health_points - 1)

        # Empty room logic
        elif room.room_type == "empty":
            print(" Nothing here. Take a breath.")

        # Display player stats
        print(f"️ Hero's health: {health_points}")
        print(f" Hero's combat strength: {combat_strength}")
        print(f" Belt: {belt}")

        # End game if hero dies in dungeon
        if health_points <= 0:
            print(" Your hero has died in the dungeon.")
            import functions
            winner = "Monster"

            # Prompt for hero name and save game result
            tries = 0
            input_invalid = True
            while input_invalid and tries in range(5):
                print("    |", end="    ")
                hero_name = input("Enter your Hero's name (in two words): ")
                name = hero_name.split()
                if len(name) != 2 or not all(part.isalpha() for part in name):
                    print("    |    Please enter a valid alphabetical name with two parts")
                    tries += 1
                else:
                    short_name = name[0][0:2] + name[1][0:1]
                    print("    |    I'm going to call you " + short_name + " for short")
                    input_invalid = False

            if not input_invalid:
                stars_display = "*" * num_stars
                print("    |    Hero " + short_name + " gets <" + stars_display + "> stars")
                functions.save_game(winner, hero_name=short_name, num_stars=num_stars)
            exit()

        # Ask if the player wants to continue exploring
        if idx < len(dungeon):
            choice = input("Do you want to continue exploring the dungeon? (yes/no): ").strip().lower()
            if choice != "yes":
                print("Best not to get too greedy.. You exit the dungeon early.")
                break
        else:
            # Message when the player finishes all rooms
            print(" Congratulations! You have finished exploring the dungeon. ")
            print(" Exiting now.")

    return belt, health_points, combat_strength
