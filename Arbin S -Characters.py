class Fighter(object):
    def __init__(self, name, att1, att2, att3, att4):
        self.name = name
        self.hel = 300
        self.att1 = att1
        self.att2 = att2
        self.att3 = att3
        self.att4 = att4

    def take_damage(self, amt):
        self.hel -= amt


class Mario(Fighter):
    def __init__(self):
        super(Mario, self).__init__("Mario", 'Fireball', 'Super Jump Punch', 'Cape', 'Mario Tornado')

    def attack1(self, target):
        print("You have hit your enemy with a fireball you did some damage")
        target.take_damage(10)

    def attack2(self, target):
        print("You Hit your enemy with a good attack and did nice damage")
        target.take_damage(22)

    def attack3(self, target):
        print("You Caped your enemy and he turned around and got confused did some damage")
        target.take_damage(10)

    def attack4(self, target):
        print("You span into a tornado  and it did great damage")
        target.take_damage(30)


class Luigi(Fighter):
    def __init__(self):
        super(Luigi, self).__init__("Luigi", 'Green Fireball', 'Super Jump Punch', 'Green Misfire', 'Luigi Cyclone')

    def attack1(self, target):
        print("You have hit your enemy with a fireball that spins in one direction you did some damage")
        target.take_damage(10)

    def attack2(self, target):
        print("You Jump up and punch at the same time and did good damage")
        target.take_damage(22)

    def attack3(self, target):
        print("You Caped your enemy and he turned around and got confused did some damage")
        target.take_damage(35)

    def attack4(self, target):
        print("You started to spin into a cyclone and it did great damage")
        target.take_damage(25)


class Peach(Fighter):
    def __init__(self):
        super(Peach, self).__init__("Peach", 'Toad', 'Peach Bomber', 'Peach Parasol', 'Vegetable')

    def attack1(self, target):
        print("You took out toad and contured the attack it did great damage"
              "but you hurt toad")
        target.take_damage(30)

    def attack2(self, target):
        print("You fling yourself towards your enemy and it did good damage")
        target.take_damage(15)

    def attack3(self, target):
        print("You jumped up high and took out your parasol that hit the enemy multiple times "
              "and did good damage")
        target.take_damage(22)

    def attack4(self, target):
        print("You pulled a vegetable out of the ground and threw it and it did some damage")
        target.take_damage(10)


class Fox(Fighter):
    def __init__(self):
        super(Fox, self).__init__("Fox", 'PK Thunder', 'PK Flash', 'PK Fire', 'Bat')

    def attack1(self, target):
        print("You use you demon powers to summon a thunder ball you can control and hit your"
              "self with it and it launches you towards your enemy doing good damage")
        target.take_damage(20)

    def attack2(self, target):
        print("You summon a ball of light with your powers and move it towards your "
              "enemy and it explodes on him doing good damage")
        target.take_damage(25)

    def attack3(self, target):
        print("You shoot a small fire creating a bigger one when it hit your enemy"
              "burning him and doing damage")
        target.take_damage(15)

    def attack4(self, target):
        print("You grab a bat come up to you enemy and swing it hard and it does "
              "great damage")
        target.take_damage(25)


class Yoshi(Fighter):
    def __init__(self):
        super(Yoshi, self).__init__("Yoshi", 'Egg Lay', 'Egg Roll', 'Egg Throw', 'Yoshi Bomb')

    def attack1(self, target):
        print("You shot your tongue out and ate your enemy and lay him in a egg and"
              "you attacked him and great damage")
        target.take_damage(25)

    def attack2(self, target):
        print("You turn yourself into and egg and rolled to your enemy hitting him multiple times")
        target.take_damage(20)

    def attack3(self, target):
        print("You threw and agg to them enemy and did some damage")
        target.take_damage(10)

    def attack4(self, target):
        print("You jump and crashed down into your enemy like a bomb and did good damage")
        target.take_damage(15)


