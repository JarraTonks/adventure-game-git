from random import getrandbits

class Character():

    def __init__(self, char_name, char_description):
        self.name = char_name
        self.description = char_description
        self.conversation = None

    def describe(self):
        """
        Prints the name and description of the character in a sentence
        """
        print(self.name + ", " + self.description + ", is here!" )

    def set_conversation(self, char_conversation):
        """
        Sets the string that this character will say when talked to
        """
        self.conversation = char_conversation

    def talk(self):
        """
        Prints the name and conversation of the character
        """
        if self.conversation is not None:
            print("[" + self.name + " says]: " + self.conversation)
        else:
            print("\n" + self.name + " doesn't want to talk to you")

    def fight(self, combat_item):
        """
        Prints refusal to fight
        """
        print("\n" + self.name + " doesn't want to fight with you")
        return True

class Enemy(Character):
    enemies_killed = 0
    def __init__(self, char_name, char_description):
        super().__init__(char_name, char_description) 
        self.weakness = None

    def set_weakness(self, enemy_weakness):
        """
        Sets a string as an Enemy's weakness (what can kill it)
        """
        self.weakness = enemy_weakness

    def get_weakness(self):
        """
        Returns a string containing an Enemy's weakness
        """
        return self.weakness

    def fight(self, combat_item): 
        """
        Takes an Item object as input to fight the Enemy with
        """
        if combat_item == self.weakness:
            print("\nYou fend " + self.name + " off with the " + combat_item)
            Enemy.enemies_killed += 1
            return True
        else:
            print("\n"+self.name + " crushes you, puny adventurer")
            return False

class Friend(Character):
    def __init__(self, char_name, char_description):
        super().__init__(char_name, char_description)
        self.clue = None

    def set_clue(self, friend_clue):
        """
        Sets a string as a clue
        """
        self.clue = friend_clue

    def get_clue(self):
        """
        Returns a string containg the Friend's clue
        """
        return self.clue

    def ask_clue(self):
        """
        Randomly either print the clue or come back later
        """
        if self.clue is not None:
            if bool(getrandbits(1)):
                print("[" + self.name + " says]: " + self.clue)
            else:
                print("[" + self.name + " says]: " + "Come back later...")
        else:
            print("[" + self.name + " says]: " + "I don't know anything, I promise!")