silly_melee = {
    'JOURNEYHALLWAY': {
        'NAME': "Journey's Beginning",
        'DESCRIPTION': "You have arrived at a hallway that will lead you into "
                       "many battles in this world to show your the best fighter out there",
        'PATHS': {
            'e': 'TANGERINESCASTLE',
            's': 'TEMPLE'
        }
    },
    'TANGERINESCASTLE': {
        'NAME': "Tangerine's Castle",
        'DESCRIPTION': "The Castle of the Olive Kingdom and your first fight "
                       "with Princess Peach and after this your adventure will start"
                       "now FIGHT",
        'PATHS': {
            'e': 'OLIVEKINGDOM',
            's': 'FOUNTAINOFSLEEP'
        }
    },
    'TEMPLE': {
        'NAME': 'Temple',
        'DESCRIPTION': "The Lowrule Temple where your first fight begins"
                       "with Princess Zelda so get ready to start your battle"
                       "with many fighters all of different powers",
        'PATHS': {
            's': 'COLDPLACE',
            'e': 'FOUNTAINOFSLEEP'
        },
    },
    'FOUNTAINOFSLEEP': {
        'NAME': 'Fountain Of Sleep',
        'DESCRIPTION': "Now you are extra sleepy but you can fight still "
                       "so be happy for that but you now you up against "
                       "a harder characters because you have chosen the short "
                       "but harder path to the end so you are up against "
                       "jugglypuff played by HBox",
        'PATHS': {
            'e': 'BLUEBLUES',
        },
    },
    'BLUEBLUES': {
        'NAME': 'Blue Blues',
        'DESCRIPTION': "Now it gets harder from here in blue blues so now "
                       "your up against sheik played by Plup ,so good "
                       "luck cause its a top tier",
        'PATHS': {
            'e': 'GRENDINOISLAND64',
        },
    },
    'GRENDINOISLAND64': {
        'NAME': 'Gren Dino Island N64',
        'DESCRIPTION': "SOOO you close to finishing your rage inducing trip"
                       "but you still have another one after this sooo, well"
                       "nevermind thagt but now you are up against Marth"
                       "played by Mew2King so don't let him grab you",
        'PATHS': {
            'e': 'DREAMLAND64',
        },
    },
    'DREAMLAND64': {
        'NAME': 'Dream Land N64',
        'DESCRIPTION': "Welp you got 2 more left and they are both bosses "
                       "but this one is like a semi-boss so good luck cause "
                       "now you are up against Fox played by Armada",
        'PATHS': {
            'n': 'WIP',
            'e': 'WIP'
        },
    },
    'OLIVEKINGDOM': {
        'NAME': 'Olive Kingdom',
        'DESCRIPTION': "This is the Olive Kingdom the home of Mario,"
                       "Dr.Mario, Peach, Bowser, and Luigi and here you will be "
                       "fighting Mario so good luck now START",
        'PATHS': {
            'e': 'OLIVEKINGDOM2',
        },
    },
    'COLDPLACE': {
        'NAME': 'Cold Place',
        'DESCRIPTION': "The Coldest place out of this whole world"
                       "which is also mount everest and here you "
                       "are fighting 2 people that are one fighther"
                       "and there name is Ice Climbers",
        'PATHS': {
            's': 'LOUDCITY',
        },
    },
    'OLIVEKINGDOM2': {
        'NAME': 'Olive Kingdom 2',
        'DESCRIPTION': "This is the other side of the Olive Kingdom where you "
                       "are slowly entering the jungle to fight someone else "
                       "but for now you up against Luigi",
        'PATHS': {
            'e': 'JUNGLEJAPS'
        },
    },
    'LOUDCITY': {
        'NAME': 'Loud City',
        'DESCRIPTION': "Loud city is a city with many racers in this place and there"
                       "are a lot of tournaments in this place for racing but you find"
                       "a small mice that seems to be electrical and his name is Pichu"
                       "and he is your next opponent",
        'PATHS': {
            's': 'SMALLRED',
        },
    },
    'JUNGLEJAPS': {
        'NAME': 'Jungle Japs',
        'DESCRIPTION': "Well now your up against the king of the jungle "
                       "DK careful he can pack a good punch so good luck "
                       "and watch out for his fist",
        'PATHS': {
            's': 'KONGOJUNGLE',
        },
    },
    'SMALLRED': {
        'NAME': 'Small Red',
        'DESCRIPTION': "Now you gotta show your moves and make sure you "
                       "don't fall off of a super fast car but you still "
                       "to fight against Captain Falcon so START",
        'PATHS': {
            'e': 'FIVESIDES',
        },
    },
    'KONGOJUNGLE': {
        'NAME': 'Kongo Jungle',
        'DESCRIPTION': "Well sometimes you won't be up against people in "
                       "there desired places but your up against Dr.Mario ",
        'PATHS': {
            's': 'WIP',
        },
    },
    'FIVESIDES': {
        'NAME': 'Five Sides',
        'DESCRIPTION': "Now your in another city near a store which is "
                       "your next location but for now you are fighting"
                       "Ness which is a boy with magical powers",
        'PATHS': {
            'e': 'DREAMLAND64',
        },
    },
}

current_node = silly_melee['JOURNEYHALLWAY']
directions = ["w", "n", "s", "e"]

while True:
    print(current_node['NAME'])
    print(current_node['DESCRIPTION'])
    print(current_node['PATHS'])
    command = input('>_')
    if command == 'quit':
        quit(0)
    if command in directions:
        try:
            name_of_node = current_node['PATHS'][command]
            current_node = silly_melee[name_of_node]
        except KeyError:
            print("You can not go back now keep fighting")
    if command == 'JV3':
        print("git gud")
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
    else:
        print('Command Not Recognized')


