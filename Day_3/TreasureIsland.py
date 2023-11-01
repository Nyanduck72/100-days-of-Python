# This is a text-based game based on player choices
# Game start
print("You have wandered the jungle for quite some time now... you're getting impatient and rations are running low")
print("Swing after swing of your machete, you cut through the dense foliage until you come at the edge of a cliff...")
print("To your right, a fallen tree creates a bridge across the gap")
print("To your left, a series of outcroppings in the cliff look like a way down the cliff")
choice_1 = int(input("Which way do you choose?\n1.- Go right\n2.- Go left\n3.- Do nothing\n"))

# Go right across the bridge
if choice_1 == 1:
    print("The tree trunk creaks as you walk slowly across it to the other side of the cliff...")
    print("After walking for a few minutes, you find an old wooden treehouse. The overgrowth on it makes it almost unrecognizable")
    print("You notice the skeleton of a skydiver tangled in the branches of the tree. It has a backpack")
    choice_1_1 = int(input("What will you do?\n1.- Try to cut it down\n2.-Leave it be\n"))
    # Try to cut it down
    if choice_1_1 == 1:
        print("You decide to climb into the treehouse, looking for a way to the skeleton.")
        print("The ladder, although very unstable, still holds your weight.")
        print("You can barely reach the skeleton with your machete, just enough to cut the parachute´s strings")
        print("You search inside the backpack for any useful items, but there is just a can of beans")
        print("You are very tired. A quick snack could give you a boost, but who knows how long that can has been there...")
        choice_1_2 = int(input("Will you eat the beans?\n1.- Yes, I´m starving!\n2.- I think I´ll pass...\n"))
        # Game Over - Quick Snack
        if choice_1_2 == 1:
            print("You snap the can open and get hit with a horrible stench that makes your eyes tear up.")
            print("You quickly down the beans hoping that the taste isn´t as bad as the smell. You are VERY wrong.")
            print("Almost instantly, you feel very ill and collapse. Your last memory is the foul taste of the bean sludge")
            print("G A M E  O V E R")
        # Not eating the beans
        if choice_1_2 == 2:
            print("Your common sense overcomes your hunger and you decide to leave the treehouse.")
            print("As you come down the ladder, it snaps, making it impossible to get to the treehouse again...")
            print("You continue through the jungle until you find a large cave entrance")
            print("There is some sort of ancient device made of stone on the entrance.")
            print('"Finally, a sign that I´m going in the right place!", you say to yourself')
            print("The cave is pitch black. You make a makeshift torch out of a branch and some cloth")
            print("As you explore the deeper parts of the cave, you hear a faint click.")
            print("A boulder drops behind you, blocking your way out of the cave...")
            print("As you continue down the cave, you see daylight and hear a waterfall.")
            print("It is very foggy, but you recognize that you´re outside now, at the bottom of the cliff")
            print("You see a shimmer across a large river. It looks like the treasure!")
            print("You stick your hands in the river to drink. The current is strong, but it can be crossed easily")
            choice_1_2_1 = int(input("What do you do?\n1.- Cross the river\n2.- Hop across some rocks to the other side\n"))
            # WIN
            if choice_1_2_1 == 1:
                print("You struggle to cross the river but help yourself by holding on to various rocks and edges to avoid slipping")
                print("Congratulations!, you´ve found the treasure and can (hopefully) pay off the trip to the island!")
            # Game Over - So Close!
            if choice_1_2_1 == 2:
                print("The rocks are very slippery and you fall. The current is too strong for your tired body and drags you away...")
                print("G A M E  O V E R")
    # Leave it be
    if choice_1_1 == 2:
        print("You feel too tired to climb. You move on and head left of the treehouse.")
        print("You don´t recognize it at first, but you´ve stumbled into the wreckage of a plane. Most likely the one the skydiver jumped out of")
        print("After looking around for a while, you find some old maps leading to the island, along with some schematics of some device")
        print("Just as you try to leave the remains of the plane, the roar of a jaguar breaks the relative silence of the jungle...")
        choice_1_1_2 = int(input("What will you do?\n1.- Stay in the plane and hide\n2.- Draw your machete and try to leave\n"))
        # Game Over - Stand your Ground
        if choice_1_1_2 == 1:
            print("You barricade the cockpit of the plane with a piece of fuselage. You accidentally cut yourself...")
            print("The faint noise of the bushes moving around make it clear that it caught the scent of your blood")
            print("You draw your machete, but it´s very hard to hold with a wounded hand...")
            print("When you least expected it, the jaguar pounces at you from the cockpit window.")
            print("Even though you managed to kill it, the damage is done and you lie down feeling sleepy...")
            print("G A M E  O V E R")
        # Game Over - Watch your step
        if choice_1_1_2 == 2:
            print("You bravely draw your machete and slowly step out of the crashed plane.")
            print("The noise comes from too many directions and it´s very difficult to focus...")
            print("You keep your back stuck to the fuselage, trying to get back to the treehouse.")
            print("Using all your energy, you make a run for it, tripping on a tree root and dropping your machete.")
            print("The jaguar was right behind and you´ve become it´s next meal...")
            print("G A M E  O V E R")
