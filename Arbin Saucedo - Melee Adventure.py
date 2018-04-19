class Item(object):
    def __init__(self, name):
        self.name = name

    def pick_up(self):
        print("You have picked up an item")


class Health(Item):
    def __init__(self, name):
        super(Health, self).__init__(name)

    def heal(self):
        print("You have healed yourself with healing item")


class Fairy_bottle(Health):
    def __init__(self, name):
        super(Fairy_bottle, self).__init__(name)

    def bottle_healing(self, target):
        if target.health < 100:
            target.health += 100


class Heart_container(Health):
    def __init__(self, name):
        super(Heart_container, self).__init__(name)

    def container_heal(self, target):
        if target.health < 300:
            target.health += 100


class Food(Health):
    def __init__(self, name):
        super(Food, self).__init__(name)

    def food_heal(self, target):
        if target.health < 300:
            target.health += 10


class Fighting_item(Item):
    def __init__(self, name):
        super(Fighting_item, self).__init__(name)


class SuperStrong(Fighting_item):
    def __init__(self, name, damage):
        super(SuperStrong, self).__init__(name)


class xbomb(SuperStrong):
    def __init__(self, name):
        super(xbomb, self).__init__(name, 65)

    def xboom(self):
        print("X-Bomb has exploded and damaged you damaged enemy")


class Masterball(SuperStrong):
    def __init__(self, name):
        super(Masterball, self).__init__(name, 80)

    def legendarypoke(self):
        print("You have spawned in a legendary pokemon that hurts your "
              "enemy badly")


class HomeRunBat(SuperStrong):
    def __init__(self, name):
        super(HomeRunBat, self).__init__(name, 100)

    def HOMERUN(self):
        print("YOU HUT A HOME RUN AND DID HUGE DAMAGE TO YOUR ENEMY")


class bob_omb(SuperStrong):
    def __init__(self, name):
        super(bob_omb, self).__init__(name, 80)

    def BIGBOOM(self):
        print("You threw a Bob-Omb and did a lat a damege")


class SmashBall(SuperStrong):
    def __init__(self, name):
        super(SmashBall, self).__init__(name, 150)

    def SMASH(self):
        print("You have Unleashed your final move on your opponent "
              "and caused MASSIVE Damage")


class MeleeItems(Fighting_item):
    def __init__(self, name, damage):
        super(MeleeItems, self).__init__(name)


class Fan(MeleeItems):
    def __init__(self, name):
        super(Fan, self).__init__(name, 15)

    def wak(self):
        print("You have waked the Hecc out of your enemy")


class Fire_flower(MeleeItems):
    def __init__(self, name):
        super(Fire_flower, self).__init__(name, 30)

    def burn(self):
        print("You burned your enemy it did decent damage")


class Beam_sword(MeleeItems):
    def __init__(self, name):
        super(Beam_sword, self).__init__(name, 40)

    def beam_slash(self):
        print("You slashed your enemy with a beam it did good damage")


class RangedItems(Fighting_item):
    def __init__(self, name, damage):
        super(RangedItems, self).__init__(name)


class green_shell(RangedItems):
    def __init__(self, name):
        super(green_shell, self).__init__(name, 20)

    def shelled(self):
        print("You hit your enemy with a green shell nice shot")


class ray_gun(RangedItems):
    def __init__(self, name):
        super(ray_gun, self).__init__(name, 55)

    def pew_pew(self):
        print("You keep shooting a your enemy and it did good damage also pew pew")


class Freezie(RangedItems):
    def __init__(self, name):
        super(Freezie, self).__init__(name, 10)

    def frozen(self):
        print("You have froze your enemey attack him with what you got")


class Pokeball(RangedItems):
    def __init__(self, name):
        super(Pokeball, self).__init__(name, 75)

    def pokemon(self):
        print("You threw the pokeball and a pokemon came out and attacked your enemey")


