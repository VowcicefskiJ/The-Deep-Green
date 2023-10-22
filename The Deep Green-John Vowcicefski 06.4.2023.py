import random

class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.item = None


class Item:
    def __init__(self, name):
        self.name = name


class Player:
    def __init__(self):
        self.inventory = []


class JungleCreature:
    def __init__(self):
        self.encountered = False


rooms = [
    Room("Start Room", "You wake up in the middle of a dense jungle. You have no memory of how you got here."),
    Room("Clearing", "You find yourself in a small clearing. The sunlight breaks through the trees."),
    Room("Riverbank", "You reach a peaceful riverbank. The sound of flowing water is calming."),
    Room("Cave", "You enter a dark cave. The air is damp and cool."),
    Room("Treehouse", "You climb up a sturdy treehouse. You have a better view of the jungle from up here."),
    Room("Waterfall", "You stumble upon a majestic waterfall. The water crashes down with great force."),
    Room("Abandoned Temple", "You discover an ancient temple, long forgotten. It emanates an eerie atmosphere."),
    Room("Final Room", "You cautiously enter the final room. It is shrouded in darkness."),
    Room("Large Field", "You enter a large open field. The grass stretches as far as the eye can see.")
]

jungle_creature = JungleCreature()

items = [
    Item("Compass"),
    Item("Rope"),
    Item("Torch"),
    Item("Binoculars"),
    Item("Machete"),
    Item("Key")
]

rooms[1].item = items[0]  # Compass
rooms[2].item = items[1]  # Rope
rooms[3].item = items[2]  # Torch
rooms[4].item = items[3]  # Binoculars
rooms[5].item = items[4]  # Machete
rooms[6].item = items[5]  # Key

current_room = rooms[0]
items_collected = 0
player = Player()

while True:
    print(current_room.description)

    if current_room == rooms[7] and not jungle_creature.encountered:
        print("You encounter a terrifying jungle creature. It attacks you and you lose the game!")
        input("Hit any key to exit")
        break

    if current_room.item:
        print("You found an item:", current_room.item.name)
        pick_up_choice = input("Do you want to pick up the item? (yes/no): ")
        if pick_up_choice.lower() == "yes":
            player.inventory.append(current_room.item)
            items_collected += 1
            current_room.item = None
            print("You successfully picked up the item.")
        print("Current inventory:", [item.name for item in player.inventory])
        print("Items left to collect:", 6 - items_collected)

    direction = input("Enter a direction (North, South, East, West, North-East, South-West, South-East, North-West): ")

    directions_map = {
        "North": rooms[1],
        "South": rooms[2],
        "East": rooms[3],
        "West": rooms[4],
        "North-East": rooms[5],
        "South-West": rooms[6],
        "South-East": rooms[7],
        "North-West": rooms[8]
    }

    if direction in directions_map:
        if direction == "North-West":
            print("You hear hissing as you enter the North-West direction.")
            snake_chance = random.randint(1, 10)
            if snake_chance <= 4:
                print("You fall into a pit with venomous snakes. You lose the game!")
                input("Hit any key to exit")
                break
            else:
                current_room = rooms[8]
        else:
            current_room = directions_map[direction]

        if current_room == rooms[7] and items_collected == 6:
            print(
                "You enter the final room with all the collected items. You have successfully escaped the jungle and won the game!")
            input("Hit any key to exit")
            break
    else:
        print("Invalid direction. Please try again.")
