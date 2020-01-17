
from room import Room
from player import Player
from item import Item

# Declare all the rooms

#Items
# make and item with name and desc
gun = Item("gun", "loaded gun")
key = Item("key", "skeleton key")
water = Item("water", "12pk of water")
flashlight = Item("flashlight", "flashlight")
booty = Item("booty", "ALL THE BOOTY")

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons", water.name, flashlight.name),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", gun.name, key.name, water.name),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", water.name),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""", booty.name),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']



# Main
#

# Make a new player object that is currently in the 'outside' room.

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

#INITIAL OPTIONS
options = ["n", "north", "s", "south", "e", "east", "w", "west", "q","quit", "i", "info"]

#INITIAL PLAYER
player = Player("Player 1", "outside", "map")

#START SCREEN
print(f"______________________________________________________________")
print()
print(F"WELCOME TO PYTHON OOP ADVENTURES")
print()
print(f"LET THE GAMES BEGIN")
print()
print()
print(f"""To Play:
______________________________________________________________
You can go, North (N), South (S), East (E) or West (W).
You can check your backpack inventory by selecting (I).
You can check the contents of a room by selecting (Check).
You can drop and item from your inventory by selecting (Drop).
You can quit the game by selecting (Q).
See what treasure you can find!
Good Luck!
______________________________________________________________""")

#PLAYER NAME
name = input("To continue, please give me your name?... ")
if len(name) > 0:
    player.name = name
    print(f"Welcome, {player.name}!")
elif len(name) <=0:
    print(f"Please enter a valid name")

while True:
    print(room[player.current_room].desc)
    option = input("Where would you like to go?>> ")
    pi=player.inventory

    def player_inv_print(pi):
        print(f"""Your Backpack Contains:""")
        for i in pi:
            print(f"~~>" , i)
#QUIT AND INVENTORY CHECK
    if option.lower() == "q":
        print(f"Thanks for playing, {player.name}!")
        break
    elif option.lower() == "i":
        player_inv_print(pi)

#DIRECTIONS
    elif option.lower() == "n":
        print(f"""North it is!""")
        if player.current_room == "outside":
            player.current_room="foyer"
            print(f"""You have now arrived at the {player.current_room}""")
        elif player.current_room == "foyer":
            player.current_room="overlook"
            print(f"""You have now arrived at the {player.current_room}""")
        elif player.current_room=="narrow":
            player.current_room="treasure"
            print(f"""You have now arrived at the {player.current_room}""")
        else:
            print("You've hit a deadend!")
            print(f"""You are in the {player.current_room}""")

    elif option.lower() == "s":
        print("South we go!")
        if player.current_room == "overlook":
            player.current_room="foyer"
            print(f"""You have now arrived at the {player.current_room}""")

        elif player.current_room == "foyer":
            player.current_room="outside"
            print(f"""You have now walked back {player.current_room}""")
        elif player.current_room=="treasure":
            player.current_room="narrow"
            print(f"""You have now arrived at the {player.current_room}""")
        else:
            print("You've hit a deadend!")
            print(f"""You are located: {player.current_room}""")
    elif option.lower() == "e":
        print("Headed East!")
        if player.current_room == "foyer":
            player.current_room = "narrow"
        else:
            print("You've hit a deadend!")
            print(f"""You are located: {player.current_room}""")

    elif option.lower() == "w":
        print("Westward!")
        if player.current_room == "narrow":
            player.current_room = "foyer"
        else:
            print("You've hit a deadend!")
            print(f"""You are located: {player.current_room}""")

#CHECK ROOM
    elif option.lower() == "check":
        room_inv= room[player.current_room].items
        pi=player.inventory

        def room_inv_print(x):
            print("This room contains: ")
            for i in x:
                print("~~> ", i)


        def player_inv_print(pi):
            print(f"""Your Backpack Now Contains:""")
            for i in pi:
                print(f"~~>" , i)

        if len(room_inv) == 0:
            print("This room is empty...")
            
        elif len(room_inv) >0:
            room_inv_print(room_inv)
            item_input = input("Which item would you like to grab?: >>")
            if item_input.lower() in room_inv:
                player.inventory.append(item_input)                
                print(f"You have grabbed the {item_input}.")
                player_inv_print(pi)
                room_inv.remove(item_input)
            elif item_input.lower() == "drop":
                print(f"Your backpack contains: ", player.inventory)
                item_input = input(" What would you like to drop? >>")
                if item_input.lower() in player.inventory:
                    player.inventory.remove(item_input)
                    room_inv= room[player.current_room].items
                    room_inv.append(item_input)
                    print("Your backpack now contains: ", player.inventory)
                    print("Room now contains: ", room_inv)
            else:
                print("You did not have that item or have made an invalid selection.")

        else:
            print("That item is not in this room")
#DROP
    elif option.lower() == "drop":
        pi=player.inventory
        ri=room[player.current_room].items

        def room_inv_print(ri):
            print("This room now contains: ")
            for i in ri:
                print("~~> ", i)

        def player_inv_print(pi):
            print(f"""Your Backpack Contains:""")
            for i in pi:
                print(f"~~>" , i)
                
        player_inv_print(pi)
        item_input = input(" What would you like to drop? >>")

        if item_input.lower() in player.inventory:
            player.inventory.remove(item_input)
            room_inv= room[player.current_room].items
            room_inv.append(item_input)
            player_inv_print(pi)
            room_inv_print(ri)
        else:
            print("You did not have that item")


    

