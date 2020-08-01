from sys import exit #to exit the game
from random import randint

class scene(object):
    def enter(self):
        print("this will be work on later cases lets work on the subclasses for a while")
        exit(1)


class engine(object):
    def __init__(self,scene_map):
        self.scene_map=scene_map
    def play(self):
        current_scene=self.scene_map.opening_scene()

        while True:
            print("\n---------------------------------")
            next_scene_name=current_scene.enter()
            current_scene=self.scene_map.next_scene(next_scene_name)
            
class death(scene):
    out=[ " You died. you Kinda suck at this.",
          " Your mom would have been proud...if you were smarter",
          " Such a loser",
          " I didn't expect this from you" ]

    def enter(self):
        print(death.out[randint(0,len(self.out)-1)])
        exit(1)

class central_corridor(scene):
    def enter(self):
        print("The gotham of planet perceal #25 have invited your ship and destroyed It",)
        print("your entire crew died. And now you have to complete the mission and escape by the escape pod.",)
        print("The mission is to get the neutron destruct bomb from the weapons army",)
        print("put it in the bridge, and blow the ship up after getting into the escape pod")

        print("now to compete the mission you started running in the central corridor to the weapons Armory........")
        print("There suddenly a gothon jumps out, with his red scaly skin, dark gritty teath and evil clown costyuem,")
        print("flowing around his body.",)
        print("Opps.... He notices u and try to pull up a weapon to blast you.")
        print("\n\n You have three options 'shoot', 'dodge' or 'Tell a joke' \n type in what you will do")
        #here i have to add a timer and to please input  in 10 9 8...     
        action = input("> ")

        if action =="shoot":
            print("Quikly you draw out your blasterr and fire it at gotham in a jist of a second")
            print("------------------------------------------------------")
            print("But the gotham was aware and he move swiftly and doges",)
            print("While giving you a bararge of blast by his blaster until you are in pieces")
            return 'death'

        elif action=='dodge':
            print("like a professional athelete you dodge the bullet and slip through him",)
            print("showing a your middle thumb to gotham and BANG! you bumbped into the wall and pass out ",)
            print("being a good dinner for gotham")
            return 'death'

        elif action=='Tell a joke':
            print("Lucky for you they made you learn jokes for gotham which can leave them into laughter")
            print("you said:'bhe zbgure vf fb sng, jura fur fvgf nebhaq gur ubhfr, fur fvgf nebhaq gur ubhfr'")
            print("the gotham stops. tries not to laugh, and then busts out laughing exposing his body for a critical shot &")
            print("BANG!!!!!")
            print("shooting into his head he crumbels down giving you a path to the Weapon armory door")
            return 'laser_weapon_armory' 

        else:
            print("Your reflexes are to slow to save you from gothans bullet")
            return "death"   


class laser_weapon_armory(scene):
    def enter(self):
        print("You have successfuly entered the laser weapon armory,",)
        print("But the atmosphere here is too quiet which shouldn't be in an armory",)
        print("You scan the room and check if there are any gotham's in the area")
        print("seeing this as an opportunity, you run far side of the room and find the neutron bomb, hidden inside the container",)
        print("There's a keypad lock on the box and you need to crack the code to get the bomb out",)
        print("If you get the code wrong 10 times, then lock locks forever and shoots the alarm,")
        print("giving you a hoard of gotham to welcome you")
        print("The code is of 3 digits try to crack the code.")
        print("Enter your choice of three numbers seperated by a spac eg. 1 2 3")

        code =("%d %d %d" % (randint(1,9), randint(1,9), randint(1,9)))
        guess = input("[keypad]> ")
        guesses = 0
        while guess != code and guesses < 10:
            print("ERRORR!!!!!!!!!!!!!!!!!!!")
            if   guesses==3 :
                print("Seems like u need help.I have a hint for you the first number is %s",code[:1])
            elif guesses==7 :
                print("well i feel pity for u,the first & second number is %s",code[:3])
            elif guesses == 8:
                print("ookkh the lastt number is between ")
            guesses += 1
            guess = input("[keypad]> ")
        if guess == code :
            print("The container clicks and the seal breaks,letting a weird gas out and you see a horde of gotham at the front of laser weapon army gate",)
            print("Seeing the gotham you grab the neutron bomb and run as fast as you can to the bridge,",)
            print("where u can place the bomb and get into the escape pod")
            return 'bridge'
        else:
            print("The lock shwos the ERRORR last time and in a split of second a hord of gothams surround you for a feast")
            return 'death'

class bridge(scene):
    def enter(self):
        print("You burst onto the bridge with the neutron bomb",)
        print("while a horde of gothams are still trying to catch you and shooting laser's ",)
        print("at the bridge suddenly there are 5 gothams in front of you")
        print("they stop right there as they see neutron bomb in your hand and dont want to distroy their ship")
        
        action =input("> ")

        if action == 'throw the bomb':
            print("In a panic u throw the bomb at the 5 gothams and leap through the bridge ",)
            print("one of them shoots you right at the back killing you ")
            return 'death'

        elif action == 'point your gun at the bomb':
            print("You point your blaster at the bomb under your arm")
            print("and the Gothons put their hands up and start to sweat.")
            print("You inch backward to the door, open it, and then carefully")
            print("place the bomb on the floor, pointing your blaster at it.")
            print("You then jump back through the door, punch the close button")
            print("and blast the lock so the Gothons can't get out.")
            print("Now that the bomb is placed you run to the escape pod to")
            print("get off this tin can.")
            return 'escape_pod'

        else:
            print("You were too late to make a decision and the gothams catch you snatching the bomb,")
            print("of you and the having a feast with you")
            return 'death'


class escape_pod(scene):
    def enter(self):
        print("You rush through the ship desperately trying to make it to")
        print("the escape pod before the whole ship explodes. It seems like")
        print("hardly any Gothons are on the ship, so your run is clear of")
        print("interference. You get to the chamber with the escape pods, and")
        print("now need to pick one to take. Some of them could be damaged")
        print("but you don't have time to look. There's 5 pods, which one")
        print("do you take?")

        good_pod=randint(1,5)
        guess=input("[pod #]> ")

        if int(guess)!=good_pod:
            print("You jump into pod %s and hit the eject button.",guess)
            print("The pod escapes out into the void of space, then")
            print("implodes as the hull ruptures, crushing your body")
            print("into jam jelly.")
            return 'death'
        
        else:
            print("You jump into pod %s and hit the eject button.",guess)
            print("The pod easily slides out into space heading to")
            print("the planet below. As it flies to the planet, you look")
            print("back and see your ship implode then explode like a")
            print("bright star, taking out the Gothon ship at the same")
            print("time. You won!")
            return 'finished'


class map(object):
    # class map has a funtion and initialsie funct start scenn
    scenes = {'central_corridor':central_corridor(),'laser_weapon_armory':laser_weapon_armory(),'bridge':bridge(),'escape_pod':escape_pod(),'death':death()}
    def __init__(self,start_scene):
        self.start_scene = start_scene

    def opening_scene(self):
        return self.next_scene(self.start_scene)

    def next_scene(self,scene_name):
        return map.scenes.get(scene_name)


mapp = map('central_corridor')
engine = engine(mapp)
engine.play()