# Go left down the cliff
if choice_1 == 2:
    print("You find a sturdy rock near the edge to tie a rope around, then begin your descent...")
    print("Putting one foot at a time, you shuffle along the cliff face. It begins to rain.")
    print("You feel the grip of your fingers start to fail as the crevices get slippery. You have to get off now!")
    print("You can probably make the nearest jump into a small cave in the cliff face, but taking your time is safer...")
    choice_1_1_3 = int(input("What will you do?\n1.- Jump to the cave\n2.- Slowly shuffle to the cave\n"))
    # Jump to the cave
    if choice_1_1_3 == 1:
        print("You jump as far as you can and barely hold on to the edge, but you lose the machete...")
        print("Wet and tired, you decide to wait out the rain by taking a short nap")
        print("A few hours later, it´s now night and the rain has stopped")
        print("Without your machete, you can´t replace the now frayed rope with a dry one...")
        print("You decide to risk it and, if it comes to it, free climb down the cliff")
        print("The darkness doesn't help much when climbing, but you continue anyway")
        print("The moonlight reflects off something in an outcrop of the cliff. It could be the machete!")
        print("As you climb even more down, your rope snaps. An error now could be fatal.")
        print("You see the end of a waterfall. The water seems deep enough to stop the fall.")
        print("The machete is also close...")
        choice_1_1_4 = int(input("What do you do?\n1.- Jump to the lake\n2.- Reach for the machete\n"))
        # Game Over - Watery Grave
        if choice_1_1_4 == 1:
            print("You jump into the lake, but you get tangled at the bottom of the lake in some vines and roots")
            print("With no way to get out, you drown...")
            print("G A M E  O V E R")
        if choice_1_1_4 == 2:
            print("You reach for the machete, barely grabbing it. You slip and fall into the lake below...")
            print("You get tangled at the bottom of the lake in vines and roots. The machete sinks slowly besides you")
            print("Quickly, you reach for it and cut yourself loose. You swim to the surface and swim to shore")
            print("You catch your breath, not realizing that the treasure is right in front of you...")
            print("Congratulations!, you´ve found the treasure and can (hopefully) pay off the trip to the island!")
    # Game Over - Don´t leave me hanging
    if choice_1_1_3 == 2:
        print("You shuffle along as fast as you can, but you end up slipping and hanging in your harness")
        print("You try swinging your weight to grab a ledge again, but you´re too far away.")
        print("The knot at the top of the cliff starts to undo because of the weight. You can only wait until gravity takes you out...")
        print("G A M E  O V E R")
# Do nothing
if choice_1 == 3:
    print("You stand there, stunned at the thought of the amount of choices offered to you at this moment")
    print("Your anxiety kicks in and starts imagining every possible outcome: falling, food poisoning, drowning, mauled by a jaguar, etc.")
    print("You decide to not venture into the jungle and trace back your steps to the boat...")
    print("NEUTRAL ENDING - Nothing special happened :/")


