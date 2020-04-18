
################################################################################
## Characters
################################################################################

define p = Character("Player", who_color=blizzard_blue)
define b = Character("Bartender", who_color=sunglow)
define r = Character("Rat Dee", who_color=radical_red)

################################################################################
## Script
################################################################################

# The game starts here.
label start:
    scene bg bar
    show eileen happy
    p"You've created a new Ren'Py game."
    p"Once you add a story, pictures, and music, you can release it to the world!"

    # This ends the game.
    return