class DonkeyKong(Fighter):
    def __init__(self):
        super(DonkeyKong, self).__init__("DonkeyKong", 'Giant Punch', 'Headbutt', 'Spinning Kong', 'Hand Slap')

    def attack1(self, target):
        print("You Charge up your punch by spinning your hand and punched your enemy with a strong punch")
        target.take_damage(30)

    def attack2(self, target):
        print("You Fling your head to your enemy and he got stuck in the ground and you land "
              "some good hits")
        target.take_damage(35)

    def attack3(self, target):
        print("You use the muscles on your arms and start to spin around hit your enemy and"
              "did some good damage")
        target.take_damage(20)

    def attack4(self, target):
        print("You slam your hands into the ground and slam your enemy and did good damage")
        target.take_damage(20)


class CaptainFalcon(Fighter):
    def __init__(self):
        super(CaptainFalcon, self).__init__("CaptainFalcon", 'KNEE', 'Falcon Punch', 'Falcon Dive', 'Falcon Kick')

    def attack1(self, target):
        print("You use your knee of justice and did massive damage")
        target.take_damage(45)

    def attack2(self, target):
        print("Your hand burst into flames as you throw a strong punch at your enemy")
        target.take_damage(35)

    def attack3(self, target):
        print("You launch up to your enemy after you kick them up and your fist turn into"
              "fire and you grab your enemy and cause a small BOOM causing good damage")
        target.take_damage(30)

    def attack4(self, target):
        print("You fly towards your enemy with your foot in front and it turns into flames"
              "and you hit your enemy with good damage")
        target.take_damage(20)


class Link(Fighter):
    def __init__(self):
        super(Link, self).__init__("Link", 'Bow', 'Boomerang Combo', 'Hero Spin', 'Bomb')

    def attack1(self, target):
        print("You take out your bow holding back the arrow and shoot it at your enemy it did"
              "some damage")
        target.take_damage(15)

    def attack2(self, target):
        print("You throw your boomerang at full speed and it turns into a small "
              "tornado and it drags your enemy towards you and you land a strong attack")
        target.take_damage(20)

    def attack3(self, target):
        print("You use your sword to spin around and it makes a light due to the power"
              "of the Master Sword and you hit your enemy multiple times")
        target.take_damage(25)

    def attack4(self, target):
        print("You grab a bomb and light it and threw it to your enemy and it exploded "
              "on them it did good damage")
        target.take_damage(15)


class Samus(Fighter):
    def __init__(self):
        super(Samus, self).__init__("Samus", 'Charge Shot', 'Missile', 'Screw Attack', 'Cover Fire')

    def attack1(self, target):
        print("You charge up a energy ball with your special suit and shoot it at"
              "you enemy and did great damage")
        target.take_damage(30)

    def attack2(self, target):
        print("You shoot a missile at your enemy fom your special suit and it hits your enemy")
        target.take_damage(15)

    def attack3(self, target):
        print("You launch up and spin and while spinning you suit lefts off electricity"
              "and hits you enemy multiple times")
        target.take_damage(20)

    def attack4(self, target):
        print("You let out small explosions from your hand and use it as a attack "
              "and it does good damage")
        target.take_damage(20)


class Kirby(Fighter):
    def __init__(self):
        super(Kirby, self).__init__("Kirby", 'Hammer', 'Absorb', 'Final Cutter', 'Stone')

    def attack1(self, target):
        print("You pull out a hammer and it begins to slowly set on fire and"
              "you use it to hit your enemy and he catches on fire")
        target.take_damage(30)

    def attack2(self, target):
        print("You begin to absorb you enemy with your special powers and take one of "
              "the enemies attacks and use it against him")
        target.take_damage(35)

    def attack3(self, target):
        print("You take out a sword and slash your enemy up and back down and you hit "
              "him with a light attack")
        target.take_damage(20)

    def attack4(self, target):
        print("You jump above your enemy and use your special powers and turn into "
              "a stone and land on your enemy")
        target.take_damage(25)


class Pikachu(Fighter):
    def __init__(self):
        super(Pikachu, self).__init__("Pikachu", 'Thunder Jolt', 'Skull Bash', 'Quick Attack', 'Thunder')

    def attack1(self, target):
        print("You shoot a ball of lightning and it stuns you enemy and did some damage")
        target.take_damage(10)

    def attack2(self, target):
        print("You fling yourself towards your enemy and hit him with your head")
        target.take_damage(20)

    def attack3(self, target):
        print("You begin to speed up and lighting flashes out of you cause of the "
              "speed and you attack him with the speed")
        target.take_damage(15)

    def attack4(self, target):
        print("You summon a thunder cloud and it strikes you and your enemy but you don't take damage")
        target.take_damage(25)