class MrSaturn(RangedItems):
    def __init__(self, name):
        super(MrSaturn, self).__init__(name, 5)

    def stun(self):
        print("You threw Mr.Saturn and it hit your enemy if he had his shield on he was stunned"
              "if not it didn't do much damage")


class Keys(Item):
    def __init__(self, name):
        super(Keys, self).__init__(name)


class DL64key(Keys):
    def __init__(self, name):
        super(DL64key, self).__init__(name)

    def closedl64(self):
        print("You have picked up the key that gets you closer to the end")


class KJ64key(Keys):
    def __init__(self, name):
        super(KJ64key, self).__init__(name)

    def closekj64(self):
        print("You are getting closer to the end")


class GDI(Keys):
    def __init__(self, name):
        super(GDI, self).__init__(name)

    def closegdi(self):
        print("There are other keys but if you find them then the end is close")


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


class Room(object):
    def __init__(self, name, description, enemey, s, n, e, w):
        self.name = name
        self.desc = description
        self.fighters = enemey
        self.north = n
        self.south = s
        self.east = e
        self.west = w

    def move(self, direction):
        global current_node
        current_node = globals()[getattr(self, direction)]


journey_hallway = Room("Journey Hall", "You have arrived at a hallway that will lead you into "
                       "many battles in this world and you need show your the best fighter out there",
                       None, 'Temple', None, 'Tangerine_Castle', None)

Temple = Room("Temple", "Des: This Temple is where your first fight begins"
              "with Princess Zelda good luck with the fight and the others that come with many more"
              "fighters you will face", "Fighter: Zelda", "N: Cold_Place", "S: None", "E: Fountain_Of_Sleep",
              "W: None")

Tangerine_Castle = Room("Tangerine Castle", "The Castle of the Olive Kingdom and your first fight "
                        "with Princess Tangerine", "Princess Peach", "Fountain_Of_Sleep", None,
                        "Olive_Kingdom", None)

Fountain_Of_Sleep = Room("Fountain Of Sleep", "Now you are extra sleepy but you can fight still "
                         "so be happy for that but you now you up against "
                         "a harder characters because you have chosen the short "
                         "but harder path to the end so you are up against "
                         "Jigglypuff", "Jigglypuff played by HBox", None, None,
                         "Blue_Blues", None)

Olive_Kingdom = Room("Olive Kingdom", "This is the Olive Kingdom the home of Mario,"
                     "Dr.Mario, and Luigi and here you will be Fighting Mario so START"
                     , "Mario", None, None, "Olive_Kingdom_2", None)

Cold_Place = Room("Cold Place", "The Coldest place out of this whole world"
                  "which is also mount everest and here you "
                  "are fighting 2 people that are one fighther"
                  "Ice Climbers", "Ice Climbers", "Loud_City", None, None, None)

Blue_Blues = Room("Blue Blues", "Now it gets harder from here in blue blues so now "
                  "your up against Sheik played by Plup ,so good luck cause its a top tier",
                   "Shiek", None, None, "Gren_Dino_Island64",None)

Olive_Kingdom_2 = Room("Olive Kingdom 2", "This is the other side of the Olive Kingdom where you "
                       "are slowly entering the jungle to fight someone else "
                       "but for now you up against Luigi", "Luigi", None, None, "Jungle_Japes", None)

Loud_City = Room("Loud City", "Well your in the city know and well this place looks like it has more of "
                 "an advance in car technology and there is still fighters here so don't"
                 "let the cars distract you anyways now your up against Pichu a small mice but "
                 "don't let that fool you he still packs a good punch", "Pichu", "Small_Red",
                 None, None, None)

Gren_Dino_Island64 = Room("Gren Dino Island 64", "SOOO you close to finishing your rage inducing trip"
                          "but you still have another one after this sooo, well never mind that but now you "
                          "are up against Marth so don't let him grab you from across the stage",
                          "Marth", None, None, "Dream_Land64", None)

