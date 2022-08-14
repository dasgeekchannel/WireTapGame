#!/usr/bin/env python3

# coding=utf-8
# Game and story created by DasGeek

# import os
# os.system('')
import climage # install climage to convert png for terminal
import time # provides various time-related functions
import random #for fight calculations
import colorama # text color
from colorama import init, Fore, Back, Style
# Initializes Colorama
init(autoreset=True)


# pip3 install climage dependency
inventory = []
gametitle = climage.convert("wiretap.png")
drone = climage.convert("drone.png")
city = climage.convert("city_cyberpunk.jpg")
total_hp = 150



def death():
    if total_hp <= 0:
        print ("You are dead")
        scene1()

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
        print(" ")
        print('Introduction')
        print(f"Your HP is {total_hp}") #using f string to combine string with numerics
        print(' ')
        print(gametitle)
        print(' ')
        input("Press Enter to continue.") # forces pause and user interaction
        
        # Testing out Fore.RED to convert text to a different color. Can use to differentiate narration vs. actions etc.
        
        print(Fore.RED +""" 

            You step out onto the streets and take a deep breath. 
            Your augment goes to work producing a filtered blast 
            of clean air.

            Before you is a city filled with an endless assortment
            of neon lights and animated holograms force-feeding 
            its message deep into wandering eyes.

            Silhouettes of women dancing alongside various types of 
            augments and quick stop convenience stores. There are 
            brands of every type, all promoting themselves with faces 
            of models and celebrities and influencers begging to be 
            remembered.

            """)
        input("Press Enter to continue.")
        print(city)
        
        print(' ')
        input("Press Enter to continue.")
        
        print("""
            
            The wet streets and towering buildings reach as far as 
            the eyes can see. The assortment of colors from the 
            digital signs bouncing off the grey and black concrete 
            jungle and their glass patios. An endless barrage of lights 
            highlighting the filth of an overpopulated city that had 
            given up on aesthetics long ago.

            """)
        
        print(' ')
        
        input("Press Enter to continue.")
        
        print("""
            
            An assortment of street vendors and loitering 
            patrons seem to go on in an endless maze. There 
            are no mountain views, grass fields, or signs of natural life. 
            You've arrived at Zire. 

            A city once known as a hub for great prosperity but as the 
            population grew the people built up into the skies until they 
            couldn’t build up any longer, so they started 
            building underground. Signs pointing towards underground tunnels 
            leading to the armpit of civilization known as 'The Beneath'. 
            Flying vehicles of various shapes and sizes consumed the 
            skies swarming like hornets protecting a nest. The whizzing 
            and buzzing blending into the sounds of bustling 
            streets.

        """)
        
        input("Press Enter to continue.")
        
        print("""
            The air is moldy and thick. The planet like a body wrapped 
            in rubber. It takes effort to breathe the 
            industrialized air, especially for those without 
            augmentations.

            Your personal assistant suddenly springs to 
            life in your visor.
        
            You notice a duffle bag on the ground lying open. 
            Someone must have left it in a hurry.
        
        """)
        scene1()


