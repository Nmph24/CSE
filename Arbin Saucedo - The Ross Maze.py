class Item(object):
    def __init__(self, name):
        self.name = name

    def pick_up(self):
        print("You have picked up %s" % self.name)


class Statue(Item):
    def __init__(self, name):
        super(Statue, self).__init__(name)


class BobRossStatue(Statue):
    def __init__(self):
        super(BobRossStatue, self).__init__("Bob Ross Statue")

    def look(self):
        print("A %s look nice and it is detailed greatly" % self.name)


class Paintings(Item):
    def __init__(self, name):
        super(Paintings, self).__init__(name)


class WildernessDay(Paintings):
    def __init__(self):
        super(WildernessDay, self).__init__("Wilderness Day")

    def look(self):
        print("%s was a painting and the last one Bob Ross painted and it shows a "
              "forest with a sun down as it time and a path way made of rocks" % self.name)


class InTheMidstOfWinter(Paintings):
    def __init__(self):
        super(InTheMidstOfWinter, self).__init__("In The Midst Of Winter")

    def look(self):
        print("%s really speaks for it self in it nice winter forest and it small cabin and "
              "the trees around it that are dead. The winter is harsh but nice" % self.name)


class LakeAtTheRidge(Paintings):
    def __init__(self):
        super(LakeAtTheRidge, self).__init__("Late At The Ridge")

    def look(self):
        print("%s " % self.name)


class You(object):
    def __init__(self, name, desc):
        self.name = name
        self.desc = desc

    def note(self):
        print("%s " % self.name)


your_name = input("What is your name? ")
print("Nice to meet you %s" % your_name)

your_desc = input("Tell me a little something about yourself")

You = You("%s is your name" % your_name, "%s" % your_desc)

print("This is You %s" % You)


class Room(object):
    def __init__(self, name, description, s, n, e, w, items):
        self.name = name
        self.desc = description
        self.north = n
        self.south = s
        self.east = e
        self.west = w
        self.items = items

    def move(self, direction):
        global current_node
        current_node = globals()[getattr(self, direction)]


wilderness_day = WildernessDay()
bob_ross_statue = BobRossStatue()

painters_beginning = Room("Painters Beginning", "Well this is ganna ba a great ride with a few items "
                          "not much there only really is paintings you can collect and they have some "
                          "reason to be there but you have to play to find out and this is a maze so "
                          "it might take some time good luck with the maze", "Wilderness", None, None, None,
                          BobRossStatue())

Wilderness = Room("Wilderness", "A Description", None, painters_beginning, None, None, wilderness_day)

wilderness = Wilderness

current_node = painters_beginning
directions = ["north", "south", "east", "west"]
short_directions = ["n", "s", "e", "w"]

bag_of_paintings = []

while True:
    print(current_node.name)
    print(current_node.desc)
    if current_node.items is not None:
        print(current_node.items)
    command = input('>_'.lower())
    if command == 'quit':
        quit(0)
    elif command in short_directions:
        pos = short_directions.index(command)
        command = directions[pos]
    if command in directions:
        try:
            current_node.move(command)
        except KeyError:
            print("You can not go back restart sorry")
    elif 'pick up' in command:
        item_req = input("What item? ")
        if item_req.lower() == current_node.items.name.lower():
            bag_of_paintings.append(current_node.items)
            print("Taken.")
    if command == 'Boring':
        print("Yes it is")
    if command == 'Knock Knock':
        print("Knock-knock - it's Knuckles - the bloat thrower ")
        print("Independent flower ")
        print("Magical Emerald holder ")
        print("Give you the coldest shoulder ")
        print("My spike goes through boulders ")
        print("That's why I stay a loner ")
        print("I was born by myself ")
        print("I don't need a posse - I get it on by myself ")
        print("Adversaries get shelft")
    if command == "look":
        print(current_node.east)
        print(current_node.north)
        print(current_node.south)
        print(current_node.west)