# coding=utf-8
# Game and story created by DasGeek
import climage
import time
import random #for fight calculations


# install climage to convert png for terminal
# pip3 install climage dependency
inventory = []
gametitle = climage.convert("wiretap.png")
drone = climage.convert("drone.png")


def game():
    import random # for battle calculations
    answer = input("would you like to play a game? (y/n)")

    if answer.lower() == "y":
        print("Welcome to Wiretap")
        print(" ")
        start = True

    else:
        start = False
        print("Ok, some other time")
    if start == True:
        print("	")
        print('Introduction')
        print(' ')
        print(gametitle)
        print(' ')
        print(
            'You step out onto the streets and take a deep breath. Your augment goes to work producing a filtered blast of clean air.')
        print(
            'Before you is a city filled with an endless assortment of neon lights and animated holograms force-feeding its message deep into wandering eyes.')
        print(' ')
        print(
            'Silhouettes of women dancing alongside augments and quick stop convenience stores. There are brands of every type, all promoting')
        print('themselves with faces of models and celebrities and influencers begging to be remembered.')
        print(' ')
        time.sleep (1)
        print(
            'The wet streets and towering buildings reach as far as the eyes could see. The assortment of colors from the digital signs bouncing off')
        print(
            'the grey and black concrete jungle and their glass patios. An endless barrage of lights highlighting the filth of an overpopulated city')
        print('that had given up on aesthetics long ago.')
        print(' ')
        print(
            'There was an assortment of street vendors and loitering patrons that seem to go on in an endless maze. There are no mountain views,')
        print(
            "grass fields, or signs of natural life. You've arrived at Zire. A city once known as a hub for great prosperity but as the population")
        print(
            'grew the people built up into the skies until they couldn’t build up any longer, so they started building underground. Signs pointing towards')
        print(
            'underground tunnels leading to the armpit of civilization known as The Beneath. Flying vehicles of various shapes and sizes consumed the skies,')
        print(
            'swarming like hornets protecting a nest. The whizzing and buzzing blending into the sounds of bustling streets.')
        print(' ')
        time.sleep (1)
        print(
            'The air is moldy and thick. The planet like a body wrapped in rubber. It takes effort to breathe the industrialized air, especially for those')
        print('without augmentations.')
        print(' ')
        print('Your personal assistant suddenly springs to life in your visor.')
        print(' ')
        print('You notice a duffle bag on the ground lying open. Someone must have left it in a hurry.')
        print(' ')
        scene1()


# START OF SCENE 1
def scene1():
    print("\nType your choice: take or ignore?")
    c1 = input(">>")
    ans = "incorrect"
    while ans == "incorrect":
        if c1.lower() == "take":
            print(
                "You scrumage inside and find old pair of gym clothes.\n As you keep searching you notice a zipper pocket on the outside of the bag with something heavy inside. \n Upon inspection of the pocket you find a pair of brass knuckles.\n"
            )
            inventory.append("Brass Knuckles")
            print(" ")
            print(str(inventory) + " has been added to your inventory")
            ans = "correct"
            scene2()
        elif c1.lower() == "ignore":
            print("You ignore the bag as it might be some kind of trap.")
            print("Probably nothing...right?")
            ans = "correct"
            scene2()
        else:
            print("ENTER THE CORRECT CHOICE! Lowercase take or ignore?")
            c1 = input(">>")


# START OF SCENE 2
def scene2():
    print("Your personal assistant comes to life with a map. Your path leads you to a sidewalk which goes off to the left and right, which direction do you want to go?"
    )
    print("Do you want to walk to the left or right?")
    c1 = input(">>")
    ans = "incorrect"
    while ans == "incorrect":
        if c1.lower() == "right":
            print('You decide to turn right and see a several neon signs and shops in the distance.')
            print('As you get closer to the shops you see there is general store, a VR World and an') 
            print('augmentation shop. As you get near the augmentation shop you notice there is an obese') 
            print('short bald man who seems to being paying special,attention to you as you approach.') 
            ans = "correct"
            print(str(inventory))
            scene3()
        elif c1.lower() == "left":
            print("You turn to the left and proceed down a dark alleyway. The streets are littered with trash and used needles.\n")
            print("A nearby buzzing sound enters your ears grabbing your attention. You find the source of the noise as a giant \n drone drops from the sky directly in your path.\n")
            print(" ")
            input("Press Enter to continue.")
            print("'Welcome patron, please register.' you notice the drone is a quadcopter with a massive round lens which keeps focusing and refocusing as")
            print("if impatiently waiting for a response. The drone is badly weathered but the camera seems recently upgraded.\n")
            print("On the outside of the drone's lens is a ring of light emitting a green'ish hue.\n")
            input("Press Enter to continue.")
            print("'Welcome citizen, please present bar code.' the drone is a quadcopter with a massive round lens which keeps focusing \n ")
            print("and refocusing over and over again as if impatiently waiting for a response. The drone had signs of once being brightly colored \n with faded strips of paint that was now badly weathered but \n ")
            print("the camera seems recently upgraded. On the outside of the drone's lens is a ring of light emitting a red hue.\n")
            print(drone)
            input("Press Enter to continue.")
            print("Do you want to 'register'? or 'attempt hack' ? ")
            ans = 'correct'
    c2 = input(">>")
    ans = "incorrect"
    while ans == "incorrect":
        if c2.lower()== "register":
            print(" you lift your sleeve revealing a bare arm with no barcode. The drones lens focuses in floats backwards defensively")
            print(" 'Another recycled war drone' ...you think to yourself ")
            print("your eyes are fixated on the barrel hanging from the bottom of the drone. ")
            time.sleep(1)
            print("'Yes, register'...you say aloud.' ")
            time.sleep(1)
            print("'Please present registration chip.' the drone's voice echoed with a synthesized and broken tone. ")
            print("You lift the sleeve of your shirt revealing a bare arm to the drone's camera.")
            print("The drone quickly floats backwards a few feet. The gun barrel at the bottom of the drone is pointing directly at you.")
            print("Red lights illuminate on the drone as it prepares to attack you.")
            print("'Unregistred citizens are in violation of code 816-3 and are subject to arrest. Please stay where you are.'")
            print("You can't be arrested again or you'll face life in prison. You know what you have to do.")
            input("Press Enter to Continue.")
            print("You currently have this in your inventory:")
            print(inventory)
            fight1()
            ans = "correct"
        elif c2.lower()=="attempt hack":
            print("you hack it")
            inventory.append("eye augmentation")
            ans = "correct"


# Define Fight 1 Simple Enemy
def fight1():
    print("***You Are In A Fight***")
    print("A: punch")
    print("B: kick")
    print("C: Use Brass Knuckles")
    decision=input('What action do you choose: A,B, or C? ')

    minPoint=1
    maxPoint=100

    ChA=(random.randint(minPoint,maxPoint))*.85
    ChB=(random.randint(minPoint,maxPoint))*.33
    ChC=(random.randint(minPoint, maxPoint))*.95

    if decision.upper()=='A' and ChA>25:
        print('you punch the drone')
        print('the drone shoots you with a tranquilizer dart')

    elif decision.upper()=='B' and ChB>25:
        print('you kick the drone')
        print('the drone loses balance and crashes into a light pole.')

    elif decision.upper()=='C' and ChC>25 and 'Brass Knuckles' in inventory:
        print('you use your brass knuckles')
        print('the punch bursts the glass camera and send the drone into a spin')
    else:
        print("Your hit didn't work, you're going to jail")

def scene3():
    print("welcome to my store")


game()