class Jigglypuff(Fighter):
    def __init__(self):
        super(Jigglypuff, self).__init__("Jigglypuff", 'R E S T', 'Rollout', 'Pound', 'Back Air')

    def attack1(self, target):
        print("You walk up to your enemy and rest in front of your enemy but "
              "your special power launch your enemy and he took a lot of damage")
        target.take_damage(35)

    def attack2(self, target):
        print("You begin to spin in place and rollout to your enemy and hit them")
        target.take_damage(20)

    def attack3(self, target):
        print("You slap your enemy really hard and it feels like they were pounded by you")
        target.take_damage(15)

    def attack4(self, target):
        print("You jump above your enemy and you spin and kick them behind you")
        target.take_damage(15)


class Ness(Fighter):
    def __init__(self):
        super(Ness, self).__init__("Ness", 'PK Flash', 'PK Thunder', 'PK Fire', 'Bat')

    def attack1(self, target):
        print("You use your demon powers and summon a flashy ball of light energy "
              "and control it and move it towards you enemy and it explodes on him")
        target.take_damage(20)

    def attack2(self, target):
        print("You summon a thunder ball you can control and you hit your self with it"
              "but it launches you towards you enemy and it hits and a lot")
        target.take_damage(20)

    def attack3(self, target):
        print("You summon a small fire towards your enemy and it hits him then makes"
              "a bigger fire burning him ")
        target.take_damage(15)

    def attack4(self, target):
        print("You pull out a bat and you hit you enemy really hard and doing great damage")
        target.take_damage(20)


class Bowser(Fighter):
    def __init__(self):
        super(Bowser, self).__init__("Bowser", 'Fire Breath', 'Koopa Claw', 'Whirling Fortress', 'Bowser Bomb')

    def attack1(self, target):
        print("You breath fire hitting your enemy burning him")
        target.take_damage(15)

    def attack2(self, target):
        print("You use your claws to get a good grip on your enemy and you jump up while"
              "holding him and slam on your enemy")
        target.take_damage(20)

    def attack3(self, target):
        print("You come up to your enemy and get into your shell as you spin and hit"
              "your enemy with you spikes on your shell")
        target.take_damage(20)

    def attack4(self, target):
        print("You jump up high into the air and come rushing down and smash your enemy")
        target.take_damage(25)


class Zelda(Fighter):
    def __init__(self):
        super(Zelda, self).__init__("Zelda", "Nayru's Love", "Din's Fire", "Farore's Wind", 'Lighting Kick')

    def attack1(self, target):
        print("You summon a crystal that can reflect projectiles and hurt your enemy and you "
              "use it on your enemy spinning and doing damage")
        target.take_damage(15)

    def attack2(self, target):
        print("You summon a flashy ball that you can control and move it towards you enemy "
              "that explodes on him")
        target.take_damage(15)

    def attack3(self, target):
        print("You spin around and teleport where you enemy is and when you appear and explosion "
              "pops to move anything in the way and it hits you enemy")
        target.take_damage(20)

    def attack4(self, target):
        print("You jump up and kick your enemy but its not a normal kick because the power"
              " of hyrule you have turns your kick into a lighting one and does good damage")
        target.take_damage(20)


class Sheik(Fighter):
    def __init__(self):
        super(Sheik, self).__init__("Sheik", 'Needle Strom', 'Chain', 'Vanish', 'Bouncing Fish')

    def attack1(self, target):
        print("You grab small throwing knifes one at a time and then rapidly throw it "
              "at your enemy cutting him and doing some damage")
        target.take_damage(15)

    def attack2(self, target):
        print("You throw a chain at your enemy but it has a electric tip and you hit "
              "them with it electrocuting them ")
        target.take_damage(15)

    def attack3(self, target):
        print("You vanish in thin air but appear in front of your enemy but before you do "
              "there is a small explosion that hurts your enemy before you appear again")
        target.take_damage(20)

    def attack4(self, target):
        print("You jump up high into the air and like a fish you use your legs to swing your "
              "self towards your enemy and hitting them with your legs and a bouncing fish")
        target.take_damage(15)


