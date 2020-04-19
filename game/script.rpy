
################################################################################
## Characters
################################################################################

define c = Character("Cat", who_color=dark_venetian)
define b = Character("Bartender", who_color=dark_venetian)
define r = Character("Rat Dee", who_color=dark_venetian)
define s = Character("Smol Mouse", who_color=dark_venetian)

################################################################################
## Animations
################################################################################

image cat sad animated:
    "cat sad.png"
    pause 1.0
    "cat blink.png"
    pause 0.3
    repeat

image cat happy animated:
    "cat happy.png"
    pause 1.0
    "cat happy blink.png"
    pause 1.0
    repeat

image cat glance animated:
    "cat nani.png"
    pause 1.0
    "cat glance.png"

image bartender blink animated:
    "bartender eye open.png"
    pause 1.0
    "bartender blink.png"
    pause 0.3
    repeat

image bartender whoops animated:
    "bartender whoops.png"
    pause 1.0
    "bartender whoops blink.png"
    pause 0.3
    repeat

image rat dee animated:
    "rat dee.png"
    pause 2.0
    "rat dee blink.png"
    pause 0.3
    repeat

image rat dee gameless animated:
    "rat dee gameless.png"
    pause 1.0
    "rat dee gameless blink.png"
    pause 0.3
    repeat

################################################################################
## Positions
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
    xalign 0.25
    yalign 1.0

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
    show smol meh at behind_bar_right_smol
    show bar
    #show bartender whoops animated at right

    b"Welcome to <Bar Name>!"

    jump scene1
    label endscene1:

    b"You chose [n]"
    b"Once you add a story, pictures, and music, you can release it to the world!"

    # This ends the game.
    return