# START OF SCENE 1
def scene1():
    print("\nType your choice: take or ignore?")
    c1 = input(">>")
    ans = "incorrect"
    while ans == "incorrect":
        if c1.lower() == "take":
            print("""
            
                "You scrumage inside the weathered bag and find an old pair of gym clothes.
                As you keep searching you notice a zipper pocket on the 
                outside of the bag with something heavy inside. 
                Upon inspection of the pocket you find a pair of brass knuckles."
            
            """)
            inventory.append("Brass Knuckles") # add item into inventory
            print(" ")
            print(str(inventory) + " has been added to your inventory") #print the inventory out to the player
            print(" ")
            ans = "correct"
            scene2()
        elif c1.lower() == "ignore":
            print("You ignore the bag as it might be some kind of trap.")
            print("Probably nothing...right?")
            ans = "correct"
            scene2()
        else:
            print("ENTER THE CORRECT CHOICE! Lowercase 'take' or 'ignore?'")
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
            print("""
            You decide to turn right and see a several neon signs 
            and shops in the distance.As you get closer to the shops
            you see there is general store, a VR World and an 
            augmentation shop. 

            Your map tells you to keep moving forward toward an alley
            at the end of the street. 

            As you get near the augmentation shop you notice there is 
            an obese short bald man who seems to being paying special,
            attention to you as you approach.
            
            You continue past the shop and notice the merchant is still
            eyeing you closely.As you pass him, you notice he points at 
            you and whistles.
            
            A massive robot grabs your arm and lifts you into the alleyway
            
            They push you into an alleyway before you have a a chance 
            to turn back around. There is a large 


            """)
            input("Press Enter to continue.")
            ans='correct'
            c3 = input(">>")
            while ans == "incorrect":
                if c3.lower =="talk":
                    print("this is a test")
                    scene3()
                elif c3.lower =="run":
                    print("this is also a test")
                    scene3()
            print(str(inventory))
            scene3()
            ans = 'correct'
        elif c1.lower() == "left":
            print("""
            You turn to the left and proceed down a dark alleyway. 
            The streets are littered with trash and used needles.
            A nearby buzzing sound enters your ears grabbing your 
            attention. You find the source of the noise as a giant 
            drone drops from the sky directly in your path.
            """)
            input("Press Enter to continue.")
            print("""

            'Welcome patron, please register.' you notice the drone 
            is a quadcopter with a massive round lens which keeps 
            focusing and refocusing as if impatiently waiting for a 
            response. The drone is badly weathered but the camera 
            seems recently upgraded. On the outside of the drone's
            lens is a ring of light emitting a green'ish hue.

            """)
            input("Press Enter to continue.")
            
            print("""
            
            'Welcome citizen, please present bar code.' the drone
            is a quadcopter with a massive round lens which keeps
            focusing and refocusing over and over again as if 
            impatiently waiting for a response. The drone had 
            signs of once being brightly colored with faded 
            strips of paint that was now badly weathered but 
            the camera seems recently upgraded. On the outside 
            of the drone's lens is a ring of light emitting a red hue.
            
            """)
            print(drone)
            input("Press Enter to continue.")
            print("Do you want to 'register'? or 'attempt hack' ? ")
            ans = 'correct'
    c2 = input(">>")
    ans = "incorrect"
    while ans == "incorrect":
        if c2.lower()== "register":
            print(""" 

            you lift your sleeve revealing a bare arm with no barcode. 
            The drones lens focuses in floats backwards defensively
            'Another recycled war drone' ...you think to yourself 
            your eyes are fixated on the barrel hanging from the bottom of the drone.

            """)
            
            time.sleep(1)
            print("'Yes, register'...you say aloud.' ")
            time.sleep(1)
            
            print("""
            'Please present registration chip.' the drone's voice echoed 
            with a synthesized and broken tone. You lift the sleeve of 
            your shirt revealing a bare arm to the drone's camera.
            "The drone quickly floats backwards a few feet. The gun 
            barrel at the bottom of the drone is pointing directly at you.
            Red lights illuminate on the drone as it prepares to attack you.
            'Unregistred citizens are in violation of code 816-3 and are 
            subject to arrest. Please stay where you are.'
            You can't be arrested again or you'll face life in prison. 
            You know what you have to do.
            
            """)
            
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
    global total_hp #set to global to allow damage to continue reducing HP. 
    print(total_hp)
    print("***You Are In A Fight***")
    print("A: punch")
    print("B: kick")
    if "Brass Knuckles" in inventory:
        print("C: Use Brass Knuckles")
    decision=input('What action do you choose: A,B, or C? ')

    minPoint=1
    maxPoint=100

    ChA=(random.randint(minPoint,maxPoint))*.85
    ChB=(random.randint(minPoint,maxPoint))*.33
    ChC=(random.randint(minPoint, maxPoint))*.95
    DMG_ind=(random.randint(minPoint, maxPoint))



    if decision.upper()=='A' and ChA>25 and total_hp >0:
        print('you punch at the drone but it easily dodges out of the way.')
        print('You see a dart whiz past your face.')
        print('Your HUD identifies the object as a tranquilizer dart')
        print('You might have one more chance to take the drone down.')
        total_hp=total_hp - DMG_ind
        print(total_hp)
        fight1()

    elif total_hp <0:
        print("you are dead")
        print(" ")
        print("Game Over")
        print(" ")
        input("Press Enter to continue.")
        scene2()

    elif decision.upper()=='B' and ChB>25:
        print('you kick the drone')
        print('the drone loses balance and crashes into a light pole.')
        print("You notice a figure standing in the shadows. Your vision goes blurry and you collapse to the ground")
        scene3()

    elif decision.upper()=='C' and ChC>25 and 'Brass Knuckles' in inventory:
        print('you use your brass knuckles')
        print('the punch bursts the glass camera and send the drone into a spin')
        print("You notice a figure standing in the shadows. Your vision goes blurry and you collapse to the ground")
        scene3()
    else:
            print("You regret your poor decision making")
            fight1()