class Ganondorf(Fighter):
    def __init__(self):
        super(Ganondorf, self).__init__("Ganondorf", 'Warlock Punch', 'Gerudo Dragon', 'Dark Drive', "Wizard's Foot")

    def attack1(self, target):
        print("You use your dark powers and release a huge amount while you punch"
              "your enemy with a lot of force")
        target.take_damage(35)

    def attack2(self, target):
        print("You rush towards your enemy with a dark power and uppercut your enemy into the air")
        target.take_damage(20)

    def attack3(self, target):
        print("You run up to your enemy hit him into the air and jump and grab your enemy"
              "in mid air and a small dark explosion pops and deals good damage at your enemy")
        target.take_damage(20)

    def attack4(self, target):
        print("You use your dark powers and kick in the air and with your powers you"
              "rush towards your enemy foot first kicking him")
        target.take_damage(15)


class DrMario(Fighter):
    def __init__(self):
        super(DrMario, self).__init__("DrMario", 'Megavitamins', 'Super Sheet', 'Super Jump Punch', 'Dr. Tornado')

    def attack1(self, target):
        print("You throw a vitamin that is much lager than a normal on and you hit your enemy with it")
        target.take_damage(10)

    def attack2(self, target):
        print("You take out a sheet and spin your enemy around and hit him with an attack")
        target.take_damage(15)

    def attack3(self, target):
        print("You walk up to your enemy and uppercut them into the air doing damage")
        target.take_damage(20)

    def attack4(self, target):
        print("You spin like a tornado and trap your enemy inside while hitting them")
        target.take_damage(15)


class YoungLink(Fighter):
    def __init__(self):
        super(YoungLink, self).__init__("YoungLink", 'Bow', 'Bomb', 'Spin Attack', 'Boomerang')

    def attack1(self, target):
        print("You take a bow out but you aren't as strong as link so your arrow aims "
              "high but you still manage to hit your enemy ")
        target.take_damage(15)

    def attack2(self, target):
        print("You take out a bomb that you make and throw it at your enemy "
              "it makes a small explosion but it sill does some damage")
        target.take_damage(15)

    def attack3(self, target):
        print("You run towards your enemy and get next to him to do a spin attack "
              "hitting your enemy with your sword")
        target.take_damage(20)

    def attack4(self, target):
        print("You throw a boomerang at your enemy hitting him and coming back to you")
        target.take_damage(15)


class Falco(Fighter):
    def __init__(self):
        super(Falco, self).__init__("Falco", 'Blaster Combo', 'Falco Phantasm', 'Fire Bird', 'Shine')

    def attack1(self, target):
        print("You shoot your enemy with a laser that causes a small stun and you use"
              "that small time to attack and stun a again and land a combo ")
        target.take_damage(20)

    def attack2(self, target):
        print("You run to your enemy and in a flash you end up behind him but you hit your "
              "enemy while you get behind him so fast")
        target.take_damage(15)

    def attack3(self, target):
        print("You run next to your enemy and flame up and launch yourself into the air"
              "with your enemy burning him and doing damage")
        target.take_damage(20)

    def attack4(self, target):
        print("You shoot your enemy with your blaster and then you take out your reflector that "
              "can damage your enemy so you use it asa shine it hits you enemy and land a great combo")
        target.take_damage(35)


class Mewtwo(Fighter):
    def __init__(self):
        super(Mewtwo, self).__init__("Mewtwo", 'Shadowball', 'Confusion', 'Teleport', 'Disable Combo')

    def attack1(self, target):
        print("You charge up a dark ball called a shadow ball and shoot it at your enemy")
        target.take_damage(25)

    def attack2(self, target):
        print("You use your telekinesis and grab your enemy and spin them around")
        target.take_damage(10)

    def attack3(self, target):
        print("You teleport behind your enemy and throw them into the air and while they fall "
              "you hit them with a good attack")
        target.take_damage(20)

    def attack4(self, target):
        print("You come up to your enemy and flash a light in there eyes tht stuns them and then "
              "you charge up a dark power from your finger tips and shoot it at the ground exploding "
              "under them doing great damage")
        target.take_damage(25)


