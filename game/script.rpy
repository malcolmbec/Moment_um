
################################################################################
## Characters
################################################################################

define p = Character("Player", who_color=dark_venetian)
define b = Character("Bartender", who_color=dark_venetian)
define r = Character("Rat Dee", who_color=dark_venetian)

################################################################################
## Positions/Animations
################################################################################

transform behind_bar_left_smol:
    xalign 0.1
    yalign 0.65

transform behind_bar_right_smol:
    xalign 0.9
    yalign 0.65

transform behind_bar_left_rat:
    xalign 0.1
    yalign 0.25

transform behind_bar_right_rat:
    xalign 0.9
    yalign 0.25

transform behind_bar_left_cat:
    xalign 0.1
    yalign 0.4

transform behind_bar_right_cat:
    xalign 0.9
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
    show cat sad at behind_bar_left_cat
    show rat dee at behind_bar_right_rat
    show bar

    b"Welcome to <Bar Name>!"

    jump scene1
    label endscene1:

    b"You chose [n]"
    b"Once you add a story, pictures, and music, you can release it to the world!"

    # This ends the game.
    return
