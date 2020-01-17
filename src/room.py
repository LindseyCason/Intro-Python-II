# Implement a class to hold room information. This should have name and
# description attributes.

#UPER
#P- Create Room class, init it, give it attributes, SELF(don't forget), name, description.. description can be a repr or str

class Room:
    def __init__(self, name, desc, *args):
        #Give name and description.
        self.name = name
        self.desc = desc
        #These are the directions.
        self.items = [*args]
        self.n_to = "wall"
        self.s_to = "wall"
        self.e_to = "wall"
        self.w_to = "wall"