class Pichu(Fighter):
    def __init__(self):
        super(Pichu, self).__init__("Pichu", 'Thunder Jolt', 'Skull Bash', 'Agility', 'Thunder')

    def attack1(self, target):
        print("You shoot a small thunder jolt and hit your enemy")
        target.take_damage(10)

    def attack2(self, target):
        print("You charge up to launch yourself at your enemy and you "
              "fly to your enemy and hit them with your head")
        target.take_damage(15)

    def attack3(self, target):
        print("You dash to your enemy really fast and hit him when you dash")
        target.take_damage(15)

    def attack4(self, target):
        print("You make a thunder cloud and and hit your self and your enemy with it ")
        target.take_damage(20)


class IceClimbers(Fighter):
    def __init__(self):
        super(IceClimbers, self).__init__("IceClimbers", 'Ice Shot', 'Squall Hammer', 'Belay Combo', 'Blizzard')

    def attack1(self, target):
        print("You shoot an ice block at your enemy and it hit them hard")
        target.take_damage(15)

    def attack2(self, target):
        print("You and your buddy spin around together and use your hammers as a weapon "
              "to hit your enemy multiple times")
        target.take_damage(20)

    def attack3(self, target):
        print("You throw your buddy in the air and behind your enemy and he hit them towards you "
              "and you use your hammer and hit them hard like a combo")
        target.take_damage(20)

    def attack4(self, target):
        print("You summon some ice and it spins around you like a blizzard and it hits you enemy "
              "freezing them and hitting them")
        target.take_damage(25)


class MrGameAndWatch(Fighter):
    def __init__(self):
        super(MrGameAndWatch, self).__init__("MrGameAndWatch", 'Chef', 'Might Number 9', 'FIRE!', 'Oil Panic')

    def attack1(self, target):
        print("You cook up some food and throw it at your enemy with a pan")
        target.take_damage(10)

    def attack2(self, target):
        print("You take out a judgement card and it shows the number nine the strongest"
              "out of all and you pull out a hammer and it hits your enemy with a great strength")
        target.take_damage(40)

    def attack3(self, target):
        print("You hit your enemy into the sky and then two guys come out and you jump on the "
              "trampoline they took out and you launch into the air and hit your enemy with a "
              "headbutt and come down safely on a parachute")
        target.take_damage(20)

    def attack4(self, target):
        print("You take out a bucket with a strange liquid and throw it at your enemy and it "
              "hit them hard")
        target.take_damage(35)


class Marth(Fighter):
    def __init__(self):
        super(Marth, self).__init__("Marth", 'Shield Breaker', 'Dancing Blade', 'Dolphin Slash', 'Counter')

    def attack1(self, target):
        print("You hold your sword over your head and with full power you thrust your sword at your "
              "enemy and it hit them hard")
        target.take_damage(30)

    def attack2(self, target):
        print("You do a sequence of many slashes like a dance hitting your enemy multiple times ")
        target.take_damage(20)

    def attack3(self, target):
        print("You jump up high with a quick uppercut with your sword at full speed slashing "
              "your enemy ")
        target.take_damage(20)

    def attack4(self, target):
        print("You stand still and your enemy rushes at you and you counter it right before he hits "
              "you ")
        target.take_damage(20)


class Roy(Fighter):
    def __init__(self):
        super(Roy, self).__init__("Roy", 'Flare Blade', 'Double Edge Blade', 'Blazer', 'Counter')

    def attack1(self, target):
        print("You put your blade behind you over your shoulder and it begins to flare up and "
              "blaze and then you hit your enemy with a explosion of fire ")
        target.take_damage(25)

    def attack2(self, target):
        print("You begin to slash at your enemy with many hits and at the end you hit him "
              "with s good slash")
        target.take_damage(20)

    def attack3(self, target):
        print("You uppercut with your sword with a fire trail under you as you jump "
              "burning your enemy ")
        target.take_damage(20)

    def attack4(self, target):
        print("You stay still and wait for your enemy to attack and he rushes at you but you"
              "counter him before he does")
        target.take_damage(20)

