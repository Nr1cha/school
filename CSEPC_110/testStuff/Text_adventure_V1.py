import ascii_magic

death = ascii_magic.from_image_file("skull.jpeg",
                                    columns=60,
                                    width_ratio=2,
                                    )

answer = input("would you like to playa game? (yes/no) ")

if answer.lower().strip() == "yes":

    weapon = input("You awake and find yourself in a dark and thick forested woods on a foggy night, before going on an adventure you must choose a weapon for protection. Which do you choose? (sword/wand) ").lower().strip()
    if weapon == "sword" \
            or "wand":
        print("")
        answer = input(
            "You encounter a deadly troll, you have two options, you can either risk your life and try to defeat the troll or flee. (fight/flee) ")
        if answer == "fight":
            print(
                f"The troll swings his heavy club over your head, barely missing your neck. You can feel the goosebumps on your skin rise. You take your {weapon}, rising it directly over your head...")
            if weapon == "sword":
                print("Your attack does no damage to the massive troll. The club comes at you again, this time landing directly upon your head.")
                print(f"You have died. Try again.\n{death}")
            else:
                spell = input(
                    "What spell would you like to cast? (stun/attack)")
                if spell == "stun":
                    print(
                        "The troll freezes in his tracks. You consider this a win and head home.")
                else:
                    print(
                        "Your attack does no damage to the massive troll. The club comes at you again, this time landing directly upon your head.")
                    print("You have died. Try again.")
        else:
            print("")
            print("you run quickly into the forest, outrunning the big slow troll.")
            print("You then come across a large cave in the side of a mountain. \nOutside the cave you see a scratched-up wooden sign, on it you can bearly make out the words 'please knock, all those who enter here'.")
            print("Thinking how odd of a sign that would be, you decide 'why not, seems nice', \nIn it you find a mess of Gold scattered about and a low breeze of air that seems to get stronger as you traverse deeper into the cave. ")
            print("As you round the corner, you find a sleeping dragon")
            print("")
            answer = input("After picking up some gold, you decide it's time to leave, upon seeing the dragon move as if close to waking up, you think to yourself, \n'should i run or sneak out'? (run/sneak) ")
            if answer == "run":
                print("")
                print(
                    "The dragon wakes up and sees you running. Upon spewing fire all around you, you turn into a pile of ash.")
                print("you have died, better luck on the next respawn")
            else:
                print("")
                print("you make it out alive without disturbing the dragon. in a low valley you find a town to exchange your gold for riches and then the story ends ")
                print("keep watch for more DLC (which is free BTW, none of that microtransactiony fluff) to see new features and stories.")

    else:
        print("well that sucks")
else:
    print("that's too bad")
