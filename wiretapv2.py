#!/usr/bin/env python3

# coding=utf-8
# Game and story created by DasGeek

# import os
# os.system('')
import climage # install climage to convert png for terminal
import time # provides various time-related functions
import random #for fight calculations
import colorama # text color
import random
from colorama import init, Fore, Back, Style
# Initializes Colorama
init(autoreset=True)


# pip3 install climage dependency
inventory = []
gametitle = climage.convert("wiretap.png")
drone = climage.convert("drone.png")
city = climage.convert("city_cyberpunk.jpg")

# random int, str, and health generator
intelligence=[4,6,10]
random_int=random.choice(intelligence)


strength=[4,6,10]
random_str=random.choice(strength)



health=[100,150,200]
total_hp=random.choice(health)




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
        #print(f"Your HP is {total_hp}") #using f string to combine string with numerics
        print(' ')
        print(gametitle)
        print(' ')
        input("Press Enter to continue.") # forces pause and user interaction
        
        # Testing out Fore.RED to convert text to a different color. Can use to differentiate narration vs. actions etc.
        
        print("Stats have been randomly generated for your character:")

        print("Your strength is >>> "+str(random_str))
        print("Your intelligence is >>> "+str(random_int))
        print("Your hp is >>> "+str(total_hp))
        time.sleep(2)
        print(""" 

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
    print("""
        Your personal assistant comes to life with a map. 
        Your path leads you to a sidewalk which goes off to the 
        left and right, which direction do you want to go?"
    """)
    print("")
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
            #c3 = input(">>")
            #while ans == "incorrect":
             #   if c3.lower =="talk":
              #      print("this is a test")
               #     scene3()
                #elif c3.lower =="run":
                 #   print("this is also a test")
                  #  scene3()
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
        else:
            print("ENTER THE CORRECT CHOICE! Lowercase 'left' or 'right?'")
            c1 = input(">>")   
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
            print("""
                You hack it but not before it shoots something.
                A numbness rises from your legs. The scenery
                begins to blur. You and the drone fall to the
                ground in unison. The eye of the drone hangs
                from some wires. You grab it and yank it from
                the wires. As you see the augment in your grip
                your vision goes dark. You have a few more 
                moments of consciousness before you pass 
                out entirely.

                """)
            inventory.append("eye augmentation")
            ans = "correct"
            scene3()
        else:
            print("ENTER THE CORRECT CHOICE! Lowercase 'register' or 'attempt hack?'")
            c1 = input(">>")       

# Define Fight 1 Simple Enemy
def fight1():
    global total_hp #set to global to allow damage to continue reducing HP. 
    print(total_hp)
    print("***You Are In A Fight***")
    print("A: punch")
    print("B: kick")
    if "Brass Knuckles" in inventory: #looks in inventory to determine whether to give option C
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
    print(Fore.RED +"""
        Well, well, you're finally awake. That drone hit you with a 
        tranquilzer dart. What were you thinking attacking a 
        corporate drone with no weapons?
        """)
    
    time.sleep(2.0) #make story auto continue after pause for reader
    
    print("""
        You notice you're in a storage room with rows of of metal shelves, 
        piled high with boxes that are overflowing with electronics, 
        augments, and parts of various robotics.  
    """)

    time.sleep(2.0)
    
    print("""
        Your vision is suddenly consumed with a strange bald man
        wearing a white doctors coat and wearing a headband full of
        various gadgets and lights. On one eye he had a magnification
        glass hanging over. He was bent over the table looking at your
        legs. You notice his lips are slobbery amplified by the lights
        beaming down from his headband, drool is pooling at the sides 
        of his mouth.The man turns and you can see his magnified right eye 
        grow wide with surprise.  
            """)

    time.sleep(1.0)

    print(Fore.RED +"""

        Well, well, look who decided to awaken early. 
        The name is Uzman. Uh...Nice to meet you.
        """)
    
    time.sleep(1.0)
    
    print("""
        As your vision becomes more clear you realize you're strapped 
        down to a metal table. You strain your neck to look down as 
        your vision clears and notice your augments have been removed 
        from your legs. There are large crude stitches and staples running
        down to your knee where your augments once resided. 
        You try to access your HUD but, an error blinks on across
        your overlay
        
        'connection lost'.
        
        """)

    input("Press Enter to continue.")

    print(Fore.RED +"""
        Imagine my surprise when I found out you had over a million 
        Eth in augments. Just know it's nothing personal. You don't look a 
        gift horse in the mouth as they say. Don't fret over the legs.
        I could leave you open take everything and dump you back where I 
        found you. I'm greedy...but I'm not evil, you know?
        """)
    
    time.sleep(2.0)
    
    print("""
        You notice you can move your fingers on your right arm. 
        Pain starts to register as you become more awake and reality 
        sets in.
        """)
    
    input("Press Enter to continue.")
    
    print(Fore.RED +"""
        You're not registered with the government...
        so it's not like they would even investigate your death.
        """)
    
    input("Press Enter to continue.")


    print("What your name offworlder? : ")
    name = input(">>>")
    print("Well hello "+name)
    print(Fore.RED +"""
        'So here is what's going to happen next %s. I'm going to put 
        you back under and take the rest of these augs. 
        I'll sew you up...don't you worry. 
        """)
    time.sleep(1)
    print("""
        Uzman holds up his hand. You notice it's trembling. A smile
        cracks across his lips. 
        """)
        
    print(Fore.RED +"""
        When you wake up you'll be knee deep in 'The Beneath'. The stinking,
        wretched, armpit of our society. There...well, you'll likely get 
        an infection in your wounds from the sewage and filth...then a fever, 
        your wounds will get all black and green, your skin will start 
        rotting and pulling away from the wounds and then after a lot of 
        pain you will die. But, if you do survive, well, you'll wish you 
        didn't. No augs, no weapons, they'll eat you alive. 
        Quite literally too.
        
        Now listen closely...don't even think about getting revenge. 
        I have eyes all over. Electronic and natural, they all look 
        out for Uncle Uzman. You understand what I'm telling 
        you offlander?
        """)

    print("")
    print("You respond with 'no'? or 'die scum' ")
    print("")
    ans = 'correct'
    c3 = input(">>>")
    ans = "incorrect"
    while ans == "incorrect":
        if c3.lower()== 'no':
            print(Fore.RED +"""
                Too bad, you'll be all natural soon enough. Nighty night
                """)
            print("")
            ans = "correct"
            scene4()
        elif c3.lower()=='die scum':
            print(Fore.RED +"""
                I'll take that as a yes. Just for that I'm going to take some 
                teeth while your out too. Street market price on natural teeth
                is through the roof lately. 
                """)
            print("")            
            ans = "correct"
            scene4()
        else:
            print("ENTER THE CORRECT CHOICE! Lowercase 'money' or 'die scum?'")
            c3 = input(">>>")   
def scene4():
    print(""" 
        Uzman walks over to the counter grabbing a syringe. He slowly squeezes
        the plunger until a clear liquid drips out the top. You hear him
        chuckling to himself as he turns back towards you. 
        """)
    scene5()

def end():
    print ("You've reached the end for now...")
    quit()


   # c3 = input(">>")
   # print ("What would you like to do? A. Fight B. Scream")
   # ans = "incorrect"
   # while ans = "incorrect":
   #     if c1 = "A"
   #     print 

def scene5():
    print("Make a choice: 'look around' or 'scream'")
    ans = 'incorrect'
    c5 = input(">>>")
    while ans =='incorrect':
        if c5.lower() == 'look around':
            print ("""
            You look around the room and notice the scalpel is just 
            within reach. Your arm moves towards it, but the pain shoots 
            through your arm like a thousand razers. Fighting through it
            your fingers manage to grab the metal handle of the blade. 
            The signals from your brain to your hand are in slow motion
            yet you manage to get it straight and into your fist tightly
            the sharp scalpel upright, ready to slash. Struggling you 
            start to pull it back towards you, carefully trying not to
            knock anything off the table. Just as you clear the tray
            the metal handle connects sending a loud 'ting'.

            Uzman sees you, he turns and comes rushing. His hand holding
            the syringe extended outwards. Suddenly Uzman slips on a pool 
            of blood. His shoes screech against the tile floors and he 
            crashes face first onto the surgical tray.
            The scalpel you were holding goes straight into his eye.
            Uzman's weight collapses the side table and you lose grip of
            the scalpel which gets shoved further into Uzmans head as his
            head smacks the floor.
            """)
            ans == 'correct'
            scene6()
        elif c5.lower() =='scream':
            print ("""

            You start to panic and scream for help as loud as you can.
            Uzman gets visibly agitated and shoves the needle into the 
            IV. You start to loose consciousness as the room begins to
            spin
            """)
            ans=='correct'
            scene7()

def scene6():
    end()

def scene7():
    end()


# either way they wake up in the store from Drone battle or they travel safely to the store going right

game()
