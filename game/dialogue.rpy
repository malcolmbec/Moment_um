label dialogue:
    scene bg bar with dissolve
    show cat sad_animated at behind_bar_left_cat
    show smol
    show bar

    "You walk up to the mouse and attempt to greet them."
    s"You’re a cat!"

    show smol anger at behind_bar_right_smol_anger

    s"Why is a cat here?"

    ## Menu 1
    show cat sad

    menu:
        "\"Well, I thought it seemed like a cool shop.\"":
            jump opt1_1
        "\"Do you have any drink recommendations?\"":
            jump opt1_2
        "\"I’m trying to make friends.\" ":
            jump opt1_3
    label opt1_1:

        show smol anger_animated

        c"Well, I thought it seemed like a cool shop."
        s"Seems pretty fishy."
        c"I don’t know what you mean."


        s"Well… you’re a cat,{w} and most of us are mice."
        s"Really, you should just leave."
        jump end1
    label opt1_2:
        c"Do you have any drink recommendations?"
        s"Why do you want a drink recommendation from me?"
        c"I thought maybe you came here often."
        s"Because I’m a mouse?!"
        c"Oh, um, no! I just meant…"
        jump end1
    label opt1_3:
        c"I’m trying to make friends."
        s"But you’re a cat,{w} why would you try to make friends here?{w} Seems like you don’t belong here."
        c"Erm, I think maybe we could all learn to be friends?"
        s"Or maybe you’re hiding something!"
        c"Uh, what?{w} No!"
        jump end1
    label end1:

    "Seems like befriending this mouse will be harder than you expected.{w} What should you say next?"

    ## Menu 2
    menu:
        "Ask if they’re a regular.":
            jump opt2_1
        "Ask about the usual regulars at the cafe.":
            jump opt2_2
    label opt2_1:
        c"Are you here often?"
        s"What’s it to you?"
        c"You seem like you know this place well."
        s"So?"
        c"Uh…"
        s"Leave before I fight you!"
        "Oh that’s not good, maybe you should try something else."
        ## Submenu 2
        menu:
            "Ask something different.":
                jump opt2_2
            "Maybe it’s best if I talk to someone else...":
                jump end2
    label opt2_2:


        c"I’ve never been here before, but they seem busy."
        s"You seem too interested in the patrons."
        c"What, no, why?"
        s"You’re a cat, maybe you’re up to something."
        c"I’m just trying to make some friends..."
        jump end2
    label end2:

    "Tensions are high, let’s change the topic all together."

    c"Do you drink a lot of coffee?"

    show smol meh at behind_bar_right_smol_anger

    s"I come here for black coffee a lot"

    show cat nani

    c"Um, isn’t that bitter?"

    show cat sad

    s"The only thing bitter around here is me."
    c"..."

    "Hm, well I guess they’re straight forward at least.{w} How should you respond?"

    ## Menu 3
    menu:
        "\"I’ll try the black coffee then.\"":
            jump opt3_1
        "\"I’m not really a coffee drinker myself.\"":
            jump opt3_2
        "\"Are you okay?\"":
            jump opt3_3
    label opt3_1:
        c"I’ll try the black coffee then."
        s"Wait, seriously? You’ll try even though you think it’s bitter?"
        c"Hm. Maybe I should suggest something you’d definitely enjoy then."
        "Seems the small mouse might be opening up! Maybe you can be friends after all."
        jump end3
    label opt3_2:
        c"I’m not really a coffee drinker myself."
        s"Why would you come here then?"
        c"Well I mean, um, most cafes have other things too."
        s"That makes no sense, it’s a coffee shop, if you’re not going to drink coffee, you should leave."
        ## Submenu 3
        menu:
            "Maybe you should try the coffee?":
                jump opt3_1
            "Might be best to regroup with the bartender and try talking to someone else...":
                jump end3
    label opt3_3:
        c"Are you okay?"

        show smol pull_animated at behind_bar_right_smol_pull

        s"You’re right, I don’t even like coffee."
        c"Why are you drinking it then?"
        s"Because I thought the caffeine would help me."

        show cat wink

        c"Let’s try something new together instead."
        s"I can’t believe you’re being nice to me after all the mean things I’ve said."

        show cat happy

        "See, all the mouse needed was a friend."
        python:
            smol_friend = True
        jump end3
    label end3:

    if smol_friend:
        "You befriended Smol Mouse!"
    else:
        "You did not make friends with Smol Mouse. :("

    jump endscene
