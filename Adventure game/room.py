from character import Character
from item import Item
class Room():
    number_of_rooms = 0
    def __init__(self, room_name):
        self.name = room_name
        self.description = None 
        self.linked_rooms = {}
        self._character = None
        self._item = None
        Room.number_of_rooms += 1

    def set_description(self, room_description):
        """
        Sets a string as the description of the room.
        """
        self.description = room_description

    def set_name(self, room_name):
        """
        Sets a string as the name of the room
        """
        self.name = room_name

    def link_room(self, room_to_link, direction):
        """
        Sets a room object as a linked room with direction from the room
        """
        self.linked_rooms[direction] = room_to_link

    def get_description(self): 
        """
        Returns a string containing the description of the room
        """
        return self.description

    def describe(self):
        """
        Prints a string containing the description of the room
        """
        print(self.description)

    def get_name(self):
        """
        Returns a string containing the name of the room
        """
        return self.name

    def get_details(self):
        """
        Prints name, description, linked rooms, and items and inhabitants in the room in a clear format
        """
        print(self.name + "\n-------------------")
        self.describe()
        for direction in self.linked_rooms:
            room = self.linked_rooms[direction]
            print("The " + room.get_name() + " is " + direction)
        room_item = self.item
        if room_item is not None:
            print("\n")
            room_item.describe()
        inhabitant = self.character
        if inhabitant is not None:
            print("\n")
            inhabitant.describe()

    
    @property
    def character(self):
        """
        Returns a character object, the character in the room
        """
        return self._character
    
    @character.setter
    def character(self, room_character):
        """
        Sets a character object as the character in the room
        """
        if isinstance(room_character, Character) or room_character is None:
            self._character = room_character
        else:
            print("character setting unsuccessful")

    @property
    def item(self):
        """
        Returns an item object, the item in the room
        """
        return self._item
       
    @item.setter
    def item(self, room_item):
        """
        Sets an item object as the item in the room
        """
        if isinstance(room_item, Item) or room_item is None:
            self._item = room_item
        else:
            print("item setting unsuccessful")

    def move(self,direction):
        """
        Returns the room in the given direction from the given room
        """
        if direction in self.linked_rooms:
            return self.linked_rooms[direction]
        else:
            print("\nYou can't go that way.")
            return self