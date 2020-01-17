#adv
from room import Room
from player import Player
# Declare all the rooms
room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),
    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),
    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),
    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),
    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
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
#
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
# Create a player
# Let player input their name
player = Player(input("Please enter your name: "), room['outside'])
print(player.current_room)
directions = ["n", "s", "e", "w"]
# Create basic REPL loop
while True:
    # Read command
    cmd = input("~~> ").lower()
    # Check if it's n/s/e/w/q
    if cmd in directions:
        # Make player travel in that direction
        player.travel(cmd)
    elif cmd == "q":
        # Quit
        print("Goodbye!")
        exit()
    else:
        print("I did not recognize that command")

#player
# # Write a class to hold player information, e.g. what room they are in
# currently.
​
class Player:
​
    def __init__(self, name, starting_room):
        self.name = name
        self.current_room = starting_room
​
    def travel(self, direction):
        # Player should be able to move in a direction
        next_room = self.current_room.get_room_in_direction(direction)
        if next_room is not None:
            self.current_room = next_room
            print(self.current_room)
        else:
            print("You cannot move in that direction.")
Collapse
#room
# Implement a class to hold room information. This should have name and
# description attributes.
​
class Room:
    def __init__(self, name, description):
        # Name, description
        self.name = name
        self.description = description
        # n_to, s_to, e_to, w_to
        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None
        self.items = []
​
    def __str__(self):
        display_string = ""
        display_string += f"\n----------------\n"
        display_string += f"\n{self.name}\n"
        display_string += f"\n{self.description}\n"
        display_string += f"\n{self.get_exits_string()}\n"
        return display_string
​
    def get_room_in_direction(self, direction):
        if hasattr(self, f"{direction}_to"):
            return getattr(self, f"{direction}_to")
        return None
​
    def get_exits(self):
        exits = []
        if self.n_to:
            exits.append("n")
        if self.s_to:
            exits.append("s")
        if self.e_to:
            exits.append("e")
        if self.w_to:
            exits.append("w")
        return exits
​
    def get_exits_string(self):
        return f"Exits: {', '.join(self.get_exits())}"
​