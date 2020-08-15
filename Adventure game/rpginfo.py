class RPGInfo():
    author = "Anonymous"

    def __init__(self, game_title):
        self.title = game_title

    def welcome(self):
        """
        Prints welcome to game message
        """
        print("Welcome to " + self.title+".\n")

    @classmethod
    def credits(cls):
        """
        Prints credits for the game
        """
        print("Thank you for playing.\nCreated by " + cls.author+".\n")

    @staticmethod
    def info():
        """
        Prints credits for the game generator
        """
        print("Made using the OOP RPG game creator (c) Claire.\n")

