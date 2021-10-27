import os
os.system("cls")
# 1 YES
    ##FIGHTER##
    # 1.2 SWORD
        # FIGHT 
            # DEATH
        # FLEE
            # MOVE TO THE MOUNTAIN
                #1.3 MOUNTAIN
                #
                # RUN 
                    #DEATH
                # SNEAK
                    #WIN

    ##WIZARD##
    # 1.2 WAND
        # ATTACK
            # DEATH
        # STUN
            # MOVE TO THE MOUNTAIN
                #1.3 MOUNTAIN
                # 
                # RUN
                    #DEATH
                # SNEAK
                    #WIN
# 2 NO
Black = "\u001b[30m."
Red = "\u001b[31m."
Green = "\u001b[32m."
Yellow = "\u001b[33m."
Blue = "\u001b[34m."
Magenta = "\u001b[35m."
Cyan = "\u001b[36m."
White = "\u001b[37m"

#BEGINNING OF STORY
answer = input("would you like to playa game? YES or NO ")

if answer.lower() == "yes":

    weapon = input("You awake and find yourself in a dark and thick forested woods on a foggy night, before going on an adventure you must choose a weapon for protection. Which do you choose, SWORD or WAND? ").lower()
    if weapon == "sword" \
            or "wand":
        answer = input("You encounter a deadly troll, you have two options, you can either risk your life and try to defeat the troll or flee. FIGHT or FLEE? ")
        if answer.lower() == "fight":
            print(f"The troll swings his heavy club over your head, barely missing your neck. You can feel the goosebumps on your skin rise. You take your {weapon}, rising it directly over your head...")
            if weapon.lower() == "sword":
                print("Your attack does no damage to the massive troll. The club comes at you again, this time landing directly upon your head.")
                print(f"{Red} You have died adventurer. Try again.")
            #WIZARD PART
            else:
                spell = input("What spell would you like to cast, STUN or ATTACK?")
                if spell.lower() == "stun":
                    print("The troll freezes in his tracks. You consider this a win and head home.")
                else:
                    print("Your attack does no damage to the massive troll. The club comes at you again, this time landing directly upon your head.")
                    print(f"{Red}You have died wizard. Try again.")
        else:
            # MOUNTAIN SECTION
            print("")
            print("you run quickly into the forest, outrunning the big slow troll.")
            print("You then come across a large cave in the side of a mountain. \nOutside the cave you see a scratched-up wooden sign, on it you can bearly make out the words 'please knock, all those who enter here'.")
            print("Thinking how odd of a sign that would be, you decide 'why not, seems nice', \nIn it you find a mess of Gold scattered about and a low breeze of air that seems to get stronger as you traverse deeper into the cave. ")
            print("As you round the corner, you find a sleeping dragon")
            print("")
            #RUN AND DEATH PART
            answer = input("After picking up some gold, you decide it's time to leave, upon seeing the dragon move as if close to waking up, you think to yourself, \n'should i run or sneak out'? RUN, SNEAK or WAIT: ")
            if answer.lower() == "run":
                print("")
                print("The dragon wakes up and sees you running. Upon spewing fire all around you, you turn into a pile of ash.")
                print(f"{Red}you have died, better luck on the next respawn")
            if answer.lower() == "wait":
                    print("you wait till night, as you ready yourself to leave you find the dragon is gone.")
                    print("you make it to the hill right over the village and find that the dragon is terrorizing the people")
                    print("you can choose to assist and rally the people to defeat the dragon or wait till all is finished and see if there is anything left in the morning")
                    answer = input("ASSIST or COWER: ")
                    if answer.lower() == "assist":
                        print("you rally what people you can find and defeat the dragon, the land prospers by the riches in the mountain and you as well.")
                        print("good job adventurer you did it!")
                    if answer.lower() == "cower":
                        print("you wait till morning on the outskirts, you return to the town and find that most are all killed.")
                        print("there is no way to obtain riches and as you leave, you see the dragon not far behind you ready to strike. unable to escape, you die wishing you had chosen to be a little more brave before")
                        print(f"{Red}you die")
            else:
            #SNEAK ESCAPE PART
                print("")
                print("you make it out alive without disturbing the dragon. in a low valley you find a town to exchange your gold for riches and then the story ends ")
                print("keep watch for more DLC (which is free BTW, none of that microtransactiony fluff) to see new features and stories.")
    else:
        print("well that sucks")
else:
    print("that's too bad")
