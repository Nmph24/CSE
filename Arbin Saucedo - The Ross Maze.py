class Item(object):
    def __init__(self, name):
        self.name = name

    def pick_up(self):
        print("You have picked up %s" % self.name)


class Statue(Item):
    def __init__(self, name, desc):
        super(Statue, self).__init__(name)
        self.desc = desc


class BobRossStatue(Statue):
    def __init__(self):
        super(BobRossStatue, self).__init__("Bob Ross Statue", "A Bob Ross Statue look nice and"
                                                               " it is detailed greatly")


class Paintings(Item):
    def __init__(self, name, desc):
        super(Paintings, self).__init__(name)
        self.desc = desc


class WildernessDay(Paintings):
    def __init__(self):
        super(WildernessDay, self).__init__("Wilderness Day", "Wilderness Day was a painting and the " 
                                            "last one Bob Ross painted and it shows a forest with a sun "
                                            "down as it time and a path way made of rocks")


class InTheMidstOfWinter(Paintings):
    def __init__(self):
        super(InTheMidstOfWinter, self).__init__("In The Midst Of Winter", "In The Midst of Winter really "
                                                 "speaks for it self in it nice winter forest and it"
                                                 "small cabin and the trees around it that are dead."
                                                 "The winter is harsh but nice")


class LakeAtTheRidge(Paintings):
    def __init__(self):
        super(LakeAtTheRidge, self).__init__("Late At The Ridge", "This painting has a view of snowy mountains "
                                             " in the distant and a shining lake with a cloudy blue sky and green"
                                             "trees and grasses")


class BalmyBeach(Paintings):
    def __init__(self):
        super(BalmyBeach, self).__init__("Balmy Beach", "You can see an ocean with a sun down and a nice pink sky"
                                         "there are also some small waves crashing by and some palm trees")
        

class EvergreenValley(Paintings):
    def __init__(self):
        super(EvergreenValley, self).__init__("Evergreen Valley", "A nice snowy mountain in the distant and tall "
                                              "green trees with a small trail amd a pink blue sky in this painting")
    
    
class TrailsEnd(Paintings):
    def __init__(self):
        super(TrailsEnd, self).__init__("Trail's End", "This painting is showing a tree with no leaves in front "
                                        "but behind it there is a trail and a lot of orange autumn trees")
        
        
class BridgeToAutumn(Paintings):
    def __init__(self):
        super(BridgeToAutumn, self).__init__("Bridge To Autumn", "In This one there is a small wooden shelter "
                                             "with a lake behind it and the autumn trees on the other side of the "
                                             "lake and a small rock trail leading to the shelter")
       
        
class ViewFromClearCreek(Paintings):
    def __init__(self):
        super(ViewFromClearCreek, self).__init__("View From Clear Creek", "A site of a creek, a small river, tall"
                                                 "green grass and tall trees with mountains and hills in the distance"
                                                 "what a nice painting of this creek")
    
    
class CabinInTheHollow(Paintings):
    def __init__(self):
        super(CabinInTheHollow, self).__init__("Cabin In The Hollow", "A snowy forest with trees with pink leaves, "
                                               "a frozen lake, some fences and a cabin with snow on top this "
                                               "this painting really shows how it gets during winter in snowy areas")
    
    
class TranquilityCove(Paintings):
    def __init__(self):
        super(TranquilityCove, self).__init__("Tranquility Cove", "A painting with a river and some trees in the "
                                              "beginning of autumn with orange grenns grass and tress with the same "
                                              "color")


class WindingStream(Paintings):
    def __init__(self):
        super(WindingStream, self).__init__("Winding Stream", "This painting shows a trail, some tall trees next to "
                                            "it and mountains in the distant background with a blue sky")


class ReflectionsOfCalm(Paintings):
    def __init__(self):
        super(ReflectionsOfCalm, self).__init__("Reflections Of Calm", "This painting speaks for itself with the nice"
                                                "reflecting lake and the mountains in the back with trees and rocks "
                                                "surrounding the lake and a blue sky to top it all off")


class BlueRidgeFalls(Paintings):
    def __init__(self):
        super(BlueRidgeFalls, self).__init__("Blue Ridge Falls", "A nice waterfall that is being split by a rock "
                                             "surrounded but tall green trees and under it is the river current it"
                                             "is making what a nice painting")


class EveningsGlow(Paintings):
    def __init__(self):
        super(EveningsGlow, self).__init__("Evening's Glow", "Another Painting that can speak for itself. This one"
                                           "has a shining sun in the distant with a few mountains and its barely "
                                           "becoming day. It has a trail leading to a small cabin with trees behind"
                                           " it and a river as well next to it")


class SeasideHarmony(Paintings):
    def __init__(self):
        super(SeasideHarmony, self).__init__("Seaside Harmony", "A painting with the ocean and a cloudy pink sky with"
                                             "waves crashing against some rocks on the shore")


class AWalkInTheWoods(Paintings):
    def __init__(self):
        super(AWalkInTheWoods, self).__init__("A Walk In The Woods", "The first every painting Bob Ross made and "
                                              "it is pretty just like the rest. This painting has a small water "
                                              "lake with a trail leading towards it and autumn trees surrounding "
                                              "the trail and the small body of water with an orange sky")

    
class You(object):
    def __init__(self, name, desc):
        self.name = name
        self.desc = desc

    def note(self):
        print("%s " % self.name)


your_name = input("What is your name? ")
print("Nice to meet you %s" % your_name)

your_desc = input("Tell me a little something about yourself")

You = You("%s is your name" % your_name, "and you are %s" % your_desc)

print(You.name, You. desc)


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

Wilderness = Room("Wilderness", "A Description", None, "painters_beginning", None, None, wilderness_day)

wilderness = Wilderness

current_node = painters_beginning
directions = ["north", "south", "east", "west"]
short_directions = ["n", "s", "e", "w"]

bag_of_paintings = []

while True:
    print(current_node.name)
    print(current_node.desc)
    if current_node.items is not None:
        print(current_node.items.name)
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
            print("You can not go that way")
    elif 'pick up' in command:
        item_req = input("What item? ")
        if item_req.lower() == current_node.items.name.lower():
            bag_of_paintings.append(current_node.items)
            print("Taken.")
        else:
            print("Item not Picked Up")
    elif "look at" in command:
        for Item in bag_of_paintings:
            if Item.name in command:
                print(Item.name)
                print(Item.desc)
    elif command == 'inventory':
        for Item in bag_of_paintings:
            print(Item.name)
    if command == 'Inventory':
        print(bag_of_paintings)
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
