"""
classes for the game
"""
class Room:
    """
    class with information about the rooms
    >>> kitchen = Room("Kitchen")
    >>> kitchen.set_description("A dank and dirty room buzzing with flies.")
    >>> dining_hall = Room("Dining Hall")
    >>> kitchen.link_room(dining_hall, "south")
    >>> kitchen.get_details()
    Kitchen
    --------------------
    A dank and dirty room buzzing with flies.
    The Dining Hall is south
    """
    def __init__(self, name: str, descriprion = None, character = None, item = None) -> None:
        """
        main info about the room: name, descriprion, character in it and item in it
        """
        self.name = name
        self.description = descriprion
        self.locations = []
        self.character = character
        self.item = item

    def set_description(self, description: str) -> None:
        """
        creates a description of the room
        """
        self.description = description

    def link_room(self, room: object, location: str) -> None:
        """
        links room to others
        """
        self.locations.append((room.name, location, room))

    def set_character(self, character: object) -> None:
        """
        places a character in the room
        """
        self.character = character

    def set_item(self, item: object) -> None:
        """
        places an item in the room
        """
        self.item = item

    def get_details(self) -> None:
        """
        prints details about the room
        """
        print(self.name)
        print('--------------------')
        print(self.description)
        for i in self.locations:
            print(f'The {i[0]} is {i[1]}')

    def get_character(self):
        """
        returns a character who is in the room
        """
        return self.character

    def get_item(self):
        """
        returns an item which is in the room
        """
        return self.item

    def move(self, root: str):
        """
        changes room
        """
        for i in self.locations:
            if root == i[1]:
                return i[2]
        return None


class Enemy:
    """
    class for all enemies and their defeats
    >>> dave = Enemy("Dave", "A smelly zombie")
    >>> dave.set_weakness("cheese")
    >>> dave.set_conversation("What's up, dude! I'm hungry.")
    >>> dave.describe()
    Dave is here!
    A smelly zombie
    >>> dave.fight('cheese')
    True
    >>> dave.fight('snow')
    False
    >>> dave.talk()
    What's up, dude! I'm hungry.
    """
    defeats = 0
    def __init__(self, name: str, description: str, conversation = None, weakness = None) -> None:
        """
        main info about the enemy: name, descriprion, its conversation and weakness
        """
        self.name = name
        self.description = description
        self.conversation = conversation
        self.weakness = weakness

    def set_conversation(self, conversation: str) -> None:
        """
        creates enemy's conversation
        """
        self.conversation = conversation

    def set_weakness(self, weakness: str) -> None:
        """
        creates enemy's weakness
        """
        self.weakness = weakness

    def describe(self):
        """
        describes an enemy
        """
        print(f'{self.name} is here!')
        print(self.description)

    def talk(self):
        """
        prints enemy's talk
        """
        print(self.conversation)

    def fight(self, item: str):
        """
        fight with the enemy
        """
        if item == self.weakness:
            return True
        return False

    def get_defeated(self):
        """
        counts enemy defeats
        """
        Enemy.defeats += 1
        return Enemy.defeats

class Item:
    """
    class for items in the rooms
    >>> cheese = Item("cheese")
    >>> cheese.set_description("A large and smelly block of cheese")
    >>> cheese.describe()
    The [cheese] is here - A large and smelly block of cheese
    >>> cheese.get_name()
    'cheese'
    """
    def __init__(self, name: str, description = None) -> None:
        """
        main info about the item: name and description
        """
        self.name = name
        self.description = description

    def set_description(self, description: str) -> None:
        """
        creates a description of the item
        """
        self.description = description

    def describe(self):
        """
        describes an item
        """
        print(f'The [{self.name}] is here - {self.description}')

    def get_name(self):
        """
        returns item's name
        """
        return self.name

if __name__ == '__main__':
    import doctest
    print(doctest.testmod())
