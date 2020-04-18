
################################################################################
## Characters
################################################################################

define p = Character("Player", who_color=radical_red)
define b = Character("Bartender")
define r = Character("Rat Dee")

################################################################################
## Script
################################################################################

# The game starts here.
label start:
    scene bg room
    show eileen happy
    p"You've created a new Ren'Py game."
    p"Once you add a story, pictures, and music, you can release it to the world!"

    # This ends the game.
    return
