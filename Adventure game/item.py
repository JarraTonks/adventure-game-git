class Item():
    def __init__(self, item_name, item_description):
        self.name = item_name
        self.description = item_description
    
    def set_name(self, item_name):
        """
        Sets a string as the name of the item
        """
        self.name = item_name

    def set_description(self, item_description):
        """
        Sets a string as the description of the item 
        """
        self.description = item_description

    def get_name(self):
        """
        Returns a string containing the name of the item
        """
        return self.name

    def get_description(self):
        """
        Returns a string containg the description of the item
        """
        return self.description

    def describe(self):
        """
        Prints the name and description of the item in a sentence
        """
        print("There's a " + self.name + " in here, " + self.description + ".")