print("  Welcome to Treasre Island")
print("-----------------------------")

choice_1 = input(
    "Welcome to Treasure Island! Your mission is to find the hidden treasure. Choose wisely, or face dire consequences. Are you ready to begin? (yes/no)"
)

if choice_1 == "no":
    print(
        "The island disappears before your eyes. Maybe next time you'll have the courage to find the treasure. Game over!"
    )
elif choice_1 == "yes":
    choice_2 = input(
        "You find yourself at a fork in the road. The path to the left is shady and mysterious, while the path to the right is sunny and clear. Which path will you choose? (left/right)"
    )
    if choice_2 == "right":
        print(
            "You stroll along the sunny path, admiring the beautiful landscape. Suddenly, quicksand pulls you under. Looks like your treasure hunting days are over. Game over!"
        )
    elif choice_2 == "left":
        choice_3 = input(
            "A fast-flowing river blocks your way. You can try to swim across or look for a bridge further downstream. What will you do? (swim/bridge)"
        )
        if choice_3 == "swim":
            print(
                "You dive bravely into the water, only to realize too late that the river is filled with hungry piranhas. Better luck next time. Game over!"
            )
        elif choice_3 == "bridge":
            choice_4 = input(
                "After crossing the river, you stumble upon a dark cave. There’s faint treasure glimmer coming from inside, but strange noises echo from within. Will you enter the cave or walk past it? (enter/walk)"
            )
            if choice_4 == "walk":
                print(
                    "You decide not to enter the cave and continue walking. Unfortunately, you wander in circles until nightfall and are never heard from again. Game over!"
                )
            elif choice_4 == "enter":
                choice_5 = input(
                    "At last, you reach the treasure room, but there's a fierce guardian dragon asleep in front of it. Will you sneak past or confront the dragon? (sneak/confront)"
                )
                if choice_5 == "confront":
                    print(
                        "You charge at the dragon, sword in hand, ready for battle. The dragon simply yawns and incinerates you with a single blast of fire. Game over!"
                    )
                elif choice_5 == "sneak":
                    print(
                        "Congratulations! You’ve found the hidden treasure and become a legend of Treasure Island!"
                    )
