
################################################################################
## Characters
################################################################################

define p = Character("Player", who_color=blizzard_blue)
define b = Character("Bartender", who_color=sunglow)
define r = Character("Rat Dee", who_color=radical_red)

################################################################################
## Positions/Animations
################################################################################

transform behind_bar_left:
    xalign 0.1
    yalign 0.4

transform rightish:
    xalign 0.75
    yalign 1.0

################################################################################
## Script
################################################################################

# The game starts here.
label start:
    scene bg bar
    show cat sad at behind_bar_left
    show bar
    show bartender friendly at rightish

    b"You've created a new Ren'Py game."

    jump scene1
    label endscene1:

    b"You chose [n]"
    b"Once you add a story, pictures, and music, you can release it to the world!"

    # This ends the game.
    return