Jungle_Japes = Room("Jungle Japs", "So they're finally here, performing for you If you know the words"
                    "you can join in to, Put you hand together, if you want to clap as we take you "
                    "through this monkey rap DK DONKEY KONG. Well you may have guessed it already that"
                    "your up against Donkey Kong king of the jungle so get ready to fight",
                    "Donkey Kong", None, None, "Kongo_Jungle", None)


Small_Red = Room("Small Red", "Small Red is a car not a map I don't know how you ended up on this car"
                 "but I am pretty sure the driver is kinda mad and he is well then there is Captain Falcon"
                 "Good luck because this man is really buff and has a very strong Knee so watch out for that",
                 "Captain Falcon", None, None, "Five_Sides", None)

Dream_Land64 = Room("Dream Land 64", "Well you got 2 rooms left if you have all the keys that is anyway"
                    "the last 2 are both bosses but this one is like a semi-boss so good luck cause "
                    "now you are up against Fox played by Armada", "Fox", None,
                    "Final_Hallway", "Key_Room", None)

Kongo_Jungle = Room("Kongo Jungle", "You mange to beat up DK but no Diddy Kong is mad at you so fight em cause"
                    "that is the only way to resolve anything in this world so get ready to fight ",
                    "Diddy Kong", None, "Good_Bay", None, None)

Five_Sides = Room("Five Sides", "Now you have fallen off of the super fast car that you were fighting on and"
                  "You have ended up in the big city but that doesn't mean you are free to do what ever you want"
                  "you still have a lot of people to fight just like now and your fighting Bowser who was here for"
                  "a brake but is fighting you now", "Bowser", None, None, "Onett", None)

Good_Bay = Room("Good Bay", "Well you made it out of the jungle but now your in a nice bay area"
                "very pretty place but that does not mean you journey is over you still have "
                "a long way to go but now you are fighting Link", "Link", "Pokefloats", None,
                None, None)

Onett = Room("Onett", "You left the big city after your fight with Bowser and now your in a small "
             "town and your at its medicine shop called Onett but your still not done fighting"
             "you are fighting Ness in his home town and he is not or normal kid watch out", "Ness",
             None, None, "Corneria", None)

Pokefloats = Room("Pokefloats", "You manage to beat Link but you somehow get to a float show with many "
                  "floats from pokemon and you happen to land on one of them and they start to inflate them"
                  "so now your in the air but there is still a challenger and his name is Pikachu", "Pikachu",
                  "Pokestadium", None, None, None)

Corneria = Room("Cornria", "Away from the small city you get on a ship to get away but there is someone "
                "else in the ship he shoots at you and you jump on top of the ship and there is the "
                "captain of the ship Falco the blue bird of the glaxies and he is your next opponent",
                "Falco", None, None, "Venom", None)

Pokestadium = Room("Pokestadium", "You made it off the floats and won against Pikachu but you now your at "
                   "a stadium for pokemon fights and you feel a weird pressure coming from the shadows "
                   "then a ball of dark energy launches at you but you dodge it and now your next fight"
                   "begins against Mewtwo careful not to look him in the eyes up close he has a special "
                   "that confuses you to get comboed so take care ", "Mewtwo", None, None, None,
                   "Rainbowcruise")

Venom = Room("Venom", "That should have been the only person there but there was someone else on the ship"
             "Young Link jumps out on top of the ship with you. He was trying to catch a ride like you to go"
             "go back home with it but he is the last one on here and he crashed the engine so your going to"
             "falling down soon so good luck", "Young Link", None, None, None, "Brinstar")

current_node = journey_hallway
directions = ["north", "south", "east", "west"]
short_directions = ["n", "s", "e", "w"]

while True:
    print(current_node.desc)
    print(current_node.name)  # Change
    command = input('>_'.lower())
    if command == 'quit':
        quit(0)
    elif command in short_directions:
        # Look for which command we typed in
        pos = short_directions.index(command)
        command = directions[pos]
        # change command to be the long form
    if command in directions:
        try:
            current_node.move(command)
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
    if command == "look":
        print(current_node.fighters)
        print(current_node.east)
        print(current_node.north)
        print(current_node.south)
        print(current_node.west)
