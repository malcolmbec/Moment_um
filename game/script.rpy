################################################################################
## Stats
################################################################################

python:
    smol_friend = False
    ratdee_friend = False

################################################################################
## Characters
################################################################################

$ name = "Cat"

define c = Character("[name]", who_color=plum)
define b = Character("Barista", who_color=dark_venetian)
define r = Character("Rat Dee", who_color=jazzberry_jam)
define s = Character("Smol Mouse", who_color=cosmic_cobalt)

################################################################################
## Animations
################################################################################

image cat sad_animated:
    "cat sad.png"
    pause 2.0
    "cat blink.png"
    pause 0.3
    repeat

image cat happy_animated:
    "cat happy.png"
    pause 1.0
    "cat happy blink.png"
    pause 1.0
    repeat

image cat glance_animated:
    "cat nani.png"
    pause 1.0
    "cat glance.png"

image barista blink_animated:
    "barista eye open.png"
    pause 1.0
    "barista blink.png"
    pause 0.3
    repeat

image barista whoops_animated:
    "barista whoops.png"
    pause 1.0
    "barista whoops blink.png"
    pause 0.3
    repeat

image ratdee animated:
    "rat dee.png"
    pause 2.0
    "rat dee blink.png"
    pause 0.3
    repeat

image ratdee gameless_animated:
    "rat dee gameless.png"
    pause 1.0
    "rat dee gameless blink.png"
    pause 0.3
    repeat

image smol anger_animated:
    "smol anger.png"
    pause 2.0
    "smol pfff.png"
    pause 0.2
    repeat

image smol pull_animated:
    "smol pull normal.png"
    pause 1.5
    "smol pull blink.png"
    pause 0.2
    repeat

image smol pull anger_animated:
    "smol pull anger.png"
    pause 1.5
    "smol pull blink.png"
    pause 0.2
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

transform behind_bar_left_smol_anger:
    xalign 0.1
    yalign 0.67

transform behind_bar_right_smol_anger:
    xalign 0.9
    yalign 0.67

transform behind_bar_left_smol_pull:
    xalign 0.1
    yalign 0.62

transform behind_bar_right_smol_pull:
    xalign 0.9
    yalign 0.62

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

transform leftish:
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
    show cat glance at behind_bar_left_cat
    show bar

    python:
        name = renpy.input(_("What's your name?"))
        name = name.strip() or __("Cat")

    show cat sad at behind_bar_left_cat
    show bar
    show barista friendly at right

    b"Hello [name]! Welcome to the cafe, can I help you?"
    c"..."

    show barista blink_animated at right

    b"I see.{w} Well, some might think you’re out of place here,{w} but I say the more the merrier!"
    b"Don’t let others discourage you.{w} With some perseverance you’ll be able to befriend everyone here!"

    show barista friendly at right

    b"In the meantime, if you want,{w} why don’t you start with getting some menu recommendations from our regulars?"
    b"Normally I would help you in this area,{w} but since you want to make friends this a good starting point!"

    show barista eye open at right

    b"Let me know how things go.{w} I’ll be cheering for you!"

    jump dialogue
    label endscene:

    ## Credits???

    # This ends the game.
    return