# Story choices above all lead here eventually.


def scene3():
    print("""
        Well, well, you're finally awake. That drone hit you with a 
        tranquilzer dart. What were you thinking attacking a 
        corporate drone with no weapons?
        """)
    
    time.sleep(2.0) #make story auto continue after pause for reader
    
    print("""
        You look around and notice a storage room full of metal shelves, 
        boxes overflowing with electronics. 
    """)

    time.sleep(2.0)
    
    print("""
        My name is Uzman. Nice to meet you.
    """)
    
    time.sleep(2.0)
    
    print("""
        As your vision becomes more clear you notice that you're strapped 
        down to a table. You look down and notice your augments have been 
        removed from your arms and legs. There are large open wounds 
        where your augments once resided. You see a scalpel covered 
        in blood on the table beside you. You try to access your HUD 
        but there is no overlay
        """)

    time.sleep(2.0)

    print("""
        Imagine my surprise when I found you passed out with over a million 
        Eth in augments. Just know it's nothing personal. You don't look a 
        gift horse in the mouth as they say. I could leave you for dead and 
        dump you back where I found you. 
        I'm greedy...but I'm not evil, you know?
        """)
    
    time.sleep(2.0)
    
    print("""
        You notice you can move your fingers on your right arm. 
        Pain starts to register as you become more awake and reality 
        sets in.
        """)
    
    time.sleep(2.0)
    
    print("""
        You're not registered with the government...
        so it's not like they would even investigate your death.
        """)
    
    input("Press Enter to continue.")


    print("What your name offworlder? : ")
    name = input(">>>")
    print ("Well hello "+name)
    print ("""
        'So here is what's going to happen next. I'm going to put you back to 
        sleep and sew you up. No need to thank me kid. You're going to be 
        dumped in 'The Beneath' where you will likely have your wounds 
        become infected by all of sewage and filth and die of infection. 
        If you do live, well, you will wish you didn't. I should just as well
        kill you right here and now. The only thing keeping you alive is the 
        fact that someone important told me you're not to die today. They want
        you alive for something. Do you know what that something is? 
        """)
    print("")
    print("You respond with 'money'? or 'die scum' ")
    print("")
    ans = 'correct'
    c3 = input(">>>")
    ans = "incorrect"
    while ans == "incorrect":
        if c3.lower()== 'money':
            print("""
                'Money drives me...not them.'
                """)
            print("")
            ans = "correct"
            scene4()
        elif c3.lower()=='die scum':
            print("""
                'No, wrong answers.'
                """)
            print("")            
            ans = "correct"
            scene4()

def scene4():
    print(""" 
        Vengeance...I'm guessing? Lots and lots of pain they want to 
        cause you. You must have messed up all kinds of bad for these
        people to want you to suffer. I'm also to tell you that 
        I'm phase one of their vengeance. Phase two...'Uzman shrugs 
        his shoulders' probably going to be even worse. 

        Anyways...that's all I'm supposed to tell you. So goodnight and 
        thank you for the augments. I'm going to use some of these personally
        for myself. 

        """)
    end()

def end():
    print ("You've reached the end for now...")
    quit()


   # c3 = input(">>")
   # print ("What would you like to do? A. Fight B. Scream")
   # ans = "incorrect"
   # while ans = "incorrect":
   #     if c1 = "A"
   #     print 




# either way they wake up in the store from Drone battle or they travel safely to the store going right

game()
