# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, name, current_room, inventory):
        self.name=name
        self.current_room=current_room
        self.inventory=[inventory]

    def __str__(self):
        return "Your name is {}. \nYou're in the {} room. \nYou have {} in your backpack.".format(self.name, self.current_room, self.inventory)