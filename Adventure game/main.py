from room import Room
from item import Item
from character import Enemy, Friend
from rpginfo import RPGInfo

spooky_castle = RPGInfo("The Spooky Castle")
spooky_castle.welcome()
RPGInfo.info()
RPGInfo.author = "JarraTonks"

kitchen = Room("Kitchen")
kitchen.set_description("A dank and dirty room buzzing with flies.")
katie = Friend("Katie","the cook")
katie.set_conversation("I hope you'll be staying for dinner")
katie.set_clue("Dave loves cheese.")
kitchen.character = katie
cheese = Item("cheese","it's mouldy, ugh")
kitchen.item = cheese

ballroom = Room("Ballroom")
ballroom.set_description("A large room with ornate golden decorations on each wall.")
painting = Item("painting","what a beautiful piece of art")
ballroom.item = painting
brian = Enemy("Brian","a spooky ghost")
brian.set_conversation("oooooooooooo")
brian.set_weakness("painting")
ballroom.character = brian

dining_hall = Room("Dining Hall")
dining_hall.set_description("A vast room with a shiny wooden floor; huge candlesticks guard the entrance.")
dave = Enemy("Dave","a smelly zombie")
dave.set_conversation("ARRRRRRRRGGHHH")
dave.set_weakness("cheese")
dining_hall.character = dave
knife = Item("knife","a rusty old knife")
dining_hall.item = knife

kitchen.link_room(dining_hall,"south")
ballroom.link_room(dining_hall,"east")
dining_hall.link_room(kitchen,"north")
dining_hall.link_room(ballroom,"west")

backpack = {}
current_room = kitchen
alive = True
moved_room = True
print("There are "+ str(Room.number_of_rooms) + " rooms to explore.\n")
while alive and Enemy.enemies_killed<2:
    if moved_room:
        current_room.get_details()
        moved_room= False
    command = input(" >")
    inhabitant = current_room.character
    if command in ["north","south","east","west"]:
        current_room = current_room.move(command)
        moved_room = True
        print("\n\n")
    elif command == "talk":
        try:
            inhabitant.talk()
        except:
            print("There is no-one to talk to in this room.")
    elif command == "fight":
        if inhabitant is not None:
            if isinstance(inhabitant,Enemy):
                fight_with = input("\nWhat will you fight with?\n >")
                if not fight_with in backpack:
                    print("You don't have that in your backpack.")
                elif not inhabitant.fight(fight_with):
                    print("\n\nGAME OVER")
                    alive = False
                else:
                    current_room.character = None
            else:
                inhabitant.fight(None)
        else:
            print("There is no-one to fight in this room")
    elif command == "clue":
        try:
            inhabitant.ask_clue()
        except:
            print("There aren't any clues around here.")
    elif command == "take":
        to_take = current_room.item
        if to_take is not None:
            backpack[to_take.get_name()] = to_take
            current_room.item = None
            print("You put a " + to_take.get_name() + " in your backpack.")
        else:
            print("There's nothing in here to take.")
    elif command=="backpack":
        print("\nHere's what you've got in your backpack:")
        for i in backpack:
            print ("-",i)
    elif command=="give up":
        alive = False
    else:
        print("\nYou can't do that!")
    print("\n")
if Enemy.enemies_killed == 2:
    print("\n\nYou won!\n\n")
RPGInfo.credits()